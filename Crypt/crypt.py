import sets as sets
import dirty_work as dw


def caesar(text, shift=-3):
    """ shifting in alphabet """
    # new_set_list = [sets.small[sets.small.index(letter) + shift) % 26] for letter in sets.small]
    # new_set = ""
    # for letter in new_set_list:
    #     new_set += letter
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


def keyword(text, key, decrypt=False):
    """ encryption using keyword to create dependent set of characters """
    new_text = ""
    new_set = dw.create_set(key)

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


def bacon(text, decrypt=False):
    result = ""
    if decrypt:
        text = list(text)
        binary = [16, 8, 4, 2, 1]
        pismena = [text[i:i + 5] for i in range(0, len(text), 5)]
        for letter in pismena:
            desifra = [a * int(b) for a, b in zip(binary, letter)]
            result += sets.small[sum(desifra)]
        return result

    else:
        for letter in text:
            if letter in sets.small:
                result += dw.to_binary(sets.small.index(letter), 5)
            elif letter == " ":
                result += letter

        return result


def polybius_square(text, decrypt=False):
    new_text = ""
    new_set = sets.caps.replace("J", "")

    if decrypt:
        row = 0

        for letter in text:
            if letter in sets.numbers:
                if row > 0:
                    index = (row - 1) * 5 + int(letter) - 1
                    new_text += new_set[index]
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
            if letter in new_set:
                row = int(new_set.index(letter) / 5) + 1
                col = int(new_set.index(letter) % 5) + 1
                new_text += str(row) + str(col)
            else:
                new_text += letter
    return new_text


def playfair(text, key, decrypt=False, omitq=False):
    text = dw.only_letters(text).lower()  # text can be only small letters
    if decrypt == False:
        text = dw.put_x(text)
    new_set = dw.create_set(key)
    if omitq:
        new_set = new_set.replace("q", "") # remove q from square
        text = text.replace("q", "") # remove q from the text
    else:
        new_set = new_set.replace("j", "") # remove j from square
        text = text.replace("j", "i") # replace j by i in the text
    new_text = ""
    letter1 = "" # first letter of the pair

    for letter in text:
        if len(letter1) < 1:
            letter1 = letter
            continue
        il1 = new_set.index(letter1) # index letter 1
        il2 = new_set.index(letter) # index letter 2
        # if letters appear on the same row, move them to the right of the square
        if int(il1 / 5) ==  int(il2 / 5):
            if decrypt:
                new_text += dw.shift_in_square(letter1, new_set, -1)
                new_text += dw.shift_in_square(letter, new_set, -1)
            else:
                new_text += dw.shift_in_square(letter1, new_set)
                new_text += dw.shift_in_square(letter, new_set)
        # if letters appear on the same column, move them down in the square
        elif il1 % 5 == il2 % 5:
            if decrypt:
                new_text += dw.shift_in_square(letter1, new_set, -1, False)
                new_text += dw.shift_in_square(letter, new_set, -1, False)
            else:
                new_text += dw.shift_in_square(letter1, new_set, row=False)
                new_text += dw.shift_in_square(letter, new_set, row=False)
        else:
            new_index = il1 - (il1 % 5) + (il2 % 5)
            new_text += new_set[new_index]
            new_index = il2 - (il2 % 5) + (il1 % 5)
            new_text += new_set[new_index]
        letter1 = ""
        new_text += " " # put space between pairs
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
