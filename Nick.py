import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def Tokenize(sentence):
    # Separate the sentence by words and punctuation
    return nltk.word_tokenize(sentence)


def Stem(word):
    # Stem the words, get prefixes
    return stemmer.stem(word.lower())


def BagOfWords(tokenizedSentence, allWords):
    pass


a = "How are you doing?"
print(a)
a = Tokenize(a)
print(a)
stemmedWords1 = [Stem(b) for b in a]
print(stemmedWords1)

words = ["organize", "organizes", "organizing"]
stemmedWords2 = [Stem(word) for word in words]
print(stemmedWords2)

