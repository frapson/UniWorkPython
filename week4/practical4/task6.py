password_1 = input("Enter your new password: ")
if len(password_1) < 6 or len(password_1) > 12:
    print("Password must be between 6 and 12 characters.")
    exit()

password_2 = input("Enter your password again: ")

if password_1 == password_2:
    print("Password Changed")
else:
    print("Passwords don't match.")