# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Een re-make van je rekenmachine die voldoet aan flowcontrol.
　　　　　　  |　  1. Je vraagt de gebruiker om 2 getallen
　　　　　　  |　  2. Je vraagt de gebruiker om een bewerking op te geven
　　　　　　  |　  3. Je geeft correcte output
　　　　　　  ＼＿＿　＿＿＿＿＿＿＿
　　　　　　　　　  ∨
            ██████████  ████
        ████▒▒░░░░░░░░██▒▒░░██
      ██▒▒░░░░██░░██░░░░██░░░░██
    ██▒▒░░░░░░██░░██░░░░░░▒▒░░██
    ██░░░░░░░░██░░██░░░░░░▒▒▒▒██
  ██░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒██
██▒▒░░░░░░░░░░░░██░░░░░░░░░░░░██
██░░░░▒▒░░░░░░░░██░░░░░░░░░░▒▒██
██░░░░▒▒░░░░░░░░░░░░░░░░░░░░██  
  ██████░░░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░▒▒██  
██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░▒▒██    
██▒▒▒▒▒▒▒▒██░░░░░░░░░░▒▒████    
  ██▒▒▒▒▒▒▒▒██▒▒▒▒▒▒████▒▒▒▒██  
    ██▒▒▒▒██████████▒▒▒▒▒▒▒▒▒▒██
      ██████      ████████████  
"""

# IMPORTS


# CONFIG


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def optellen(getal_1, getal_2):
    return getal_1 + getal_2


def aftrekken(getal_1, getal_2):
    return getal_1 - getal_2


def vermenigvuldigen(getal_1, getal_2):
    return getal_1 * getal_2


def delen(getal_1, getal_2):
    return getal_1 / getal_2


def main():
    print("Welke bewerking wil je uitvoeren?")
    print("1: Optellen")
    print("2: Aftrekken")
    print("3: Vermenigvuldigen")
    print("4: Delen")
    keuze = int(input())

    print('Geef een eerste getal op:')
    getal_1 = int(input())
    print('Geef een tweede getal op:')
    getal_2 = int(input())

    resultaat = 0
    if keuze == 1:
        resultaat = (getal_1, getal_2)
    elif keuze == 2:
        resultaat = aftrekken(getal_1, getal_2)
    elif keuze == 3:
        resultaat = vermenigvuldigen(getal_1, getal_2)
    elif keuze == 4:
        resultaat = delen(getal_1, getal_2)

    print("Het resultaat is", resultaat,)


if __name__ == '__main__':
    main()
