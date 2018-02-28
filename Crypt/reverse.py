from crypt import reversed_alphabet


def main():
    print("Type 'q' and hit 'enter' to exit.")

    while True:
        text = input("Text to encrypt: ")
        if text == 'q':
            break
        print(reversed_alphabet(text))


if __name__ == '__main__':
    main()
