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
        if letter not in sets.small or letter not in sets.caps:
            word = word.replace(letter, "")
    return word


def create_alphabet(password):
    """ creates a new alphabet String object dependent on password """
    password = remove_numbers(password).lower()
    password = remove_duplicity(password)  # password's characters can't be repeated

    for letter in sets.small:
        if letter not in password:
            password += letter
    return password


def alphabet_matrix(password='', removed_letter='q'):
    matrix = []
    list_row = []
    num = 0
    alpha_list = list(create_alphabet(password))
    alpha_list.remove(removed_letter)

    for _ in range(5):
        for _ in range(5):
            list_row.append(alpha_list[num])
            num = num + 1
        matrix.append(list_row)
        list_row = []
    return np.array(matrix)
