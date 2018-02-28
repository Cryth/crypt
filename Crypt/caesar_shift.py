from crypt import caesar_encrypt


def main():
    print("Type 'q' and hit 'enter' to exit.")

    while True:
        text = input("Text to encrypt: ")
        if text == 'q':
            break
        print(caesar_encrypt(text))


if __name__ == "__main__":
        main()
