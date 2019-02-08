import sets


def remove_duplicity(word):
    """ removes duplicity of characters from a word """
    new_word = ""

    for letter in word:
        if letter not in new_word:
            new_word += letter
    return new_word

def to_binary(number, length):
    """ converts number to binary of desired bit length"""
    number = int(number)
    result = ""
    while number > 0:
        result = str(number % 2) + result
        number = int(number / 2)
    if len(result) < length:
        result = (length-len(result)) * "0" + result

    return result

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


def put_x(word):
    """ puts x between letter pairs if they are the same
    puts x at the end of the text if its length is odd """
    new_word = ""
    for letter in word:
        if len(new_word)%2 == 1 and letter == new_word[-1]:
            new_word += "x" + letter
        else:
            new_word += letter
    if len(new_word) % 2 == 1:
        new_word += "x"
    return new_word

def shift_in_square(letter, set, shift=1, row=True):
    """ move characters in a row or column of polybius square """
    if row:
        new_index = (set.index(letter) + shift) % 5 + set.index(letter) - set.index(letter) % 5
        return set[new_index]
    new_index = (set.index(letter) + 5 * shift) % 25
    return set[new_index]


def create_set(password):
    """ creates a new alphabet String object dependent on password """
    password = only_letters(password).lower()
    password = remove_duplicity(password)  # password's characters can't be repeated

    for letter in sets.small:
        if letter not in password:
            password += letter
    return password
