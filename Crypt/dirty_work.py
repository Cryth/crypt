import numpy as np
import sets


def list_overlap(alphabet, letter, shift):
    """ if shifting gets beyond character set's length """

    shift = shift % len(alphabet)  # corrects inputs bigger than character set's length

    position = alphabet.index(letter)

    if position + shift + 1 > len(alphabet):  # checks if shifted position is going to be beyond character set's length
        position = position + shift - len(alphabet)  # shifting with overlap
    else:
        position = position + shift  # shifting

    return position


def remove_duplicity(word):
    """ removes duplicity of characters from a word """

    new_word = ""

    for letter in word:
        if letter not in new_word:
            new_word += letter

    return new_word


def remove_numbers(word):
    """ removes numbrs from a word """
    new_word = ""
    for letter in word:
        if letter not in sets.numbers:
            new_word += letter
    return new_word


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

