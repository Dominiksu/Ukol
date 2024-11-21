import os, json, hashlib

DATA_PATH = "C:/Users/domin/Documents/Python_01/Ukoly/Ukol_1/users.json"

def hash_password(password):
    hash_value = hashlib.sha256(password.encode())
    return hash_value.hexdigest()

def check_password(password, password_check):
    if password != password_check:
        raise ValueError("passwords does not match")

def write_data(data):
    with open (DATA_PATH, mode="w", encoding="utf8") as file:
        json.dump(data, file)

def read_data():
    with open (DATA_PATH, encoding="utf-8") as file:
        data = json.load(file)
        return data
    
def check_username(data, username):
    if username in data:
        raise ValueError ("Username already in use")


def login_user(Username, password):
    data = read_data()
    try:
        assert data[Username] == hash_password(password), "chybné heslo"
        return True
    except(KeyError, AssertionError):
        return False


def register(username, password, password_check):
    
    check_password(password, password_check)
    data = read_data()
    check_username(data, username)
    data[username] = hash_password(password)
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

def zkouska():
    change_password("test7", "heslo7","heslo heslo")

def test2():
    register("TEST", "HESLO", "HESLO")

zkouska()