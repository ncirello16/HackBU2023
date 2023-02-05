import random
import json
import torch
import os.path
from trainData import trainTheData
from model import NeuralNet
from nltkUtils import BagOfWords, Tokenize

if not (os.path.exists('bin/data.pth')):
    trainTheData()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('bin/intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "bin/data.pth"
data = torch.load(FILE)

inputSize = data["inputSize"]
hiddenSize = data["hiddenSize"]
outputSize = data["outputSize"]
allWords = data["allWords"]
tags = data["tags"]
modelState = data["modelState"]

model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)
model.load_state_dict(modelState)
model.eval()

botName = "ChatBot"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = Tokenize(sentence)
    x = BagOfWords(sentence, allWords)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    output = model(x)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{botName}: {random.choice(intent['responses'])}")
    else:
        print(f"{botName}: I do not understand...")