import numpy as np
from ai_stock_trading_bot.database.pull_db_data import get_data_from_db

def predict_stock_price(symbol):
    db_path = 'ai_stock_trading_bot/database/historical_data.db'
    data = get_data_from_db(db_path, symbol)

    class SimpleNeuralNetwork:
        def __init__(self, input_size, hidden_size, output_size):

            # initialize weights and biases with random values
            self.w1 = np.random.randn(input_size, hidden_size)
            self.b1 = np.zeros((1, hidden_size))
            self.w2 = np.random.randn(hidden_size, output_size)
            self.b2 = np.zeros((1, output_size))


        def forward(self, X):
            self.z1 = np.dot(X, self.w1) + self.b1
            self.z2 = np.dot(self.z1, self.w2) + self.b2
            # no activation on the output layer for regression
            return self.z2  

        
        def train(self, X, y, epochs):
            for epoch in range(epochs):
                output = self.forward(X)
                # calculate loss but skip updating weights (because I am not using backpropogation yet)
                if epoch % 100 == 0:
                    loss = np.mean(np.square(y - output))
                    print(f"epoch {epoch}, loss: {loss}")

        def predict(self, X):
            return self.forward(X)

    # prepare data
    X = data[:-1]    # all but the last day
    y = data[1:, 3]  # close prices of the next day
    y = y.reshape(-1, 1)  # reshape close prices to fit the network

    # create and train the network
    nn = SimpleNeuralNetwork(input_size=5, hidden_size=10, output_size=1)
    nn.train(X, y, epochs=1000)

    # make a prediction
    prediction = nn.predict(X[-1].reshape(1, -1))
    predicted_price = prediction[0][0] * np.max(data[:, 3])
    
    return predicted_price
