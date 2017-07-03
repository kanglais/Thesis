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
   
        # for p in every_mention_every_term_list: print(p)

        # create a set to hold each term ** only once **
        unique_term_set = create_set(every_mention_every_term_list)
        
        # generate zero vector, one zero corresponds to one unique term
        zero_vector = term_vector_generator(unique_term_set)



        
        new_test_dict = spawn_user_zero_vector_dict(zero_vector, unique_user_id_list)

        for k,v in new_test_dict.items():
            print(k, v)



def spawn_user_zero_vector_dict(zero_vector, unique_user_id_list):
    
    user_zero_vector_dict =  {}
    index_tracker = 0
    number_of_users = len(unique_user_id_list) - 1

    while index_tracker <= number_of_users:
        
        user_zero_vector_dict.update({ unique_user_id_list[index_tracker] : zero_vector})

        index_tracker += 1

    return user_zero_vector_dict


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


def term_vector_generator(unique_term_set):

    term_vector = []

    for term in  unique_term_set:
        term_vector.extend('0')

    return term_vector




def main():

    # define input data file
    input_data_file = './data/toy_data.json'
    
    # generate data structure
    create_initial_data_structure(input_data_file)

if __name__ == "__main__":
    main()
    
    













