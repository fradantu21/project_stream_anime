from funzioni import *


def removeM(s):
    final = ""
    for char in s:
        if char == '-':
            final += " "
        else:
            final += char
    return final


def main():

    found = []

    while len(found) < 1:
        nome_anime = input("cerca anime: ")
        found = search(nome_anime)

        for i in range(len(found)):
            name = str(found[i])
            name = name.split("/")[-1]
            name = removeM(name)
            print(f"n{i+1} {name}")
        print()

        nome = int(input("inserire numero: "))
        anime = choose(found[nome-1])

        Nep = int(input(f"inserire numero episodio range({1}-{len(anime)}): "))
        Nep = Nep - 1

        com = ""
        while com != "n":
            if Nep >= 0 and Nep < len(anime):
                ep = episode(anime[Nep])
                play(ep)
                com = input(
                    "[p] per guardare prossimo episodio \n[n] per scegliere un novo anime \n[q] per uscire \ninserisci: ")
                if com == "p":
                    Nep += 1
                if com == "n":
                    found = []
                if com == "q":
                    quit()
            else:
                print("episodio non esistente")
                found = []
                break


if __name__ == '__main__':
    main()
