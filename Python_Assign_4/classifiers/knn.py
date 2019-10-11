import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

train_df = pd.read_csv('./train_preprocessed.csv')
test_df = pd.read_csv('./test_preprocessed.csv')
print(train_df.shape)
print("check null values",train_df[train_df.isnull().any(axis=1)])
X_train = train_df.drop("Survived", axis=1)
print("Training Data=",X_train)
X_train = X_train.drop("Sex", axis=1)
print("Survived  and Sex Variable in Training Data = ",X_train)
Y_train = train_df["Survived"]
print(Y_train)
X_test = test_df.drop("PassengerId", axis=1)
print("Copy=",X_test)
X_test = X_test.drop("Sex", axis=1)
#check null values
print("check null values",train_df[train_df.isnull().any(axis=1)])

##KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
Y_prob = knn.predict_proba(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print("KNN accuracy is:", acc_knn)
