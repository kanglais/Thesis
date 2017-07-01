from sklearn import preprocessing
from sklearn import cluster
import numpy as np
from matplotlib.pyplot import plot
import os
import json
import pickle

S_DIR = '/Users/Kellie/Desktop/'
D_DIR = '/Users/Kellie/Desktop/'

with open(os.path.join(S_DIR, 'hash_mention.json'), 'rb') as rf:

    hash_mention = json.load(rf)

full_list = []

for user in hash_mention:

    full_list.extend(hash_mention[user])

vocabulary = list(set(full_list))

tf_matrix = np.zeros((len(hash_mention), len(vocabulary)))
##tf_matrix = tf_matrix.astype(np.float32)

users = hash_mention.keys()

inv_index = {}

for i, handle in enumerate(vocabulary):

    inv_index[handle] = i

for i, user in enumerate(users):

    for handle in hash_mention[user]:

        tf_matrix[i, inv_index[handle]] += 1

    #if i % 1000 == 0:

        #print('Processed users so far: ' + str(i))

tf_matrix = tf_matrix.astype(np.float32)

#np.save(os.path.join(D_DIR, 'hashtag_mention_tf_matrix.npy'), tf_matrix)

#with open(os.path.join(D_DIR, 'users_vocabulary.pkl'), 'wb') as wf:

    #pickle.dump([users, vocabulary], wf)

matrix = np.array(tf_matrix)

print(matrix)
print(np.sum(matrix[10]))

"""
matrix = np.array(tf_matrix)

preprocessing.normalize(matrix)

k = 2
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(matrix)

labels = kmeans.labels_
centroids = kmeans.cluster_centers_


for i in range(k):
    # select only data observations with cluster label == i
    ds = matrix[np.where(labels==i)]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
pyplot.show()

---------
"""