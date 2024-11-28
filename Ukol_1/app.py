from users import login_user, register


while True:
    username = input("Zadej username: ")
    password = input("Zadej heslo:")
    print(username, password)
    succes= login_user(username, password)
    if succes:
        print("ok")
        break
    else:
        print("invalid")
        