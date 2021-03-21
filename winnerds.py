import numpy as np
import json


def sigmoid(x):
    try:
        return 1 / (1 + np.exp(-x))
    except Exception as E:
        print(E)


with open('20_years_format/txt_files/kurort.txt', 'r', encoding='utf-8') as fh:
    data = [float(i.strip()) for i in fh.readlines()]
print(type(data))

inputs = []
outputs1 = data[366:5476]
print(len(inputs), len(outputs1))

synaptic_weights = ''

err = 0
def train(inputs, outputs1):
    global synaptic_weights, err
    training_inputs = np.array(inputs)

    training_outputs = np.array([outputs1]).T

    np.random.seed(42)

    synaptic_weights = 2 * np.random.random((365, len(inputs))) - 1
    # print("Случайные веса: ")
    # print(synaptic_weights)
    err = 0
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))
    if i == 1:
        print()
    err = training_outputs - outputs


    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
    synaptic_weights += adjustments

    print("Результат после обучения: ")
    for out in outputs:
        print(round(float(out) * 10))


for i in range(5110):
    inputs = data[i:i + 365]

train(inputs, outputs1)