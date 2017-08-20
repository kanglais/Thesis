import break_tweet_into_dicts
import pprint
import json
import numpy as np
from sklearn import preprocessing
from sklearn import cluster
from matplotlib import pyplot
import os
import pandas as pd

def create_initial_data_structure(input_data_file):
    # generate python dict from raw json data in break_tweet file
    all_users_terms_dict = break_tweet_into_dicts.all_users_terms_dict

    # list that each individual user id
    unique_user_id_list = break_tweet_into_dicts.user_id_list

    # set of terms from break_tweet file
    unique_term_set = input_data_file

    # unique_terms_list = unique_term_list(unique_term_set)
    
    #create a dict to hold 0's or 1's based on which terms the user used
    associated_value_return_list = associate_terms_with_user(unique_term_set, all_users_terms_dict)

    #transform the above dict into a matrix
    matrix_of_associated_values = matrix_creation(associated_value_return_list)

    #normalize matrix
    normalized_matrix = normalize_associated_term_values(matrix_of_associated_values)

    # to_file = write_to_file(normalized_matrix)

    return normalized_matrix

# def write_to_file(normalized_matrix):

#     with open('/var/scratch/kenglish/hash_mention_matrix.json', 'w') as f:
#         for line in normalized_matrix:
#             jsonify_matrix = pd.Series(line).to_json(orient='values')

#             json.dump(jsonify_matrix, f)

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
            #
            break
            print(count)

    return associated_value_return_list

def main():
    
    input_data_file = break_tweet_into_dicts.hash_mention_list


    # generate data structure
    create_initial_data_structure(input_data_file)

if __name__ == "__main__":
    main()
    

input_data_file = break_tweet_into_dicts.hash_mention_list
normalized_matrix = create_initial_data_structure(input_data_file)




