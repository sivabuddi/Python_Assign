from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.decomposition import PCA

# You can add the parameter data_home to wherever to where you want to download your data
dataset = pd.read_csv('Iris.csv')
x = dataset.iloc[:,[1,2,3,4]]
y = dataset.iloc[:,-1]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Fit on training set only.
scaler.fit(x)

# Apply transform to both the training set and the test set.
x_scaler = scaler.transform(x)
pca = PCA(2)
x_pca = pca.fit_transform(x_scaler)
df2 = pd.DataFrame(data=x_pca)
finaldf = pd.concat([df2,dataset[['Species']]],axis=1)
print(finaldf)
