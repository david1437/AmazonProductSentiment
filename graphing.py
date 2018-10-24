from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def graphs(container, name):
    
    positive = np.asarray([element[1] for element in container])
    negative = np.asarray([element[2] for element in container])
    ratings = np.asarray([element[3] for element in container])

    plt.figure(figsize=(12, 12))
    
    plt.scatter(positive, ratings)
    plt.title("positive vs ratings  ")
    plt.savefig(name + '_positive_ratings.pdf')
    plt.clf()
        
    plt.scatter(negative, ratings)
    plt.title("negative vs ratings  ")
    plt.savefig(name + '_negative_ratings.pdf')
    plt.clf()