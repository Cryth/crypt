import matplotlib.pyplot as plt


chars = list("abcdefghijklmnopqrstuvwxyz")
ci = [num for num in range(len(chars))]
ca = [0 for _ in range(len(chars))] # char amounts
col = 'red'
cp = 0 # celkovy pocet

def main():
    file = input("File path: ")
    _freqfile(file)
    _plot(file)


def _freqfile(file_name):
    with open(file_name, "r") as f:
        while True:
            ch = f.read(1)
            if not ch:
                break
            if ch in chars:
                ca[chars.index(ch)] += 1
                global cp
                cp += 1


def _plot(file_name):
    plt.plot(ci, ca, color=col)
    plt.title("Frekvenčná analýza súboru {}".format(file_name))
    plt.ylabel("Počet")
    plt.xticks(ci, chars)
    for i, val in enumerate(ca):
        per = round(val / cp * 100, 2) # percento
        plt.text(i,val,str(per)+"%")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()