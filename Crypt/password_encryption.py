from crypt import keyword_encrypt
from dirty_work import create_alphabet


def main():
    password = input("Choose a password: ")
    print(list(create_alphabet(password)))

    print("Type 'q' and hit 'enter' to exit.")
    while True:
        text = input("Type text: ")
        if text == 'q':
            break
        print(keyword_encrypt(text, password))


if __name__ == '__main__':
    main()