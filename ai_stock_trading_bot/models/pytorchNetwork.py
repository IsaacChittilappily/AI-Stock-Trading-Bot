from ai_stock_trading_bot.database.pull_db_data import get_data_from_db
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# pull the data from the data for a specific symbol from the database
db_path = 'ai_stock_trading_bot/database/historical_data.db' 
table_name = 'NVDA'
data = get_data_from_db(db_path, table_name)


# separate features and target (the target is the next day's closing price)

# all rows except the last one
X = data[:-1]

# next day's closing price (index 3 refers to the 'Close' column)
y = data[1:, 3]


# split into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, shuffle=False)

# standardize the data (scaling features to have zero mean and unit variance)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)

# convert to PyTorch tensors
X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.float32).view(-1, 1)
X_val_tensor = torch.tensor(X_val_scaled, dtype=torch.float32)
y_val_tensor = torch.tensor(y_val, dtype=torch.float32).view(-1, 1)


# creates class for the neural network
class StockPredictor(nn.Module):
    def __init__(self):
        super(StockPredictor, self).__init__()
        # a simple fully connected network with 2 hidden layers
        self.fc1 = nn.Linear(5, 64)  # input layer (5 features -> 64 neurons)
        self.fc2 = nn.Linear(64, 64) # hidden layer
        self.fc3 = nn.Linear(64, 1)  # output layer (1 value - next day's closing price)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)  # no activation for the output
        return x

# initialize model, loss function, and optimizer
model = StockPredictor()
criterion = nn.MSELoss()  # mean squared error loss for regression
optimizer = optim.Adam(model.parameters(), lr=0.001)


# training loop
num_epochs = 100
batch_size = 32  
train_loader = torch.utils.data.DataLoader(list(zip(X_train_tensor, y_train_tensor)), batch_size=batch_size, shuffle=True)

for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    for i, (inputs, targets) in enumerate(train_loader):
        # zero the parameter gradients
        optimizer.zero_grad()

        # forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # backward pass and optimization
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    # validation after each epoch
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_val_tensor)
        val_loss = criterion(val_outputs, y_val_tensor)

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}, Val Loss: {val_loss.item():.4f}")


# predicting the next days closing price
model.eval()

# get the last row of data
last_day_data = data[-1].reshape(1, -1)

# Scale the data using the same scaler
last_day_scaled = scaler.transform(last_day_data)
last_day_tensor = torch.tensor(last_day_scaled, dtype=torch.float32)

# predict the next day's closing price
with torch.no_grad():
    predicted_close = model(last_day_tensor)
    print(f"Predicted next days closing price: {predicted_close.item():.4f}")
