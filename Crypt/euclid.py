# coding=utf-8
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solve(a, b):
    while b:
        a, b = b, a % b
        if b > 1:
            yield a, b


def gcd_generator(a, b):
    while b:
        yield "{} : {} = {} zv. {}".format(a, b, int(a / b), a % b)
        a, b = b, a % b


def solve_gcd(a, b):
    for i in gcd_generator(a, b):
        print(i)
    return gcd(a, b)


def flci(a, b):
    """ find linear combination by increasing x """
    x = 0
    nsd = gcd(a, b)
    while True:
        y = a * x - nsd
        if y % b == 0:
            return x, int(y / -b)
        x += 1


def flcd(a, b):
    """ find linear combination by decreasing x """
    x = 0
    nsd = gcd(a, b)
    while True:
        y = a * x - nsd
        if y % b == 0:
            return x, int(y / -b)
        x -= 1


def title():
    print("\n\tMULTIPLIKATÍVNA INVERZIA - ROZŠÍRENÝ EUKLIDOV ALGORITMUS\n")


def main():
    title()
    while True:
        # input prvok
        a = input("Prvok: ")
        if a == "exit()" or a == "quit()":
            break

        # input zvyskova trieda
        b = input("Zvyšková trieda: ")
        if b == "exit()" or b == "quit()":
            break

        # skontroluj prirodzené čísla
        try:
            p, z = int(a), int(b)
            if p <= 0 or z <= 0:
                raise ValueError
        except (TypeError, ValueError):
            print("\n\tZADAJTE PRIRODZENÉ ČÍSLA\n")
            continue

        # p**-1 mod z
        print("\t\n{}**-1 mod {}\n\n".format(p, z))

        # vypočítaj nsd a skontroluj, či je rovné 1
        nsd = solve_gcd(z, p)  # euklidov algoritmus
        if nsd != 1:
            print("\tINVERZNÝ PRVOK NEEXISTUJE\n")
            continue

        # vypíš vyjadrenia zvyškov
        for a, b in solve(z, p):
            print("{0} = {1}*{2} + {3}\t\t{3} = {0} - {1}*{2}".format(a, b, int(a / b), a % b))

        # vypíš riešenie nájdenia inverzného prvku
        print("")
        # dosadzuj(ea)

        # nájdi lineárnu kombináciu --> y je inverzný prvok
        x, y = flcd(z, p)

        # 1 = z*x + p*y
        print("\n{} = {}*{} + {}*{}\n".format(nsd, z, x, p, y))

        # INVERZNÝ PRVOK JE y%z
        print("\tINVERZNÝ PRVOK JE {}\n".format(y % z))


if __name__ == "__main__":
    main()
