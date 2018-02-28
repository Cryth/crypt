from crypt import caesar_encrypt


def main():
    while True:
        try:
            shift = input("Choose a shift: ")
            shift = int(shift)
            break
        except ValueError:
            print("Shift must be an integer!")
            continue

    print("Type 'q' and hit 'enter' to exit.")

    while True:
        text = input("Text to encrypt: ")
        if text == 'q':
            break
        print(caesar_encrypt(text, shift))


if __name__ == "__main__":
    main()
