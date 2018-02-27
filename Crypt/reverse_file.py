import crypt

def main():
    file = input("File: ")
    with open(file) as fr, open("reversed_" + file, "w") as fw:
        content = fr.readlines()
        content = [line.strip() for line in content]
        for line in content:
        	fw.write(crypt.reversedAlphabet(line) + "\n")

if __name__ == "__main__":
    main()
