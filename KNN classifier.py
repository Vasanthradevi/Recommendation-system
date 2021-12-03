import numpy as np
import pandas as pd
import operator
from random import randrange
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings('ignore')

Accuracy = []
def knn_classifier_lda(feature, labels, curr_feature):
    warnings.filterwarnings("ignore")
    file_x = feature
    file_y = labels

    X = pd.read_csv(file_x, low_memory=False,
                    usecols=lambda c: not c.startswith('Unnamed:'))
    Y =  pd.read_csv(file_y, low_memory=False,
                usecols=lambda c: not c.startswith('Unnamed:'))

    # Split the data into training/testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, random_state=42)

    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # linear discriminant analysis
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    lda = LinearDiscriminantAnalysis(n_components=1)
    X_train = lda.fit_transform(X_train, y_train)
    X_test = lda.fit_transform(X_test, y_test)

    # KNN classsifier
    clf = KNeighborsClassifier(n_neighbors=10)
    trained_model = clf.fit(X_train, y_train)
    trained_model.fit(X_train, y_train)

    clf.fit(X_train, y_train)
    y_predict = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_predict)
    print(cm)

    print("Accuracy score of valence test KNN-LDA with"+curr_feature+"is:")
    Accuracy.append(accuracy_score(y_test, y_predict) * 100)
    print(accuracy_score(y_test, y_predict) * 100)


class_arousal = "Trained data/class arousal.csv"
class_valence = "Trained data/class valence.csv"
all_features = ["DFAfeatures", "Hjorith_mobil_valfeatures", "Hurst_valfeatures", "mean_valfeatures", "std_valfeatures", "pfd_valfeatures", "spectralratiofeatures", "spectralentropyfeatures", "DWTdetailfeatures", "DA_meanfeatures", "MSCE_features"]
'''
all_features = ["DA_meanfeatures", "DA_stdfeatures", "DWTdetailfeatures",  "DWTapproxfeatures","DFAfeatures"
           , "Hjorith_complex_valfeatures", "Hjorith_mobil_valfeatures", "Hurst_valfeatures", "mean_valfeatures", "std_valfeatures",
            "MSCE_features", "pfd_valfeatures", "spectralentropyfeatures", "spectralratiofeatures"]
            '''
features = ["DFA", "Hjorth", "Hurst", "Time_Mean", "Time_std", "PFD", "spectral ratio", "spectral entropy", "DWT", "DA", "MSCE"]
# features = ["DA_mean", "DA_std", "DWT_detail", "DWT_approx", "DFA", "Hjorith_complex", "Hjorith_mobility", "Hurst", "Time_Mean", "Time_std", "MSCE", "PFD", "spectral entropy", "spectral ratio"]

for i in all_features:
    feature = "Trained data/"+i+".csv"
    knn_classifier_lda(feature, class_valence, i)

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(features, Accuracy, color='mediumorchid',
        width=0.4)

plt.xlabel("all features")
plt.ylabel("Accuracy")
plt.xticks(rotation = 70)
plt.title("Accuracies for each features in valence")
plt.show()
print(all_features)
print(Accuracy)
Accur = pd.DataFrame(columns=["Features", "Accuracy"])
Accur["Features"] = all_features
Accur["Accuracy"] = Accuracy
print(Accur)
#  "spectralentropyfeatures", "spectralpowerfeatures" "DWTapproxfeatures" , "spectralentropy_features", "spectralratiofeatures"