import pprint
import json

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
        

        associate_terms_with_user(unique_term_set, all_users_terms_dict)


def associate_terms_with_user(unique_term_set, all_users_terms_dict):

    associated_value_return_dict = {}

    # consider the first user
    for user_id in all_users_terms_dict:

        print(user_id)

        # what terms *could* this user have possibly used
        this_user_zero_vector = []

        # this could be refactored somehow
        for term in  unique_term_set:
            this_user_zero_vector.extend('0')

        print("what terms *could* this user have possibly used: ", this_user_zero_vector, '\n')

        # what terms *did* this user use
        terms_belong_to_this_user = all_users_terms_dict.get(user_id)

        print("what terms *did* this user use: ", terms_belong_to_this_user, '\n')

        # let's start counting all the possible terms that this term in the personal
        # user list of words could correspond to... 
        global_term_element_index = 0

        # while this one term is in the range of all possible terms
        while global_term_element_index < len(unique_term_set):

            # start count
            ing the number of terms he used
            local_term_set_item_index = 0

            # if this one term he used is still in the range of terms he used, counting them one by one
            while local_term_set_item_index < len(terms_belong_to_this_user):

                print('\t',list(unique_term_set)[global_term_element_index])

                # if this one user term is the same as this one global term
                if list(unique_term_set)[global_term_element_index] == terms_belong_to_this_user[local_term_set_item_index]:

                    # increment the number of times this user used this term
                    this_user_zero_vector[global_term_element_index] = '1'

                # go to the next term for this user
                local_term_set_item_index += 1

            # go to the next term in the global list of all possible terms
            global_term_element_index += 1

        associated_value_return_dict.update({user_id: this_user_zero_vector})

    pprint.pprint(associated_value_return_dict)


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
    input_data_file = './data/toy_toy_data.json'
    
    # generate data structure
    create_initial_data_structure(input_data_file)

if __name__ == "__main__":
    main()
    




