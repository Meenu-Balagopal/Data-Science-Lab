from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

iris=load_iris()
x=iris.data[:,:2]
y=iris.target
km=KMeans(n_clusters=3)
km.fit(x,y)
print(km.cluster_centers_)
print(km.labels_)
fig,axes=plt.subplots(1,2,figsize=(17,20))
axes[0].scatter(x[:,0],x[:,1],c=y,s=40)
axes[1].scatter(x[:,0],x[:,1],c=km.labels_,s=40)
axes[0].set_xlabel("Sepal Length")
axes[0].set_ylabel("Sepal width")
axes[1].set_xlabel("Sepal length")
axes[1].set_ylabel("Sepal Width")
axes[0].set_title("Before")
axes[1].set_title("After")
