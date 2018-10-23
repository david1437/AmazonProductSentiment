from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def cluster_images(container):
    
    positive = np.asarray([element[1] for element in container])
    negative = np.asarray([element[2] for element in container])
    combined = np.asarray([[element[1],element[2]] for element in container])
        
    y_pred = KMeans(n_clusters=3, random_state=0).fit_predict(positive)

    plt.figure(figsize=(12, 12))
    
    plt.scatter(positive[:, 0], positive[:, 1], c=y_pred)
    plt.title("Positive Clusters ")
    plt.savefig('positive.pdf')
    plt.clf()
    
    
    y_pred = KMeans(n_clusters=3, random_state=0).fit_predict(negative)

    plt.figure(figsize=(12, 12))
    
    plt.scatter(negative[:, 0], negative[:, 1], c=y_pred)
    plt.title("Negative Clusters ")
    plt.savefig('negative.pdf')
    plt.clf()
    
    y_pred = KMeans(n_clusters=3, random_state=0).fit_predict(combined)

    plt.figure(figsize=(12, 12))
    
    plt.scatter(combined[:, 0], combined[:, 1], c=y_pred)
    plt.title("Combined Clusters ")
    plt.savefig('combined.pdf')
    plt.clf()
    