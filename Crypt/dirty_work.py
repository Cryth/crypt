import numpy as np


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


def create_alphabet(alphabet, password):
    """ creates a new alphabet String object dependent on password """

    password = remove_duplicity(password)  # password's characters can't be repeated

    for letter in alphabet:
        if letter not in password:
            password += letter

    return password


def create_matrix(alphabet, password='', removed_letter='q'):
    matrix = []
    list_row = []
    num = 0
    alphabet = create_alphabet(alphabet, password)
    alpha_list = list(alphabet)
    alpha_list.remove(removed_letter)

    for _ in range(5):
        for _ in range(5):
            list_row.append(alpha_list[num])
            num = num + 1
        matrix.append(list_row)
        list_row = []
    return matrix
