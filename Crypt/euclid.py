# coding=utf-8
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def vyjadri_a(a, b):
    while b:
        a, b = b, a%b
        if b > 0:
            print("{} = {}*{} + {}".format(a, b, int(a/b), a%b))


def gcd_generator(a, b):
    while b:
        yield "{} : {} = {} zv. {}".format(a, b, int(a/b), a%b)
        a, b = b, a%b


def solve_gcd(a, b):
    for i in gcd_generator(a, b):
        print(i)


def flc(a, b):
    """ find linear combination """
    x = 0
    nsd = gcd(a, b)
    while True:
        y = a * x - nsd
        # print(x, y / -b)
        if y % -b == 0:
            return x, int((y / -b)%a)
        x += 1



def main():
    print("ROZŠÍRENÝ EUKLIDOV ALGORITMUS\n")
    while True:
        stra = input("Inverzný prvok k: ")
        strb = input("K základu: ")
        a, b = int(stra), int(strb)
        print("\n{}**-1 mod {}\n".format(a, b))
        solve_gcd(b, a)
        print("")
        nsd = gcd(b, a)
        vyjadri_a(b, a)
        x, y = flc(b, a)
        print("\n{} = {}*{} - {}*{}\n".format(nsd, b, x, a, y))
        print("INVERZNÝ PRVOK JE {}\n".format(y))


if __name__ == "__main__":
    main()