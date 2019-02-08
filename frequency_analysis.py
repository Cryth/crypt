# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt


chars = list("abcdefghijklmnopqrstuvwxyz")
ci = [num for num in range(len(chars))]
col = ['r', 'b', 'g', 'c']

files = [] # file names
file_ca = [] # lists of character amounts

def main():
    title("Frekvenčná analýza súborov")

    for _ in col:
        file = input("File path: ")
        if file == "" or file == " ":
            break
        files.append(file)
        _freqfile(file)
    if len(files) == 1:
        _bar(files[0])
    else:
        _plot()


def title(text):
    print("\n\t{}\n".format(text.upper()))


def _freqfile(file_name):
    with open(file_name, "r") as f:
        cp = 0  # celkovy pocet
        ca = [0 for _ in range(len(chars))]  # char amounts

        while True:
            ch = f.read(1).lower()
            if not ch:
                break
            if ch in chars:
                ca[chars.index(ch)] += 1
                cp += 1
        np_ca = np.array(ca)
        np_ca = np_ca / cp * 100 # percentá
        file_ca.append(np_ca)


def _bar(file_name):
    plt.bar(ci, file_ca[0], color=col[0])
    plt.title("Frekvenčná analýza súboru {}".format(file_name))
    plt.ylabel("Percentá")
    plt.xticks(ci, chars)
    for i, val in enumerate(file_ca[0]):
        per = round(val, 2)
        plt.text(i-.45, val+.2, str(per) + "%")
    plt.grid(True)
    plt.show()


def _plot():
    for i, ca in enumerate(file_ca):
        plt.plot(ci, ca, color=col[i], label=files[i])
    plt.title("Frekvenčná analýza súborov {}".format(files))
    plt.legend(title="Súbory", loc='right', bbox_to_anchor=(0.5, 1.05), fancybox=True, shadow=True)
    plt.ylabel("Percentá")
    plt.xticks(ci, chars)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
