import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
import csv

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)



#Exploratory variables (independent variables)
#Response / target variables (dependent variables)


# Calculating Outliers
data = pd.read_csv('train.csv')
X = data["GarageArea"]
print("No.of. observations", len(X),"\n")
print("Dimension of the data ", data.shape,"\n")
outliers=[]

def detect_outlier(data_1):
    threshold = 3
    mean_1 = np.mean(data_1)
    std_1 = np.std(data_1)

    for y in data_1:
        z_score = (y - mean_1) / std_1
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers


outlier_datapoints = detect_outlier(X)
print("Outlier Data Points= ",outlier_datapoints, "\n")
#print(sorted(X))
X1=sorted(X)
print("Sorted values \n",X1)
q1, q3= np.percentile(X1,[25,75])
print(q1)
print(q3)
iqr=q3-q1 #inter quartile deviation
print(iqr)

lower_bound = q1 - (1.5 * q1)
upper_bound = q3 + (1.5 * q3)



print("Lower Boundary=\n",lower_bound)
print("Upper Boundary=\n",upper_bound)

#print(X)

print("Outlier Data Points= ",outlier_datapoints, "\n")
total_data=sorted(X)
print(total_data)

data = pd.read_csv('train.csv')
XData = data["GarageArea"]
YData = data["SalePrice"]
plt.scatter(XData, YData)
plt.title('Outlier Demo')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()

desired_length = len(total_data) - 7
total_data=total_data[0:desired_length]
print(total_data)
data = pd.read_csv('train.csv')
XData = data["GarageArea"]
YData = data["SalePrice"]
plt.scatter(XData, YData)
plt.title('Outlier Demo')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()



'''

total_data=total_data[:1453]
print(total_data)


# Scatter plot between GaurageArea  and SalePrice
print("value of X=",X,"\n")
data = pd.read_csv('train.csv')
XData = data["GarageArea"]
YData = data["SalePrice"]
plt.scatter(XData, YData)
plt.title('Outlier Demo')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()




#print(X)
#print("data type of X is =",type(X))
#print(len(X))
#X.rename(index = {"Id": "Id", "GarageArea":"GarageArea"}, inplace = True)



#train = pd.read_csv('train.csv')
#train.SalePrice.describe()
#print(train.SalePrice.describe())
#Next, we'll check for skewness
#print ("Skew is:", train.SalePrice.skew()) # print the value of skewness ; positive represents
#plt.hist(train.SalePrice, color='blue') # draw the histogram
#plt.show()
 
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
'''