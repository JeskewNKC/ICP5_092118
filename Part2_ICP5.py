import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


X = np.array([[1.0, 1.0],
              [1.5, 2.0],
              [3.0, 4.0],
              [5.0, 7.0],
              [3.5, 5.0],
              [4.5, 5.0]])

kmeans = KMeans(max_iter=100, n_clusters=2, random_state=0)
kmeans.fit(X)

centers = kmeans.cluster_centers_
labels = kmeans.labels_
print(centers)
colors = ["g.","r.","c.","y."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centers[:, 0],centers[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
plt.show()
