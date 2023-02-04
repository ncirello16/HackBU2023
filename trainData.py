import numpy as np
import json

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

from nltkUtils import BagOfWords, Tokenize, Stem
from model import NeuralNet


def trainTheData():
    with open('bin/intents.json', 'r') as f:
        intents = json.load(f)

    allWords = []
    tags = []
    xy = []
    # loop through each sentence in our intents patterns
    for intent in intents['intents']:
        tag = intent['tag']
        # add to tag list
        tags.append(tag)
        for pattern in intent['patterns']:
            # tokenize each word in the sentence
            w = Tokenize(pattern)
            # add to our words list
            allWords.extend(w)
            # add to xy pair
            xy.append((w, tag))

    # stem and lower each word
    ignoreWords = ['?', '.', '!']
    allWords = [Stem(w) for w in allWords if w not in ignoreWords]
    # remove duplicates and sort
    allWords = sorted(set(allWords))
    tags = sorted(set(tags))

    print(len(xy), "patterns")
    print(len(tags), "tags:", tags)
    print(len(allWords), "unique stemmed words:", allWords)

    # create training data
    xTrain = []
    yTrain = []
    for (patternSentence, tag) in xy:
        # X: bag of words for each pattern_sentence
        bag = BagOfWords(patternSentence, allWords)
        xTrain.append(bag)
        # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
        label = tags.index(tag)
        yTrain.append(label)

    xTrain = np.array(xTrain)
    yTrain = np.array(yTrain)

    # Hyper-parameters
    numEpochs = 1000
    batchSize = 8
    learningRate = 0.001
    inputSize = len(xTrain[0])
    hiddenSize = 8
    outputSize = len(tags)
    print(inputSize, outputSize)

    class ChatDataset(Dataset):

        def __init__(self):
            self.nSamples = len(xTrain)
            self.xData = xTrain
            self.yData = yTrain

        # support indexing such that dataset[i] can be used to get i-th sample
        def __getitem__(self, index):
            return self.xData[index], self.yData[index]

        # we can call len(dataset) to return the size
        def __len__(self):
            return self.nSamples

    dataset = ChatDataset()
    trainLoader = DataLoader(dataset=dataset,
                             batch_size=batchSize,
                             shuffle=True,
                             num_workers=0)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model = NeuralNet(inputSize, hiddenSize, outputSize).to(device)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learningRate)

    # Train the model
    for epoch in range(numEpochs):
        for (words, labels) in trainLoader:
            words = words.to(device)
            labels = labels.to(dtype=torch.long).to(device)

            # Forward pass
            outputs = model(words)
            # if y would be one-hot, we must apply
            # labels = torch.max(labels, 1)[1]
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch + 1}/{numEpochs}], Loss: {loss.item():.4f}')

    print(f'final loss: {loss.item():.4f}')

    # Create a dictionary
    data = {
        "modelState": model.state_dict(),
        "inputSize": inputSize,
        "outputSize": outputSize,
        "hiddenSize": hiddenSize,
        "allWords": allWords,
        "tags": tags
    }

    FILE = "bin/data.pth"
    torch.save(data, FILE)

    print(f'training complete. File saved to {FILE}')
