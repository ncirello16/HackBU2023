import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

# YOU MIGHT HAVE TO DOWNLOAD THIS
# nltk.download('punkt')

stemmer = PorterStemmer()


def Tokenize(sentence):
    # Separate the sentence by words and punctuation
    return nltk.word_tokenize(sentence)


def Stem(word):
    # Stem the words, get prefixes
    return stemmer.stem(word.lower())


def BagOfWords(tokenizedSentence, allWords):
    # Lets say sentence = ["hello, "how", "are", "you"]
    # words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    # BOF =   [ 0,     1,     0,    1,      0,      0,      0]
    tokenizedSentence = [Stem(word) for word in tokenizedSentence]
    bag = np.zeros(len(allWords), dtype=np.float32)
    for idx, word, in enumerate(allWords):
        if word in tokenizedSentence:
            bag[idx] = 1.0

    return bag


sentence = ["hello", "how", "are", "you"]
words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
bag = BagOfWords(sentence, words)
print(bag)

