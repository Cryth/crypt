import numpy as np
import sets


def remove_duplicity(word):
    """ removes duplicity of characters from a word """
    new_word = ""

    for letter in word:
        if letter not in new_word:
            new_word += letter
    return new_word


def remove_numbers(word):
    """ removes numbers from a word """
    for num in sets.numbers:
        word = word.replace(str(num), "")
    return word


def only_letters(word):
    """ removes everything but letters """
    for letter in word:
        if (letter not in sets.small) and (letter not in sets.caps):
            word = word.replace(letter, "")
    return word


def create_set(password):
    """ creates a new alphabet String object dependent on password """
    password = only_letters(password).lower()
    password = remove_duplicity(password)  # password's characters can't be repeated

    for letter in sets.small:
        if letter not in password:
            password += letter
    return password
