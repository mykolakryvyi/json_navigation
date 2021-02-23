"""
Mykola Kryvyi
Lab 3.2
"""
import pprint
import requests

def twitter_api(user_name):
    """
    Function returns from Twitter API information about
    user's account
    """
    base_url = "https://api.twitter.com/"

    bearer_token = ""

    search_url = '{}1.1/users/lookup.json'.format(base_url)

    search_headers = {
        'Authorization': 'Bearer {}'.format(bearer_token)
    }

    search_params = {
        'screen_name': user_name
    }

    response = requests.get(search_url, headers = search_headers, params=search_params)
    return response.json()[0]

if __name__ == "__main__":
    name_of_user = input('Type the name of the user you would like \
to view information about(without @): ')
    print('Here is list of keys that are available: ')
    standart_dictionary = twitter_api(name_of_user)
    while True:
        pprint.pprint(list(standart_dictionary.keys()))
        line = input('Would you like to view informatiom of the key?\
If no, press ^D or ^Z to finish: ')
        if line:
            if isinstance(standart_dictionary[line], dict):
                print('This is a dictionary')
                print('Here are keys of inner dictionary:')
                standart_dictionary = standart_dictionary[line]
            elif isinstance(standart_dictionary[line], list):
                print('This is a list')
                pprint.pprint(standart_dictionary[line])
                break
            else:
                pprint.pprint(standart_dictionary[line])
                break
            line = ''
