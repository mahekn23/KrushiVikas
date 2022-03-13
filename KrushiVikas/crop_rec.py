from __future__ import print_function
import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import warnings

warnings.filterwarnings("ignore")


def crop_pred(N, P, K, temp, humidity, ph, rain):
    df = pd.read_csv("Crop_recommendation.csv")
    # df['label'].unique()
    features = df[["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]]
    target = df["label"]
    # features = df[['temperature', 'humidity', 'ph', 'rainfall']]
    labels = df["label"]
    # Initialzing empty lists to append all model's name and corresponding name
    acc = []
    model = []
    Xtrain, Xtest, Ytrain, Ytest = train_test_split(
        features, target, test_size=0.2, random_state=2
    )

    RF = RandomForestClassifier(n_estimators=20, random_state=0)
    RF.fit(Xtrain, Ytrain)

    predicted_values = RF.predict(Xtest)
    data = np.array([[N, P, K, temp, humidity, ph, rain]])
    prediction = RF.predict(data)
    # print(prediction)
    x = metrics.accuracy_score(Ytest, predicted_values)
    acc.append(x)
    model.append("RF")
    print("The crop is predicted with an accuracy of: ", round(x * 100, 2))
    print(prediction)
    # print(classification_report(Ytest,predicted_values))
    return prediction


N = float(sys.argv[1])
P = float(sys.argv[2])
K = float(sys.argv[3])
temp = float(sys.argv[4])
humidity = float(sys.argv[5])
ph = float(sys.argv[6])
rain = float(sys.argv[7])

data = crop_pred(N, P, K, temp, humidity, ph, rain)
# print(data)
