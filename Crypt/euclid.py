# coding=utf-8
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a


def vyjadri(a, b):
    while b:
        a, b = b, a%b
        if b > 0:
            print("{0} = {1}*{2} + {3}\t\t{3} = {0} - {1}*{2}".format(a, b, int(a/b), a%b))


def gcd_generator(a, b):
    while b:
        yield "{} : {} = {} zv. {}".format(a, b, int(a/b), a%b)
        a, b = b, a%b


def solve_gcd(a, b):
    for i in gcd_generator(a, b):
        print(i)
    return gcd(a, b)


def flc(a, b):
    """ find linear combination """
    x = 0
    nsd = gcd(a, b)
    while True:
        y = a * x - nsd
        if y % -b == 0:
            return x, int(y / -b)
        x += 1


def main():
    print("\tMULTIPLIKATÍVNA INVERZIA - ROZŠÍRENÝ EUKLIDOV ALGORITMUS\n")
    while True:
        a = input("Prvok: ")
        if a == "exit()" or a == "quit()":
            break

        b = input("Zvyšková trieda: ")
        if b == "exit()" or b == "quit()":
            break

        # ak nie su prirodzené čísla
        try:
            p, z = int(a), int(b)
            if p <= 0 or z <= 0:
                raise ValueError
        except (TypeError, ValueError):
            print("\n\tZADAJTE PRIRODZENÉ ČÍSLA\n")
            continue

        # p**-1 mod z
        print("\t\n{}**-1 mod {}\n".format(p, z))

        nsd = solve_gcd(z, p) # euklidov algoritmus
        print("")

        # platí len pre nsd == 1
        if nsd != 1:
            print("\tINVERZNÝ PRVOK NEEXISTUJE\n")
            continue

        vyjadri(z, p) # vyjadri zvyšky

        x, y = flc(z, p) # vypočítaj inverzný prvok

        # 1 = z*x + p*y
        print("\n{} = {}*{} + {}*{}\n".format(nsd, z, x, p, y))

        # INVERZNÝ PRVOK JE y mod z = y%z
        print("\tINVERZNÝ PRVOK JE {} mod {} = {}\n".format(y, z, y%z))


if __name__ == "__main__":
    main()