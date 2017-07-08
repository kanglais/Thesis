import create_hashtag_mention_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import decomposition
from sklearn.cluster import KMeans
import numpy as np
import pylab as pl


def cluster_with_kmeans(x):

    kmeans = KMeans(n_clusters=2, random_state=0)
    kmeans.fit(X)

    pl.scatter(X[:, 0], X[:, 1], c=kmeans.labels_)
    pl.show()

def create_matrix_with_pca(normalized_matrix):

    X_std = create_standardized_matrix(normalized_matrix)
    
    pca = decomposition.PCA(n_components=10)
    pca.fit(X_std.data)
    PCA(copy=True, n_components=10, whiten=False)
    X = pca.transform(X_std.data)
    
    return X

def create_standardized_matrix(normalized_matrix):

	X_std = StandardScaler().fit_transform(normalized_matrix)

	return X_std

def main():

    # define input data file
	input_data_file = './data/hash_mention.json'
    
    # access hashtag_clustering file, data from file to use in this script
	create_matrix_with_pca_and_kmeans( create_hashtag_mention_matrix.create_initial_data_structure(input_data_file) )

if __name__ == "__main__":
    main()