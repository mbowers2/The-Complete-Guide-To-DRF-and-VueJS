import requests


def client_get_token():
    '''
    This function was used to create a token to register a new user: 'a'.
    '''
    # Mimic admin credentials
    data = {
        'username': 'a',
        'email': 'a@a.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
    # Get response from rest-auth login for admin
    response = requests.post(
        'http://127.0.0.1:8000/api/rest-auth/registration/',
        data=data,
    )
    print('status code:', response.status_code)
    response_data = response.json()
    print(response_data)

def client_try_access():
    '''
    This function tests the use of the token to get permission for a the 
    profile list view.
    '''
    # That 'Token ' is needed before the actual token
    token_h = 'Token 553fc900bd3acac1b6ad576d892389e95e195da3'
    headers = {'Authorization': token_h}

    response = requests.get(
        'http://127.0.0.1:8000/api/profiles/',
        headers=headers,
    )
    print('status code:', response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == '__main__':
    #client_get_token()
    client_try_access()
