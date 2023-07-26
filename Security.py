def Sign_up():
    # SIGN UP

    # check user age
    age = int(input('Enter your age before you create your new account: '))
    print(" ")
    if age < 13 and age > 0:
        print('Sorry! You cannot be a user in FeelConditioner, you will be able to register until 13 years old')
    elif age >= 13:
        print("Welcome user! Please enter your new username ")
        print("Your username should be more than 6 and less than 12 characters ")

        # enter username
        username = str(input('Enter here: '))
        for i in range(1000):
            if len(username) not in range(6, 13, 1):
                print(" ")
                print("Invalid. Please try again ")
                username = str(input('Enter here: '))

            if len(username) in range(6, 13, 1):
                print("Valid")
                print(" ")
                break

            # enter password
        print("Please enter your new password ")
        print("Your password should be more than 6 characters")
        password = str(input("Enter here: "))
        for i in range(1000):
            if len(password) >= 6:
                print("Valid password")
                print("Your username and password were registered")
                print(" ")
                print("Welcome to FeelConditioner")
                break
            else:
                print(" ")
                print("Invalid password. Please try again ")
                password = str(input("Enter here: "))

    # Save username and password
    data_participant = open("/Users/phambaolong/PycharmProjects/pythonProject/data_user.txt", "w")

    # save username
    username_registered = f'{username} \n'
    data_participant.write(username_registered)

    # save password
    password_registered = f'{password}'
    data_participant.write(password_registered)

    data_participant.close()

def Log_in():
    # Login
    # Enter username and password first
    import random
    print("Hello 👋")
    # CHECK INPUT USERNAME AND PASSWORD
    with open("/Users/phambaolong/PycharmProjects/pythonProject/data_user.txt") as data_saved:
        package = [line.rstrip() for line in data_saved]
    username_corrected = package[0]
    password_corrected = package[1]
    data_saved.close()

    # Username
    print("LOGIN ")
    username_login = str(input("Enter your username: "))
    for i in range(1000):
        if username_login != username_corrected:
            print("Your username was wrong")
            print("Please try again")
            username_login = str(input("Enter your username: "))

        if username_login == username_corrected:
            print("Username checked!")
            print(" ")
            print("Welcome {name}, please enter your password".format(name=username_login))
            break

    # Password
    pass_login = str(input("Enter your password: "))
    for i in range(1000):
        if pass_login == password_corrected:
            print("Password Checked!")
            print(" ")
            break
        else:
            print("Your password was wrong")
            print("Please try again")
            pass_login = str(input("Enter your password: "))

    # Vertification code
    characters = "1234567890qwertyuiopasdfghjklzxcvbnm"
    list_characters = random.sample(characters, 4)
    list_characters_uppercase = random.sample(characters.upper(), 4)
    full_lists = list_characters + list_characters_uppercase
    verification_code = ''.join(str(i) for i in full_lists)
    print(" ")
    print(verification_code)
    print(" ")

    code = str(input("Enter your vertification code: "))
    for i in range(100000):
        if code == verification_code:
            print("All requirements are valid")
            print(" ")
            print("Welcome our user")
            break
        else:
            print("Please try again")
            print(" ")
            list_characters = random.sample(characters, 4)
            list_characters_uppercase = random.sample(characters.upper(), 4)
            full_lists = list_characters + list_characters_uppercase
            verification_code = ''.join(str(i) for i in full_lists)
            print(verification_code)
            print(" ")
            code = str(input("Enter your verification code: "))
