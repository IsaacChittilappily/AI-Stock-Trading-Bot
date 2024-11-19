import numpy as np

# basic code for a neuron
class Neuron:
    def __init__(self, weights: np.ndarray, bias: float) -> None:
        self.weights = weights
        self.bias = bias

    def forward(self, inputs: np.ndarray) -> float:
        return np.dot(inputs, self.weights) + self.bias

inputs = np.array([1.0, 2.0, 3.0, 2.5])
weights = np.array([0.7, 0.4, 1.2, 2.3])
bias = 3.0

neuron = Neuron(weights, bias)
print(neuron.forward(inputs))



def reLu(x):
    return max(0, x)


inputs = [
    [1.0, 2.0, 3.0, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
         ]

class layerDense:
    def __init__(self, n_inputs, n_neurons) -> None:
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forwardPass(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class reLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)



layer1 = layerDense(4, 5)
layer2 = layerDense(5, 2)

layer1.forwardPass(inputs)
print(layer1.output)
layer2.forwardPass(layer1.output)
print(layer2.output)