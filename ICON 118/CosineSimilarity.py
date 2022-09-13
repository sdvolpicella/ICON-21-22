import Utils
import pandas as pd
from scipy import spatial
import pickle
import os

def deleteStopwords(text):
    ROOT_DIR = os.path.abspath(os.curdir)
    directory = Utils.fixPath(ROOT_DIR)
    it_stops = deserializeStopSet(ROOT_DIR + '/resources/Stopwords.dat')

    #print(it_stops)

    textWords = text.split()
    for word in textWords:
        if (it_stops.__contains__(word.lower())):
            textWords.remove(word)

    return textWords
def deleteMarks(text):
    count = 0
    for word in text:
        word = word.replace('.', '')
        word = word.replace(',', '')
        word = word.replace(';', '')
        word = word.replace('_', '')
        word = word.replace('-', '')
        word = word.replace('!', '')
        word = word.replace('?', '')
        word = word.replace('[', '')
        word = word.replace(']', '')
        word = word.replace('#', '')
        word = word.replace('"', '')
        word = word.replace('(', '')
        word = word.replace(')', '')
        word = word.replace('â', '')
        word = word.replace('‹', '')
        word = word.replace('€', '')
        word = word.replace('¦', '')
        word = word.replace(':', '')
        word = word.replace('™', '')
        word = word.replace('ã', '')
        word = word.replace('²', '')
        word = word.replace('¹', '')
        word = word.replace('¨', '')
        text[count] = word
        count += 1
    return text
def toLowerText(text):
    count = 0
    for word in text:
        word = word.lower()
        text[count] = word
        count += 1
def preprocessText(text):
    textWords = deleteStopwords(text)
    textWords = deleteMarks(textWords)
    toLowerText(textWords)
    return textWords

def wordsCounter(dictionary, text):
    row = {}
    row = dict(zip(dictionary, [None] * len(dictionary)))

    for word in dictionary:
        row[word] = text.count(word)

    return row

def createDictionary(texts):
    count = 0
    dictionary = []

    #texts = textsDF.tolist()


    for text in texts:
        texts[count] = preprocessText(text)
        for word in texts[count]:
            if(dictionary.__contains__(word) == False):
                dictionary.append(word)
        count += 1

    return dictionary
def createDataframe(dictionary, texts):
    df = pd.DataFrame(columns=dictionary)

    count = 0
    while(count<len(texts)):
        df = df.append(wordsCounter(dictionary,texts[count]), ignore_index=True)
        count += 1

    return df

def importTexts(intoxPath, alcholicPath, heartPath, traumaPath, breathPath, psycPath, neopPath):
    texts = []

    with open(intoxPath) as f:
        text = f.read()
        texts.append(text)
    f.close()
    with open(alcholicPath) as f:
        text = f.read()
        texts.append(text)
    f.close()
    with open(heartPath) as f:
        text = f.read()
        texts.append(text)
    f.close()
    with open(traumaPath) as f:
        text = f.read()
        texts.append(text)
    f.close()
    with open(breathPath) as f:
        text = f.read()
        texts.append(text)
    f.close()
    with open(psycPath) as f:
        text = f.read()
        texts.append(text)
    f.close()
    with open(neopPath) as f:
        text = f.read()
        texts.append(text)
    f.close()

    return texts

def serializeDictionary(dictionary, dictPath):
    with open(dictPath, 'wb') as dictionaryFile:
        pickle.dump(dictionary, dictionaryFile)
        dictionaryFile.close()
def deserializeDictionary(dictPath):
    dictionary = []
    with open(dictPath, 'rb') as dictionary_file:
        dictionary = pickle.load(dictionary_file)

    return dictionary
def serializeStopSet(stopSet, setPath):
    with open(setPath, 'wb') as stopSetFile:
        pickle.dump(stopSet, stopSetFile)
        stopSetFile.close()
def deserializeStopSet(setPath):
    set = []
    with open(setPath, 'rb') as stopSet_file:
        set = pickle.load(stopSet_file)

    return set

def calculateSimilarity(words):
    ROOT_DIR = os.path.abspath(os.curdir)
    directory = Utils.fixPath(ROOT_DIR)

    texts = importTexts(str(directory) + '/resources/Patologie/Cardiocircolatoria.txt',
                        str(directory) + '/resources/Patologie/Etilista.txt',
                        str(directory) + '/resources/Patologie/Intossicazione.txt',
                        str(directory) + '/resources/Patologie/Neoplastica.txt',
                        str(directory) + '/resources/Patologie/Psichiatrica.txt',
                        str(directory) + '/resources/Patologie/Respiratoria.txt',
                        str(directory) + '/resources/Patologie/Traumatica.txt')


    dictionary = createDictionary(texts)
    dataframe = pd.read_pickle(str(directory) + '/resources/DataframePatologie.dat')

    words = preprocessText(words)
    words = list(wordsCounter(dictionary, words).values())

    max_cossim = 0
    index = -1

    for i in range(len(dataframe.index)):
        # print("Index: ",i," Lenght: ",len(textsDF.iloc[i].tolist()))
        cosine_similarity = 1 - spatial.distance.cosine(dataframe.iloc[i].tolist(), words)
        if (cosine_similarity > max_cossim and (spatial.distance.cosine(dataframe.iloc[i].tolist(), words)) > 0):
            max_cossim = cosine_similarity
            index = i

    return max_cossim, index

def updateTexts():
    ROOT_DIR = os.path.abspath(os.pardir)
    print(ROOT_DIR)
    texts = importTexts(ROOT_DIR + '/resources/Patologie/Cardiocircolatoria.txt',
                        ROOT_DIR + '/resources/Patologie/Etilista.txt',
                        ROOT_DIR + '/resources/Patologie/Intossicazione.txt',
                        ROOT_DIR + '/resources/Patologie/Neoplastica.txt',
                        ROOT_DIR + '/resources/Patologie/Psichiatrica.txt',
                        ROOT_DIR + '/resources/Patologie/Respiratoria.txt',
                        ROOT_DIR + '/resources/Patologie/Traumatica.txt')
    dictionary = createDictionary(texts)
    dataframe = createDataframe(dictionary, texts)
    dataframe.to_pickle(ROOT_DIR + '/resources/DataframePatologie.dat')
    print('Done')




