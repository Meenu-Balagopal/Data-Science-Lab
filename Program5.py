from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
iris=load_iris()
x=iris.data
y=iris.target
print("Extracting feature names")
print(iris.feature_names)
print("extracting target names")
print(iris.target_names)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
print("no of columns of train data")
print(x_train.shape)
print("no of columns of test data")
print(x_test.shape)
y_pred=c_knn.predict(x_test)
print("predicted output of test data")
print(y_pred)
print("accuracy score")
print(metrics.accuracy_score(y_test,y_pred))
sample=[[5,2,3,4]]
pred=c_knn.predict(sample)
pred_v=[iris.target_names[p] for p in pred]
print("predicted values")
print(pred_v)
