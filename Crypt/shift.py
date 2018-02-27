import crypt 

def main():
    shift = input("Choose a shift: ")

    print("Type 'q' and hit 'enter' to exit.")

    while True:
            text = input("Text to encrypt: ")
            if text == 'q' :
                    break
            print(crypt.caesar(text, int(shift)))

if __name__ == "__main__":
    main()
