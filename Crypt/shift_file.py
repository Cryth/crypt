import crypt

def main():
    file = input("File: ")
    shift = input("Password: ")
    with open(file) as fr, open("shifted_" + file, "w") as fw:
        content = fr.readlines()
        content = [line.strip() for line in content]
        for line in content:
        	fw.write(crypt.caesar(line, int(shift)) + "\n")

if __name__ == "__main__":
    main()
