import hashtag_clustering
from sklearn.preprocessing import StandardScaler
import numpy as np

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls

from sklearn.decomposition import PCA


def create_matrix_with_pca(normalized_matrix):

	X_std = create_standardized_matrix(normalized_matrix)

	pca = PCA(n_components=2)
	pca.fit(X_std)
	PCA(copy=True, iterated_power='auto', n_components=2, random_state=None,
	  svd_solver='auto', tol=0.0, whiten=False)
	print(pca.explained_variance_ratio_) 

# 	covariance_matrix = create_covariance_matrix(normalized_matrix, X_std)

# 	eigdecomposition_covariance = eigendecomposition_on_covariance_matrix(covariance_matrix, X_std)

# 	eigdecomposition_correlation = eigendecomposition_on_correlation_matrix(X_std)

# 	singular_vector_decomposition = create_singular_vector_decomposition(X_std)

# 	print(eigdecomposition_correlation)

# def create_singular_vector_decomposition(X_std):

# 	u,s,v = np.linalg.svd(X_std.T)
# 	# # print(u)
# 	# # print(s)
# 	# print(v)

# 	return u, s, v

# def eigendecomposition_on_correlation_matrix(X_std):

# 	cor_mat1 = np.corrcoef(X_std.T)

# 	eig_vals, eig_vecs = np.linalg.eig(cor_mat1)

# 	#return eig_vals, eig_vecs


# 	#creates error Arrays are not almost equal to 6 decimals
# 	# for ev in eig_vecs:
# 	#     np.testing.assert_array_almost_equal(1.0, np.linalg.norm(ev))
# 	# print('Everything ok!')

# 	# Make a list of (eigenvalue, eigenvector) tuples
# 	eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# 	# Sort the (eigenvalue, eigenvector) tuples from high to low
# 	eig_pairs.sort()
# 	eig_pairs.reverse()

# 	# Visually confirm that the list is correctly sorted by decreasing eigenvalues
# 	# print('Eigenvalues in descending order:')
# 	# for i in eig_pairs:
# 	#     print(i[0])

# def eigendecomposition_on_covariance_matrix(covariance_matrix, X_std):

# 	covariance_matrix = np.cov(X_std.T)

# 	eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)

# 	return eig_vals, eig_vecs

# def create_covariance_matrix(normalized_matrix, X_std):

# 	mean_vector = np.mean(normalized_matrix, axis=0)
# 	covariance_matrix = (X_std - mean_vector).T.dot((X_std - mean_vector)) / (X_std.shape[0]-1)
# 	return covariance_matrix


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