import requests


def client_get_token():
    '''
    This function was used to create a token for the admin user 'b'.
    '''
    # Mimic admin credentials
    credentials = {
        'username': 'b',
        'password': 'testpassword',
    }
    # Get response from rest-auth login for admin
    response = requests.post(
        'http://127.0.0.1:8000/api/rest-auth/login/',
        data=credentials,
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
    token_h = 'Token 49b345e90dc17728f4acd3f3661faa3224dd0adb'
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
