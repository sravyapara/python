from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

# Loading data form Iris
data = load_iris()
# Setting data
x = data.data
# Setting target
y = data.target
# Giving test and train samples
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=12)
# Calling Linear Discriminant method
lindiscamodel=LinearDiscriminantAnalysis()
# Calling Logical Regression method
logregmodel=LogisticRegression()
# Fitting the train data
lindiscamodel.fit(train_x,train_y)
# Predicting the Test data
liprediction=lindiscamodel.predict(test_x)
# Accuracy for linear regression
print("Accuracy for linear regression is ", accuracy_score(liprediction, test_y))
# Fitting logical regression model
logregmodel.fit(train_x, train_y)
# Prediction logical regression model
loprediction=logregmodel.predict(test_x)
# Logistic regression accuracy

print("Accuracy for logistic regression is ", accuracy_score(loprediction, test_y))