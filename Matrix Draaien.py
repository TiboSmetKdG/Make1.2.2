# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Schrijf een script dat:
　　　　　　  |　Stel dat je een lijst met lijsten hebt waar elke waarde in de binnenste lijsten een tekenreeks is.
　　　　　　  |　Je kunt het raster[x][y] zien als het karakter op de x- en y-coördinaten van een "plaatje" dat met
　　　　　　  |　tekstkarakters is getekend. De (0, 0) oorsprong zal in de linkerbovenhoek liggen, de x-coördinaten
　　　　　　  |　nemen toe naar rechts, en de y-coördinaten nemen toe naar beneden.
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
LIJST = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]

GEDRAAIDE_LIJST = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.']]


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def print_matrix(m):
    for regel in m:                                 # de matrix zal overlopen worden voor elke regel die hij bevat
        for item in regel:                          # de regel zal overlopen worden voor elk item dat het bevat
            print(item, end="")                     # print elk item van de regel op 1 lijn
        print("")                                   # zorgt voor een nieuwe lijn


def turn_left():
    i = 0                                           # Eerste teller voor de lengte van de lijst af te gaan.
    j = 0                                           # Eerste teller voor de hoogte van de lijst af te gaan.
    x = len(LIJST)                                  # Variabele die de lengte van de lijst bij houd
    y = len(LIJST[0])                               # Variabele die de hoogte van de lijst bij houd

    while i < x:                                    # while lus voor de lengte van de lijst af te gaan.
        while j < y:                                # while lus voor de hoogte van de lijst af te gaan.
            GEDRAAIDE_LIJST[j][i] = LIJST[i][j]     # Item dat op positie i, j staat in LIJST wordt op plaats j, i gezet
            j += 1                                  # in GEDRAAIDE_LIJST
        i += 1                                      # Er wordt 1 bijgeteld bij tellers i en j

    print_matrix(GEDRAAIDE_LIJST)                   # De lijst wordt geprint met de methode print_matrix


def turn_right():
    print("Moet nog ingevuld worden.")


def main():
    print_matrix(LIJST)

    print("Maak een kezue:")
    print("1. Draai linksom.")
    print("2. Draai rechtsom.")
    keuze = input()

    if keuze == 1:
        turn_left()
    elif keuze == 2:
        turn_right()


if __name__ == '__main__':
    main()
