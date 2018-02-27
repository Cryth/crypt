import sets as sets
import dirty_work as dw


def caesar_encrypt(text, shift=-3):
    """ encrypting by shifting in alphabet """

    encrypted_text = ""  # initialize an empty encrypted text String object

    for letter in text:
        if letter in sets.small:
            encrypted_text += sets.small[dw.list_overlap(sets.small, letter, shift)]
        elif letter in sets.caps:
            encrypted_text += sets.caps[dw.list_overlap(sets.caps, letter, shift)]
        elif letter in sets.numbers:
            encrypted_text += sets.numbers[dw.list_overlap(sets.numbers, letter, shift)]
        else:
            encrypted_text += letter

    return encrypted_text


def reversed_alphabet(text):
    """ encrypting by reversing alphabet """

    encrypted_text = ""  # initialize an empty encrypted text String object

    for letter in text:
        if letter in sets.small:
            encrypted_text += sets.small[(sets.small.index(letter) + 1) * -1]
        elif letter in sets.caps:
            encrypted_text += sets.caps[(sets.caps.index(letter) + 1) * -1]
        elif letter in sets.numbers:
            encrypted_text += sets.numbers[(sets.numbers.index(letter) + 1) * -1]
        else:
            encrypted_text += letter

    return encrypted_text


def keyword_encrypt(text, password):
    """ encryption using password to create dependent set of characters """

    encrypted_text = ""  # initialize an empty encrypted text String object

    new_alphabet = dw.createAlphabet(password)

    for letter in text:
        encrypted_text += new_alphabet[letter]

    return encrypted_text


def square_encrypt(text, password=''):
    encrypted_text = ""  # initialize an empty encrypted text String object
    text = text.lower()
    mat = dw.create_matrix(sets.small, password=password)
    print(type(mat))
    """print(mat)
    for letter in text:
        if letter in sets.small:
            row = int(mat.index(letter) / 5)
            col = int(sets.small.index(letter) % 5)
            encrypted_text += str(row + 1) + str(col + 1)
        elif letter in sets.numbers:
            raise ValueError("Can't use numbers for this encryption.")
        else:
            encrypted_text += letter
    return encrypted_text"""


def square_decrypt(text, password='', alphabet='small'):
    decrypted_text = ""  # initialize an empty decrypted text String object

    if alphabet.lower() == 'large' or 'l':
        alphabet = sets.caps
        password = password.upper()
    else:
        alphabet = sets.caps
        password = password.lower()
    mat = dw.create_matrix(alphabet, password=password)
    row = 0
    for num in text:
        if num in sets.numbers:
            if row > 0:
                decrypted_text += mat[row - 1][num - 1]
                row = 0
            else:
                row = num
        else:
            row = 0
    return decrypted_text


print(dw.create_matrix(sets.small))