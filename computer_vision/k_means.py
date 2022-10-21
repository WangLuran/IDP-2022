import numpy as np

def distEclud(x,y):
    return np.sqrt(np.sum((x-y)**2, axis = 1))
 
def randCent(dataSet,k):
    m,n = dataSet.shape
    centroids = np.zeros((k,n))
    indexes = np.random.randint(0, m, k)
    centroids = dataSet[indexes, :]
    return centroids
 
def kmeans_open(dataSet,k):
 
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,1)))
    clusterChange = True
 
    centroids = randCent(dataSet,k)
    print(centroids)
    while clusterChange:
        clusterChange = False
 
        for i in range(m):
            distance = distEclud(centroids,dataSet[i,:])
            minIndex = np.argmin(distance)
            clusterChange = clusterAssment[i,0] != minIndex
            clusterAssment[i,0] = minIndex

            
        for j in range(k):
            pointsInCluster = dataSet[np.nonzero(clusterAssment[:,0].A == j)[0]]  
            centroids[j,:] = np.mean(pointsInCluster,axis=0)
    print(centroids)
 
    return centroids
