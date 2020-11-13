student_ID = input("Enter your student ID number ")
username = input("Enter your username ")

banned_words = [student_ID, username, 'huddersfield',
                'password', 'cheese', 'programming']

password_1 = input("Enter your new password: ")
if len(password_1) < 6 or len(password_1) > 12:
    print("Password must be between 6 and 12 characters.")
    exit()
elif password_1 in banned_words:
    print("This password is too easy.\nCan't change the password")
    exit()

password_2 = input("Enter your password again: ")
if password_1 == password_2:
    print("Password Changed")
else:
    print("Passwords don't match. Can't change the password")