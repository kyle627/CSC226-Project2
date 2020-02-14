""" Author: Kyle Evangelisto
    Date Programed: 2/13/2020
    Professor aw
    CSC 226 Project 2 Part 1
    Purpose: Check the validity of a user
    changing their password."""


def main():
    startup()  # Calls the startup method.
    check_size()  # Calls the Check Size Method


def startup():  # Startup displays a set of instructions to the user for the requirements for the password.
    print("Hello it's time to update your password.\nPlease enter a new password "
          "that is at least nine characters long, has 1 uppercase letter, 1 lowercase letter "
          "and at least 1 digit:\n")


def recall():  # Recall is a traceback method meaning that if the password is entered incorrectly at any point,
    # this method is run and the process begins again.
    print("That password does not meet the criteria, please enter in a password that meets the criteria:\n")
    check_size()


def password_incorrect():  # Password incorrect is run when the entered password meets the criteria but does not
    # match when the user re-validates the password.
    print("Your passwords did not match, please enter in a new password:\n")
    check_size()


def check_size():  # Check Size checks to make sure that the password entered is a valid length (greater than or
    # equal to 9 digits)
    new_password = input()
    if len(new_password) < 9:  # If the length of the password is less than 9 digits, the recall method is called.
        recall()
    else:
        print("Length okay")  # debug info
        check_for_digit(new_password)  # The check for digit method is called and the new password is passed to it.


def check_for_digit(new_password):  # check for digit checks to see if the password contains one or more digit. If it
    # does, it continues to be checked for the other criteria, if not, the recall method is called.
    digit_checker = False  # digit checker is a boolean method originally set to false, and is set to true if the
    # password contains a digit
    for element in new_password:
        if element.isdigit():
            digit_checker = True
    if digit_checker == True:
        print("digit valid")  # debug info
        check_lower_case(new_password)   # The check for lower case method is called and the new password is passed
        # to it.
    else:
        recall()


def check_lower_case(new_password):  # check for lower case checks to see if the password contains one or more lower
    # case letters. If it does, it continues to be checked for the other criteria, if not, the recall method is called.
    lower_checker = False  # lower checker is a boolean method originally set to false, and is set to true if the
    # password contains a lower case letter
    for element in new_password:
        if element.islower():
            lower_checker = True
    if lower_checker == True:
        print("lower case okay") # debug info
        check_upper_case(new_password) # The check for upper case method is called and the new password is passed
        # to it.
    else:
        recall()


def check_upper_case(new_password):  # check for upper case checks to see if the password contains one or more upper
    # case letters. If it does, it goes on to be confirmed, if not, the recall method is called.
    upper_checker = False  # upper checker is a boolean method originally set to false, and is set to true if the
    # password contains an upper case letter.
    for element in new_password:
        if element.isupper():
            upper_checker = True
    if upper_checker == True:
        print("uppercase valid")  # debug info
        confirmation(new_password)  # The confirmation method is called and the new password is passed
        # to it.
    else:
        recall()


def confirmation(new_password):  # outputs a blurb that the password meets the requirements, and then moves the new
    # password as well as the password inputed a second time to the validate method.
    confirmed_password = input("Okay, the password you entered is valid, please enter it in again to confirm:\n")
    validate(new_password, confirmed_password)


def validate(new_password, confirmed_password):  # validate checks to see if the new password is the same as the
    # password typed in a second time by the user. If it is the same, the password is confirmed, if not, the pasword
    # incorrect method is called, and the process starts again
    if new_password == confirmed_password:
        print("Your password has been confirmed, you are good to go!")
    else:
        password_incorrect()


main()  # calls the main function, starts the program.
