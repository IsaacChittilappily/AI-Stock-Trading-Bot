import numpy as np
import sqlite3

def get_data_from_db(db_path, table_name):
    # connect to the database
    c = sqlite3.cect(db_path)
    cursor = c.cursor()

    # fetch the data
    query = f"SELECT Open, High, Low, Close, Volume FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()

    # close the cection
    c.close()

    # convert to numpy array
    data = np.array(data, dtype=float)

    return data

db_path = 'historical_data.db'
table_name = 'AAPL_stock_data'    
data = get_data_from_db(db_path, table_name)


class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.001):
        # initialize weights and biases with smaller random values
        self.w1 = np.random.randn(input_size, hidden_size) * 0.01
        self.b1 = np.zeros((1, hidden_size))
        self.w2 = np.random.randn(hidden_size, output_size) * 0.01
        self.b2 = np.zeros((1, output_size))
        self.learning_rate = learning_rate

    def tanh(self, x):
        return np.tanh(x)
    
    def relu(self, x):
        return max(1, x)

    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2

    def forward(self, X):
        self.z1 = np.dot(X, self.w1) + self.b1
        self.a1 = self.tanh(self.z1)
        self.z2 = np.dot(self.a1, self.w2) + self.b2
        output = self.z2  # no activation on the output layer for regression
        return output

    def backward(self, X, y, output):
        # calculate loss (mean squared error)
        loss = y - output
        d_output = loss

        # backpropagation
        d_w2 = np.dot(self.a1.T, d_output)
        d_b2 = np.sum(d_output, axis=0, keepdims=True)

        d_a1 = np.dot(d_output, self.w2.T)
        d_z1 = d_a1 * self.tanh_derivative(self.a1)

        d_w1 = np.dot(X.T, d_z1)
        d_b1 = np.sum(d_z1, axis=0, keepdims=True)

        # update weights and biases
        self.w1 += self.learning_rate * d_w1
        self.b1 += self.learning_rate * d_b1
        self.w2 += self.learning_rate * d_w2
        self.b2 += self.learning_rate * d_b2

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)

            if epoch % 100 == 0:
                loss = np.mean(np.square(y - output))
                print(f"epoch {epoch}, loss: {loss}")

    def predict(self, X):
        return self.forward(X)

# prepare data (assuming the last column is the close price to predict)
X = data[:-1]  # all but the last day
y = data[1:, 3]  # close prices of the next day

def z_score_scaler(X):
    X_mean = np.mean(X, axis=0)
    X_std = np.std(X, axis=0)
    return (X - X_mean) / X_std

# scale the inputs and outputs
X = z_score_scaler(X)
y = z_score_scaler(y)
y = y.reshape(-1, 1)

# create and train the network
nn = SimpleNeuralNetwork(input_size=5, hidden_size=10, output_size=1, learning_rate=0.001)
nn.train(X, y, epochs=1000)

# make a prediction (for the last day in your dataset)
prediction = nn.predict(X[-1].reshape(1, -1))
print(f"predicted close price: {prediction[0][0] * np.max(data[:, 3])}")
