# coding=utf-8
def main():
    title("Square and multiply")
    while True:
        try:
            p = input("Prvok: ")
            if p == "exit()" or p == "quit()":
            	break

            m = input("Mocnina: ")
            if m == "exit()" or m == "quit()":
            	break

            z = input("Modulo: ")
            if z == "exit()" or z == "quit()":
            	break

            p, m, z = int(p), int(m), int(z)
            if p < 1 or m < 1 or z < 1:
                raise ValueError
        except (TypeError, ValueError):
            print("Zadajte prirodzené čísla!\n")
            continue

        # p**m mod z
        print("\n{}**{} mod {}\n".format(p,m,z))

        powers = lmp(m) # mocniny dvojky po m
        rm2(p, z, powers) # rozložený p**m mod z
        results = vyi(p, m, z, powers) # list mocniny m rozložený na mocniny dvojky
        vys(p, m, z, results) # výsledný príklad


def title(text):
    print("\n\t{}\n".format(text.upper()))


def nm2(m):
    """ zistí najväčiu mocninu 2 """
    p2 = 1
    while p2 < m:
        p2 = p2 * 2
    return p2/2 if p2 > 1 else p2


def lmp(m):
    """ vráti list mocniny dvojky po danú mocninu """
    powers = []
    while m >= 1:
        m2 = int(nm2(m))
        powers.append(m2)
        m -= m2
    return powers


def rm2(p, z, powers):
    """ rozloží p**m mod z pomocou mocnín dvojky """
    rozklad = "("
    for moc in powers:
        rozklad += "{}**{} * ".format(p, moc)
    print("{}) mod {}\n".format(rozklad[0:-3], z))


def vyi(p, m, z, powers):
    """ vypíše yi = ... a vráti pole so správnymi mocninami modulovanými z """
    results = []
    inc = 0
    while 2 ** inc <= nm2(m):
        result = (p ** (2 ** inc)) % z
        if (2 ** inc) in powers:
            results.insert(0, result)
        # yi+1 = p**(2**i) mod z = result
        print("y{} = {}**{} mod {} = {}".format(inc + 1, p, 2 ** inc, z, result))
        inc += 1
    return results


def vys(p, m, z, results):
    """ vysledok """
    priklad = "("
    for i in results:
        priklad += str(i) + " * "
    print("\n{}) mod {} = {}\n".format(priklad[0:-3], z, (p ** m) % z))


if __name__ == "__main__":
    main()
