import crypt

def main():
    print("Type 'q' and hit 'enter' to exit.")

    while True:
            text = input("Text to encrypt: ")
            if text == 'q' :
                    break
            print(crypt.reversedAlphabet(text))

if __name__ == '__main__':
	main()
