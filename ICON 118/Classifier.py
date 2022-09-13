import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier
from sklearn import metrics
from sklearn.model_selection import cross_val_score


def importDataset(datasetPath):
    importedDtaset = pd.read_csv(datasetPath, sep=',', header=None)
    return importedDtaset

# genero il train set dal dataset importato
def generateSets(importedDtaset, test):
    X = importedDtaset.values[:, 0:7]
    Y = importedDtaset.values[:, 7]
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.0001, random_state=44)

    X_test = test

    return X, Y, X_train, X_test, y_train, y_test

# addestro il classificatore usando come parametro di split l'entropia
def createAndFit(X_train, y_train):
    clf = BaggingClassifier(n_estimators=10)
    clf.fit(X_train, y_train)
    return clf

# effettuo la predizione della feature target
def classPrediction(X_test, classifier):
    y_pred = classifier.predict(X_test)
    return y_pred

# richiamo la pipeline del classificatore
def classify(test, datasetPath):
    dataset = importDataset(datasetPath)
    X, Y, X_train, X_test, y_train, y_test = generateSets(dataset, test)
    clf_entropy = createAndFit(X_train, y_train)
    y_pred = classPrediction(X_test, clf_entropy)
    return y_pred