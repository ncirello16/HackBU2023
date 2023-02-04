import json
import numpy as np
import torch
import torch.nn as nn

from model import NeuralNet
from torch.utils.data import Dataset, DataLoader
from Nick import Tokenize, Stem, BagOfWords

with open("intents.json", 'r') as f:
    intents = json.load(f)

# Create the empty lists
allWords = []
tags = []
xy = []

for intent in intents["intents"]:
    tag = intent["tag"]
    tags.append(tag)
    for pattern in intent["patterns"]:
        w = Tokenize(pattern)
        allWords.extend(w)
        xy.append((w, tag))

ignorePunctuation = ['?', "!", ",", "."]
allWords = [Stem(word) for word in allWords if word not in ignorePunctuation]
allWords = sorted(set(allWords))
tags = sorted(set(tags))

xTrain = []
yTrain = []
for (patternSentence, tag) in xy:
    bag = BagOfWords(patternSentence, allWords)
    xTrain.append(bag)

    label = tags.index(tag)
    yTrain.append(label)

# Training Data
xTrain = np.array(xTrain)
yTrain = np.array(yTrain)


class ChatDataSet(Dataset):
    def __init__(self):
        self.nSamples = len(xTrain)
        self.xData = xTrain
        self.yData = yTrain

    def __getitem__(self, index):
        return self.xData[index], self.yData[index]

    def __len__(self):
        return self.nSamples


batchSize = 8
hiddenSize = 8
outputSize = len(tags)
inputSize = len(xTrain[0])

dataset = ChatDataSet()
trainLoader = DataLoader(dataset=dataset, batch_size=batchSize, shuffle=True, num_workers=2)

model = NeuralNet(inputSize, hiddenSize, outputSize)