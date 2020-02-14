""" Author: Kyle Evangelisto
    Date Programed: 2/13/2020
    Professor aw
    CSC 226 Project 2 Part 2
    Purpose: South America Country
    and Capitol City Quiz,
    Utilizes Dictionaries"""


def main():  # main method, calls the startup method and dictionary logic, drives the whole program.
    startup()
    dictionary_logic()


def startup():  # startup outputs a blurb of instructions to the user
    print("Welcome to the South American Countries Quiz!\nEach South American Country will be listed and you will"
          "have to input that countries capitol city name. Spelling and capitol letters matter."
          "\nBegin:")


def dictionary_logic():  # The logic for the whole game. Includes functionality such as counters, dictionaries,
    # file input and output streams, loops and conditional statements.
    counter = 0  # keeps count of the player's correct answers
    dictionary = {}  # creates a new dictionary
    with open('input.txt', 'r') as file:  # opens the file input.txt and reads it in.
        for element in file:  # for each element in the file, iterate through and assign each key and value
            (key, value) = element.split(",")  # split each key and value per line via  a ','
            dictionary[key] = value
            #  print(dictionary[key]) debug info
    for key, value in dictionary.items():  # for each key and value in the dictionaries items loop through, print out
        # the key for the player to see
        print(key)
        # print(value) debug info
        player_answer = input()  # get the player's answer and assign it to the variable "player answer"
        if player_answer == value.strip('\n'):  # if the player's answer is equal to the key's value
            print("Correct")  # tell the player they are correct
            counter += 1  # add one to the score counter
            # print(counter) debug info
        else:
            print("Incorrect")  # tells the player they are incorrect
    print("Average Score:", "{:.2%}".format(counter / 13), "\nTotal Correct: ", counter,
          "Total Incorrect: ", 13 - counter)  # prints out the player's stats from the quiz including average score,
    # number of questions incorrect and correct. Also formats the % to two decimal places.
    for key, value in dictionary.items():  # for each key and value in the dictionary, output the formatted dictionary
        print("Country: ", key, "Capitol: ", value, end='')


main()  # main function call, drives the program.
