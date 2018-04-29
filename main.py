import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB


# import server
# remember to use two mocdels....


def main():
    model_1 = DecisionTreeClassifier()
    datax = data_operations('data_med.csv')

    symptoms = datax.Symptoms
    diseases = datax.Disease

    new_symptoms = []
    for x in symptoms:
        new_symptoms.append(x)

    new_diseases = []
    for y in diseases:
        new_diseases.append(y)
    '''
    print(symptoms)
    print(new_symptoms)

    # just trying
    print(symptoms.shape)
    print(diseases.shape)
    '''

    new_diseases = new_diseases
    new_symptoms = new_diseases

    features = [new_symptoms[:5], new_symptoms[5:10], new_symptoms[10:15], new_symptoms[15:20]]
    labels = [new_diseases[5], new_diseases[10], new_diseases[15], new_diseases[20]]
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3)

    xz = 0
    while xz < 5:
        model_1 = model_1.fit(features, labels)
        print("fitting ", str(xz))
        xz += 1

    diag = model_1.predict(
        [[datax.Symptoms[16], datax.Symptoms[18], datax.Symptoms[19], datax.Symptoms[19], datax.Symptoms[16]]])
    stuff = model_1.predict(features_test)

    print("##########")
    print(datax.Symptoms[2])
    print(datax.Disease[2])
    print("##########")

    print('with an accuracy of', accuracy_score(labels_test, stuff))
    return str(diag)


def data_operations(location):
    data = pd.read_csv(location, sep='\t')
    data.Symptoms = pd.Categorical(data.Symptoms)
    data.Symptoms = data.Symptoms.cat.codes

    data.Disease = pd.Categorical(data.Disease)
    data.Disease = data.Disease.cat.codes

    print('\n')
    print('returning data')
    return data


if __name__ == "__main__":
    print(main())
