from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

def cluster_images(container):
    
    positive = np.asarray([element[1] for element in container])
    negative = np.asarray([element[2] for element in container])
    ratings = np.asarray([element[3] for element in container])
    combined = np.asarray([[element[1],element[2]] for element in container])
        
    y_pred = KMeans(n_clusters=2, random_state=0).fit_predict(combined)

    plt.figure(figsize=(12, 12))
    
    plt.scatter(positive, ratings, c=y_pred)
    plt.title("positive vs ratings  ")
    plt.savefig('positive_ratings.pdf')
    plt.clf()
    