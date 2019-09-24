import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('train.csv')
train.SalePrice.describe()
#print(train.SalePrice.describe())
#Next, we'll check for skewness
print ("Skew is:", train.SalePrice.skew()) # print the value of skewness ; positive represents
plt.hist(train.SalePrice, color='blue') # draw the histogram
plt.show()


target = np.log(train.SalePrice) # increase the linearity of the data
print ("Skew is:", target.skew())
plt.hist(target, color='blue')
plt.show()


#Working with Numeric Features
numeric_features = train.select_dtypes(include=[np.number])
print("Numerical Features", "\n", numeric_features)
corr = numeric_features.corr()
print("Correlation values \n",corr)


print (corr['SalePrice'].sort_values(ascending=False)[:5], '\n')
print (corr['SalePrice'].sort_values(ascending=False)[-5:])

quality_pivot = train.pivot_table(index='OverallQual', values='SalePrice', aggfunc=np.median)
print(quality_pivot)




#Notice that the median sales price strictly increases as Overall Quality increases.
quality_pivot.plot(kind='bar', color='blue') # Relationship between overallQual and SalePrice
plt.xlabel('Overall Quality')
plt.ylabel('Median Sale Price')
plt.xticks(rotation=0)
plt.show()


##Null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)




##handling missing value
data = train.select_dtypes(include=[np.number]).interpolate().dropna()
print("handling missing values \n", sum(data.isnull().sum() != 0))



##Build a linear model
y = np.log(train.SalePrice)  #Increase the linearity of the data if it is skewed
X = data.drop(['SalePrice', 'Id'], axis=1) # drop SalePrice and Id data into X using drop method
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.33)
from sklearn import linear_model
lr = linear_model.LinearRegression()
model = lr.fit(X_train, y_train)
print(model)


##Evaluate the performance and visualize results
print ("R^2 is: \n", model.score(X_test, y_test))
predictions = model.predict(X_test)
from sklearn.metrics import mean_squared_error
print ('RMSE is: \n', mean_squared_error(y_test, predictions))



##visualize
actual_values = y_test
plt.scatter(predictions, actual_values, alpha=.75, color='b') #alpha helps to show overlapping data
plt.xlabel('Predicted Price')
plt.ylabel('Actual Price')
plt.title('Linear Regression Model')
plt.show()
