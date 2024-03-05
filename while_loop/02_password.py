username = input()
password = input()

while True:
    user_password = input()
    if user_password == password:
        print(f'Welcome {username}!')
        break
