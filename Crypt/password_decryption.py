from crypt import keyword_decrypt
from dirty_work import create_alphabet


def main():
    password = input("Choose a password: ")
    print(list(create_alphabet(password)))

    print("Type 'q' and hit 'enter' to exit.")
    while True:
        text = input("Type text: ")
        if text == 'q':
            break
        print(keyword_decrypt(text, password))


if __name__ == '__main__':
    main()