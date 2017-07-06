import pprint
import json
import numpy as np
from sklearn import preprocessing

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
        
        #create a dict to hold 0's or 1's based on which terms the user used
        associated_value_return_dict = associate_terms_with_user(unique_term_set, all_users_terms_dict)

        #transform the above dict into a matrix
        matrix_of_associated_values = matrix_creation(associated_value_return_dict)

        #normalize matrix
        normalized_matrix = normalize_associated_term_values(matrix_of_associated_values)

    return normalized_matrix

def normalize_associated_term_values(matrix_of_associated_values):

    matrix_as_float = matrix_of_associated_values.astype(float)

    normalized_matrix = preprocessing.normalize(matrix_as_float)

    return normalized_matrix   

def matrix_creation(associated_value_return_dict):

    matrix_of_associated_values = []

    for user in associated_value_return_dict:
        matrix_of_associated_values.append(associated_value_return_dict[user])

    matrix_of_associated_values = np.matrix(matrix_of_associated_values)

    return matrix_of_associated_values


def associate_terms_with_user(unique_term_set, all_users_terms_dict):

    associated_value_return_dict = {}

    # consider the first user
    for user_id in all_users_terms_dict:

        # what terms *could* this user have possibly used
        this_user_zero_vector = []


        # this could be refactored somehow
        for term in  unique_term_set:
            # this_user_zero_vector.extend(0)

            this_user_zero_vector.insert( len(this_user_zero_vector) ,0)
            #to create array of zeros:
            #np.zeros(this_user_zero_vector)

        # what terms *did* this user use
        terms_belong_to_this_user = all_users_terms_dict.get(user_id)

        # let's start counting all the possible terms that this term in the personal
        # user list of words could correspond to... 
        global_term_element_index = 0

        # while this one term is in the range of all possible terms
        while global_term_element_index < len(unique_term_set):

            # start counting the number of terms he used
            local_term_set_item_index = 0

            # if this one term he used is still in the range of terms he used, counting them one by one
            while local_term_set_item_index < len(terms_belong_to_this_user):

                # if this one user term is the same as this one global term
                if list(unique_term_set)[global_term_element_index] == terms_belong_to_this_user[local_term_set_item_index]:

                    # increment the number of times this user used this term
                    this_user_zero_vector[global_term_element_index] += 1

                # go to the next term for this user
                local_term_set_item_index += 1

            # go to the next term in the global list of all possible terms
            global_term_element_index += 1

        associated_value_return_dict.update({user_id: this_user_zero_vector})

    return associated_value_return_dict


def generate_complete_terms_list_and_users_list(all_users_terms_dict):

    complete_terms_list = []

    complete_users_list = []

    for key, value in all_users_terms_dict.items():
        complete_terms_list.extend(value)
        if key not in complete_users_list:
            complete_users_list.append(key)

    return([complete_terms_list, complete_users_list])


def create_set(complete_terms_list):

    term_set = set(complete_terms_list)

    return term_set


def main():

    # define input data file
    input_data_file = './data/toy_data.json'
    
    # generate data structure
    create_initial_data_structure(input_data_file)

if __name__ == "__main__":
    main()
    




