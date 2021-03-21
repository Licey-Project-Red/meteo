import numpy as np
import json
 
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
 
with open('20_years_format\\Алмазный.json', 'r', encoding='utf-8') as fh:
    data = json.load(fh)

inputs = []
outputs1 = data[366:5476]
for i in range(5110):
    inputs.append(data[i:i+365])
print(len(inputs), len(outputs1))


def train(inputs, outputs1):
    training_inputs = np.array(inputs)
    
    training_outputs = np.array([outputs1]).T
    
    np.random.seed(42)
    
    synaptic_weights = 2 * np.random.random((365, len(inputs))) - 1
    print("Случайные веса: ")
    print(synaptic_weights)
    

    for i in range(20000):
        input_layer = training_inputs
    
        outputs = sigmoid(np.dot(input_layer, synaptic_weights))
        if i == 1:
            print(outputs)
        err = training_outputs - outputs
    
        adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))
        synaptic_weights += adjustments
    
    print("Веса после обучения: ")
    print(synaptic_weights)
    
    print("Результат после обучения: ")
    for out in outputs:
        print(round(float(out) * 10))


train(inputs, outputs1)