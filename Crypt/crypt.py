import sets as sets
import dirty_work as dw


def caesar(text, shift=-3):
    """ shifting in alphabet """
    # new_alphabet_list = [sets.small[sets.small.index(letter) + shift) % 26] for letter in sets.small]
    # new_alphabet = ""
    # for letter in new_alphabet_list:
    #     new_alphabet += letter
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


def atbash(text):
    """ reversing alphabet """
    new_text = ""

    for letter in text:
        if letter in sets.small:
            new_index = (sets.small.index(letter) + 1) * -1
            new_text += sets.small[new_index]
        elif letter in sets.caps:
            new_index = (sets.caps.index(letter) + 1) * -1
            new_text += sets.caps[new_index]
        elif letter in sets.numbers:
            new_index = (sets.numbers.index(letter) + 1) * -1
            new_text += sets.numbers[new_index]
        else:
            new_text += letter
    return new_text


def rot13(text):
    """ rotate by 13 places """
    new_text = ""

    for letter in text:
        if letter in sets.small:
            new_index = (sets.small.index(letter) - 13) % 26
            new_text += sets.small[new_index]
        elif letter in sets.caps:
            new_index = (sets.caps.index(letter) - 13) % 26
            new_text += sets.caps[new_index]
        elif letter in sets.numbers:
            new_index = (sets.numbers.index(letter) - 5) % 10
            new_text += sets.numbers[new_index]
        else:
            new_text += letter
    return new_text


def keyword(text, password, decrypt=False):
    """ encryption using password to create dependent set of characters """
    new_text = ""
    new_set = dw.create_set(password)

    for letter in text:
        if letter in sets.small:
            if decrypt:
                new_text += sets.small[new_set.index(letter)]
            else:
                new_text += new_set[sets.small.index(letter)]
        elif letter in sets.caps:
            if decrypt:
                new_text += sets.caps[new_set.index(letter.lower())]
            else:
                new_text += new_set[sets.caps.index(letter)].upper()
        else:
            new_text += letter
    return new_text


def polybius_square(text, decrypt=False):
    new_text = ""
    new_alphabet = sets.caps.replace("J", "")

    if decrypt:
        row = 0

        for letter in text:
            if letter in sets.numbers:
                if row > 0:
                    index = (row - 1) * 5 + int(letter) - 1
                    new_text += new_alphabet[index]
                    row = 0
                else:
                    row = int(letter)
            else:
                row = 0
                new_text += letter
    else:
        text = text.upper()
        text = dw.remove_numbers(text)
        text = text.replace("J", "I")

        for letter in text:
            if letter in new_alphabet:
                row = int(new_alphabet.index(letter) / 5) + 1
                col = int(new_alphabet.index(letter) % 5) + 1
                new_text += str(row) + str(col)
            else:
                new_text += letter
    return new_text


def vigenere(text, key=sets.small, decrypt=False, autokey=False):
    new_text = ""
    if autokey:
        key = key + text
    key = key.lower()
    key = dw.only_letters(key)
    kp = 0  # key position

    for letter in text:
        if letter in sets.small:
            if decrypt:
                new_index = (sets.small.index(letter) - sets.small.index(key[kp])) % 26
            else:
                new_index = (sets.small.index(letter) + sets.small.index(key[kp])) % 26
            new_text += sets.small[new_index]
            kp = (kp + 1) % len(key)
        elif letter in sets.caps:
            if decrypt:
                new_index = (sets.caps.index(letter) - sets.small.index(key[kp])) % 26
            else:
                new_index = (sets.caps.index(letter) + sets.small.index(key[kp])) % 26
            new_text += sets.caps[new_index]
            kp = (kp + 1) % len(key)
        else:
            new_text += letter
    return new_text


def beaufort(text, key=sets.small):
    new_text = ""
    key = key.lower()
    key = dw.only_letters(key)
    kp = 0  # key position

    for letter in text:
        if letter in sets.small:
            new_index = (sets.small.index(key[kp]) - sets.small.index(letter)) % 26
            new_text += sets.small[new_index]
            kp = (kp + 1) % len(key)
        elif letter in sets.caps:
            new_index = (sets.small.index(key[kp]) - sets.caps.index(letter)) % 26
            new_text += sets.caps[new_index]
            kp = (kp + 1) % len(key)
        else:
            new_text += letter
    return new_text
