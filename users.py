import os, json

DATA_PATH = "c:/Users/domin/Documents/Python_01/03/users.json"
def check_password(password, password_check):
    if password != password_check:
        raise ValueError("passwords does not match")

def write_data(data):
    with open (DATA_PATH, mode="w", encoding="utf8") as file:
        json.dump(data, file)

def read_data():
    with open (DATA_PATH, encoding="utf-8") as file:
        data = json.load(file)
        print(type(data))
        return data
    
def check_username(data, username):
    if username in data:
        raise ValueError ("Username already in use")


def login_user(Username, password):
    data = read_data()
    try:
        assert data[Username] == password, "chybné heslo"
        return True
    except(KeyError, AssertionError):
        return False


def register(username, password, password_check):
    
    check_password(password, password_check)
    data = read_data()
    check_username(data, username)
    data[username] = password
    write_data(data)

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password:
        del data[username]
        write_data(data)
    
def change_password(username, password, new_password,):
    data = read_data()
    if username in data and data[username] == password:
        data[username] = new_password
        write_data(data)
    else:
        print("password could not be changed")


change_password("test7", "Heslo heslo","heslo7")