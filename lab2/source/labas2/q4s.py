from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors,datasets
dataset =datasets.load_iris() #import iris data set
x=dataset.data #loading data and target
y=dataset.target
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=22)#split training and test data
knn=neighbors.KNeighborsClassifier(n_neighbors=50) # define the k mean model
knn.fit(train_x, train_y) # fit the training data
prediction=knn.predict(test_x) # predict on test data
print("The accuracy score :", accuracy_score(prediction, test_y)) # getting the accuracy score