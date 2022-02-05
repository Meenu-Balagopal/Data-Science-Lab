'''To Implement Naive Bayes Algorithm'''

from sklearn.datasets import load_iris
x,y=load_iris(return_X_y=True)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.5,random_state=0)

# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(x_train,y_train)
# Predicting the Test set results
y_pred=gnb.predict(x_test)
print("-----------------------------------------------------------------------------------")
print("Prediction(Test set)\n\n",y_pred)

from sklearn import metrics
print("-----------------------------------------------------------------------------------")
print("Accuracy\n")
print(metrics.accuracy_score(y_test,y_pred))

# Predicting the sample results
sample=[[5,5,4,5]]
pred=gnb.fit(x_train,y_train).predict(sample)
print("-----------------------------------------------------------------------------------")
print("Prediction(sample)\n\n",pred)

pred_val=[load_iris().target_names[p] for p in pred]
print("-----------------------------------------------------------------------------------")
print("Predicted Values\n")
print(pred_val)
print("-----------------------------------------------------------------------------------")
