from sklearn.datasets import fetch_20newsgroups

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)

tfidf_Vect = TfidfVectorizer()

X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train_tfidf, twenty_train.target)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

predicted = clf.predict(X_test_tfidf)

print("Score without bigram")
print(metrics.accuracy_score(twenty_test.target, predicted))
