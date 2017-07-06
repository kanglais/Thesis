import hashtag_clustering
from sklearn.preprocessing import StandardScaler
import numpy as np


def create_matrix_with_pca(normalized_matrix):

	X_std = create_standardized_matrix(normalized_matrix)

	covariance_matrix = create_covariance_matrix(normalized_matrix, X_std)

	eigendecomposition_on_covariance_matrix(covariance_matrix, X_std)

def eigendecomposition_on_covariance_matrix(covariance_matrix, X_std):

	covariance_matrix = np.cov(X_std.T)

	eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)

	print(eig_vecs)
	print('\nEigenvalues \n%s' %eig_vals)

def create_covariance_matrix(normalized_matrix, X_std):

	mean_vector = np.mean(normalized_matrix, axis=0)
	covariance_matrix = (X_std - mean_vector).T.dot((X_std - mean_vector)) / (X_std.shape[0]-1)
	return covariance_matrix


def create_standardized_matrix(normalized_matrix):

	X_std = StandardScaler().fit_transform(normalized_matrix)

	return X_std

def main():

    # define input data file
	input_data_file = './data/toy_data.json'
    
    # access hashtag_clustering file, data from file to use in this script
	create_matrix_with_pca( hashtag_clustering.create_initial_data_structure(input_data_file) )

if __name__ == "__main__":
    main()