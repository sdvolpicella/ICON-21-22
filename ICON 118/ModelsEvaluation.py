from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import make_scorer
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.model_selection import cross_validate

from sklearn import model_selection
import os
import pandas as pd
import Utils

ROOT_DIR = os.path.abspath(os.pardir)
directory = Utils.fixPath(ROOT_DIR)
dataset = pd.read_csv(directory + '/resources/datasetICON.csv', sep=',', header=None)

X = dataset.values[:, 0:7]
y = dataset.values[:, 7]


Kfold = model_selection.KFold(n_splits=8, random_state=None)

bag_model = BaggingClassifier(n_estimators=10)
knn_model = KNeighborsClassifier(metric='manhattan', n_neighbors=5)
svc_model = SVC(C=1, gamma='auto', kernel='rbf', probability=True)
rand_model = RandomForestClassifier(max_features='sqrt', n_estimators=10)

scoring = {'accuracy': make_scorer(accuracy_score),
           'precision': make_scorer(precision_score, average='macro', zero_division=0),
           'recall': make_scorer(recall_score, average='macro', zero_division=0)}

#  cross-validation su ogni classifier
bag = cross_validate(bag_model, X, y, cv=Kfold, scoring=scoring)
svc = cross_validate(svc_model, X, y, cv=Kfold, scoring=scoring)
knn = cross_validate(knn_model, X, y, cv=Kfold, scoring=scoring)
rfc = cross_validate(rand_model, X, y, cv=Kfold, scoring=scoring)

# crea un dataframe con i valori delle metriche
models_scores_table = pd.DataFrame({'Bagging Classifier': [bag['test_accuracy'].mean(),
                                                           bag['test_precision'].mean(),
                                                           bag['test_recall'].mean()],

                                    'SVC': [svc['test_accuracy'].mean(),
                                            svc['test_precision'].mean(),
                                            svc['test_recall'].mean()],

                                    'Random Forest': [rfc['test_accuracy'].mean(),
                                                      rfc['test_precision'].mean(),
                                                      rfc['test_recall'].mean()],

                                    'KNearestNeighbor': [knn['test_accuracy'].mean(),
                                                         knn['test_precision'].mean(),
                                                         knn['test_recall'].mean()]},

                                   index=['Accuracy', 'Precision', 'Recall'])

acc = [round(bag['test_accuracy'].mean(), 2), round(svc['test_accuracy'].mean(), 2),
       round(rfc['test_accuracy'].mean(), 2), round(knn['test_accuracy'].mean(), 2)]
prec = [round(bag['test_precision'].mean(), 2), round(svc['test_precision'].mean(), 2),
        round(rfc['test_precision'].mean(), 2), round(knn['test_precision'].mean(), 2)]
rec = [round(bag['test_recall'].mean(), 2), round(svc['test_recall'].mean(), 2),
       round(rfc['test_recall'].mean(), 2), round(knn['test_recall'].mean(), 2)]

# Add 'Best Score' column
models_scores_table['Best Score'] = models_scores_table.idxmax(axis=1)
# tabella dei risultati
print('Random Forest:\n-----------------------------\n', models_scores_table['Random Forest'])
print('=======================================')
print('Bagging Classifier:\n------------------------------\n', models_scores_table['Bagging Classifier'])
print('=======================================')
print('SVC:\n-----------------------------\n', models_scores_table['SVC'])
print('=======================================')
print('KNearestNeighbor:\n-----------------------------\n', models_scores_table['KNearestNeighbor'])
print('=======================================')