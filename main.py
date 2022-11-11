import json 

def json_file_to_dict(file_path: str) -> dict:
    '''convert json to dict
    
    Args:
        file_path (str): file path.
        
    Returns:
        dict: dict data
    '''
    data = open(file_path).read()
    data_json = json.loads(data)
    return data_json


def get_number_of_users(data: dict) -> int:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        int: number of all users.
    '''
    sum = []
    
    return len  (data['users'])
data = json_file_to_dict('data.json')
print((get_number_of_users(data)))


def get_all_countries(data: str) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of counrties
    '''
    return


def get_all_users_fullname(data: str) -> list:
    '''all users' data.
    
    Args:
        data (dict): users data
    
    Returns:
        list: list of all users' full name
    '''
    return


def get_user_by_id(id: int) -> dict:
    '''get user by id
    
    Args:
        id (int): user id.
        
    Returns:
        dict: user data
    '''
    return


def get_user_by_firstname(first_name: str) -> dict:
    '''get user by first name
    
    Args:
        first_name (str): user's first name.
        
    Returns:
        dict: user data
    '''
    return


def get_user_by_lastname(last_name: str) -> dict:
    '''get user by last name
    
    Args:
        first_name (str): user's last name.
        
    Returns:
        dict: user data
    '''
    return


def get_user_by_country(country: str) -> dict:
    '''get user by country
    
    Args:
        country (str): name of user's country.
        
    Returns:
        dict: user data
    '''
    return

