from crypt import caesar_encrypt


def main():
    file = input("File: ")

    while True:
        try:
            shift = input("Password: ")
            shift = int(shift)
            break
        except ValueError:
            print("Shift must be an integer!")

    with open(file) as fr, open("shifted_" + file, "w") as fw:
        content = fr.readlines()
        content = [line.strip() for line in content]
        for line in content:
            fw.write(caesar_encrypt(line, shift) + "\n")


if __name__ == "__main__":
    main()
