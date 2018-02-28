from crypt import keyword_encrypt, keyword_decrypt


def main():
    file = input("File: ")
    decrypt = input("Type '1', 'd' or 'decrypt' to use decryption: ")
    decrypt = check_encrypt(decrypt)
    password = input("Password: ")

    if decrypt:
        file_prefix = "decrypted_"
    else:
        file_prefix = "encrypted_"

    with open(file) as fr, open(file_prefix + file, "w") as fw:
        content = fr.readlines()
        content = [line.strip() for line in content]
        if decrypt:
            for line in content:
                fw.write(keyword_decrypt(line, password) + "\n")
        else:
            for line in content:
                fw.write(keyword_encrypt(line, password) + "\n")


def check_encrypt(word):
    word = word.lower()
    return word == "d" or word == "decrypt" or word == "1"


if __name__ == '__main__':
    main()