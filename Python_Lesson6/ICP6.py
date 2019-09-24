import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")

dataset = pd.read_csv('CC.csv')
print("Original Data size=",dataset.shape)
x = dataset.iloc[:,1:17]
y = dataset.iloc[:,-1]
print(x.shape, y.shape)

# see how many samples we have of each Tenure
print(dataset["TENURE"].value_counts())




sns.FacetGrid(dataset, hue="TENURE", size=7).map(plt.scatter, "TENURE", "CASH_ADVANCE").add_legend()
#do same for petals
#sns.FacetGrid(dataset, hue="TENURE", size=7).map(plt.scatter, "PetalLengthCm", "PetalWidthCm").add_legend()
plt.show()


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

##handling missing value
data = x.select_dtypes(include=[np.number]).interpolate().dropna()
print(sum(data.isnull().sum() != 0))


from sklearn.cluster import KMeans
nclusters = 7 # this is the k in kmeans
km = KMeans(n_clusters=nclusters)
km.fit(data)

# predict the cluster for each data point
y_cluster_kmeans = km.predict(data)
from sklearn import metrics
score = metrics.silhouette_score(data, y_cluster_kmeans)
print(score)


##elbow method to know the number of clusters

from sklearn.cluster import KMeans
wcss = []

for i in range(1,17):
    kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=17,random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,17),wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('CASH_ADVANCE')
plt.show()


# Applying PCA for same data set
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
##handling missing value
data = x.select_dtypes(include=[np.number]).interpolate().dropna()
print("null values sum = ",sum(data.isnull().sum() != 0))
scaler.fit(data)

# Apply transform to both the training set and the test set.
x_scaler = scaler.transform(data)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,dataset[['TENURE']]],axis=1)
print(finaldf)
