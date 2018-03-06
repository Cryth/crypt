import sets as sets
import dirty_work as dw


def caesar_cipher(text, shift=-3):
    """ encrypting by shifting in alphabet """
    new_text = ""

    for letter in text:
        if letter in sets.small:
            new_index = (sets.small.index(letter) + shift) % 26
            new_text += sets.small[new_index]
        elif letter in sets.caps:
            new_index = (sets.caps.index(letter) + shift) % 26
            new_text += sets.caps[new_index]
        elif letter in sets.numbers:
            new_index = (sets.numbers.index(letter) + shift) % 10
            new_text += sets.numbers[new_index]
        else:
            new_text += letter
    return new_text


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

    new_alphabet = dw.create_alphabet(password)

    for letter in text:
        if letter in sets.small:
            encrypted_text += new_alphabet[sets.small.index(letter)]
        elif letter in sets.caps:
            encrypted_text += new_alphabet[sets.caps.index(letter)].upper()
        else:
            encrypted_text += letter

    return encrypted_text


def keyword_decrypt(text, password):
    """ decryption using password to create dependent set of characters """

    decrypted_text = ""
    new_alphabet = dw.create_alphabet(password)
    for letter in text:
        if letter in sets.small:
            decrypted_text += sets.small[new_alphabet.index(letter)]
        elif letter in sets.caps:
            decrypted_text += sets.caps[new_alphabet.index(letter.lower())]
        else:
            decrypted_text += letter

    return decrypted_text


def square_encrypt(text, password=''):
    encrypted_text = ""  # initialize an empty encrypted text String object
    text = text.lower()
    text = dw.remove_numbers(text)
    new_alphabet = dw.create_alphabet(password)
    new_alphabet = new_alphabet.replace("q", "")

    print(dw.alphabet_matrix(password))
    for letter in text:
        if letter in sets.small:
            row = int(new_alphabet.index(letter) / 5)
            col = int(new_alphabet.index(letter) % 5)
            encrypted_text += str(row + 1) + str(col + 1)
        else:
            encrypted_text += letter
    return encrypted_text


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
