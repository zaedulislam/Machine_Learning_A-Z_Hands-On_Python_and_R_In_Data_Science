# Hierarchical Clustering

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
filepath = 'E:\\WORKSTATION\\Machine Learning Training\\Machine Learning A-Z™ Hands-On Python and R In Data Science\\Part 4 - Clustering\\Section 25 - Hierarchical Clustering\\Dataset\\Mall Customers.csv'
dataset = pd.read_csv(filepath)
X = dataset.iloc[:,[3, 4]].values

# Using the dendogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram = sch.dendrogram(sch.linkage(X, method = 'ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean Distances')
plt.show()

# Fitting Hierarchical Clustering to the Mall Customers
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

# Visualize the clusters
# Visualizing the clusters
# Cluster are numbered from 0 to 4
# X[y_kmeans == 0, 0] - Plotting the x coordinates of all the observation points that belong to cluster 1
# y_kmeans == 0 - Taking the cluster 1, 0 - Specifying the first column of dataset X
# X[y_kmeans == 0, 1] - Plotting the y coordinates of all the observation points that belong to cluster 1
# s - Size of a observation
# c - Set the cluster color   
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s = 100, c = 'red', label = 'Careful')
# Follow same thing for other 4 clusters
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s = 100, c = 'blue', label = 'Standard')
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s = 100, c = 'green', label = 'Target')
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s = 100, c = 'cyan', label = 'Careless')
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s = 100, c = 'magenta', label = 'Sensible')

# Caveat - For clustering in more than two dimensions, the below code block will not work properly 
plt.title('Clusters of clients') 
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()