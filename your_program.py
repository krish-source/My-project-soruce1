import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn


dataset = pd.read_csv('Mall_customers.csv')
data = dataset.iloc[:,[3,4]].values
data.shape

a = plt.scatter(data[:,0], data[:,1], s = 10, c = 'black')


# Elbow meathod for det clusters

from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++',max_iter = 300, n_init = 10)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')


