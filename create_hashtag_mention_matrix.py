import pprint
import json
import numpy as np
from sklearn import preprocessing
from sklearn import cluster
import numpy as np
from matplotlib import pyplot
import os
import pandas as pd

#split into smaller ones and dump into pickles

def create_initial_data_structure(input_data_file):
    # load tweet data as an object
    with open(input_data_file, 'rb') as raw_tweet_data:

        # generate python dict from raw json data
        all_users_terms_dict = json.load(raw_tweet_data)

        # create list that hold two lits, one is all terms and the other list is all users
        users_list_and_terms_list = generate_complete_terms_list_and_users_list(all_users_terms_dict)

        # get list that holds every mention of every term
        every_mention_every_term_list = users_list_and_terms_list[0]

        # list that each individual user id
        unique_user_id_list = users_list_and_terms_list[1]

        # create a set to hold each term ** only once **
        unique_term_set = create_set(every_mention_every_term_list)

        unique_terms_list = unique_term_list(unique_term_set)
        
        #create a dict to hold 0's or 1's based on which terms the user used
        #save this one, then run everything on it?
        associated_value_return_list = associate_terms_with_user(unique_term_set, all_users_terms_dict)

        #transform the above dict into a matrix
        matrix_of_associated_values = matrix_creation(associated_value_return_list)

        #normalize matrix
        normalized_matrix = normalize_associated_term_values(matrix_of_associated_values)

        to_file = write_to_file(normalized_matrix)

    return normalized_matrix

def write_to_file(normalized_matrix):

    with open('/var/scratch/kenglish/hash_mention_matrix.json', 'w') as f:
        for line in normalized_matrix:
            jsonify_matrix = pd.Series(line).to_json(orient='values')

            json.dump(jsonify_matrix, f)

def normalize_associated_term_values(matrix_of_associated_values):

    matrix_as_float = matrix_of_associated_values.astype(float)

    normalized_matrix = preprocessing.normalize(matrix_as_float)

    return normalized_matrix   

def matrix_creation(associated_value_return_list):

    matrix_of_associated_values = []

    for user in associated_value_return_list:
        matrix_of_associated_values.append(user)

    matrix_of_associated_values = np.array(matrix_of_associated_values)

    #matrix_of_associated_values = np.reshape(matrix_of_associated_values, (7, 52))

    return matrix_of_associated_values


def associate_terms_with_user(unique_term_set, all_users_terms_dict):

    associated_value_return_list = []

    count = 0

    for user_id in all_users_terms_dict:

        #to create array of zeros:
        this_user_zero_vector = list(np.zeros(len(unique_term_set)))
        
        # what terms *did* this user use
        terms_belong_to_this_user = all_users_terms_dict.get(user_id)
                    
        for global_index, unique_term in enumerate(unique_term_set):
            this_user_zero_vector[global_index] = terms_belong_to_this_user.count(unique_term)
            
        associated_value_return_list.append(this_user_zero_vector)

        count +=1
        
        if count%10000==0:
            break
            #print(count)

    return associated_value_return_list


def generate_complete_terms_list_and_users_list(all_users_terms_dict):

    complete_terms_list = []

    complete_users_list = []

    for key, value in all_users_terms_dict.items():
        complete_terms_list.extend(value)
        if key not in complete_users_list:
            complete_users_list.append(key)

    return([complete_terms_list, complete_users_list])

def unique_term_list(unique_term_set):
    unique_terms_list = []

    for term in unique_term_set:
        unique_terms_list.append(term)
        
    #print(len(unique_terms_list))
    return(unique_terms_list)

def create_set(complete_terms_list):

    term_set = set(complete_terms_list)
    #print(len(term_set))

    return term_set


def main():

    # define input data file
    input_data_file = '/var/scratch/kenglish/january_hash_mention.json'
    
    # generate data structure
    create_initial_data_structure(input_data_file)

if __name__ == "__main__":
    main()
    




