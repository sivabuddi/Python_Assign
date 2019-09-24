import pandas as pd
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics


train_df = pd.read_csv('./train_preprocessed.csv')
#print(train_df)
test_df = pd.read_csv('./test_preprocessed.csv')
#print(test_df)
X_train = train_df.drop("Survived", axis=1)
X_train = X_train.drop("Sex", axis=1)
Y_train = train_df["Survived"]
X_test = test_df.drop("PassengerId", axis=1).copy()
X_test = X_test.drop("Sex", axis=1)
print(train_df[train_df.isnull().any(axis=1)])


##KNN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
# print(confusion_matrix(X_test, Y_pred))

#print(classification_report(y_test, y_pred))


Y_prob = knn.predict_proba(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print("KNN accuracy is:", acc_knn)




print("what is the correlation of sex in the survival calculations.")
print(train_df[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Sex', ascending=False))
