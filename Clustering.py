import numpy as np
from sklearn import cluster
from sklearn import metrics
from numpy import nan





def Clusters(data):

    for k in range(2,10):
        kmeans = cluster.KMeans(n_clusters = k)
        kmeans.fit(data)

        labels = kmeans.labels_
        print k,':',  metrics.silhouette_score(data, labels, sample_size=3000, metric='euclidean')

