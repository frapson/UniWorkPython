def how_many_exact_letters(word, letter):
    # if given parameter is NOT a string it throws an exception
    if type(word) != str:
        raise TypeError("must be str")
    else:
        # we count how many times given letter occurs
        count = 0
        for i in word:
            if i == letter:
                count += 1
    return count


def is_valid(email, domain):
    # string may contain spaces so we have to delete them
    email = email.strip(' ')

    # it splits given email to two parts: letter before and after "@"
    splitted = email.split("@")

    # if: there is not @, there is too much @'s, part before @ is empty or
    # domains are not the same it throws an exception
    if '@' not in email or how_many_exact_letters(email, "@") != 1 or \
            splitted[0] == '' or splitted[1] != domain:
        raise ValueError("{} is not valid at {}".format(email, domain))
    else:
        # it prints the information that given email is correct
        return "{} is valid at {}".format(email, domain)


while True:
    try:
        # we can type email and domain and check if it is valid
        email, domain = input(), input()
        print(is_valid(email, domain))
    except ValueError as error:
        # otherwise it throws an exception
        # it tells the user that email or domain is invalid
        print(error)