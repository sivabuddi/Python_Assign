import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.model_selection import train_test_split
import time
from sklearn import metrics

data = pd.read_csv("glass.csv")
X_train, X_test = train_test_split(data, test_size=0.4, random_state=int(time.time()))

used_features = [
    "RI", "Na", "Mg", "Al", "Si", "K", "Ca", "Ba", "Fe"
]
svc = SVC(kernel='linear')
svc.fit(X_train[used_features].values,X_train["Type"])

Y_pred = svc.predict(X_test[used_features])

acc_svc = round(svc.score(X_test[used_features].values, X_test["Type"]) * 100, 2)
print("svm accuracy is:", acc_svc)

'''
svc1 = SVC(kernel='rbf')
svc1.fit(
    X_train[used_features].values,
    X_train["Type"]
)

Y_pred = svc1.predict(X_test[used_features])


acc_svc = round(svc1.score(X_test[used_features].values, X_test["Type"]) * 100, 2)
print("svm accuracy is:", acc_svc)
print("\n")
print(metrics.classification_report(X_test["Type"], Y_pred))
'''