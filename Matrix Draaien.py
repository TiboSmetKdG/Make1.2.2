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
LIST = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']]


# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def print_array(m):
    for line in m:                                  # de matrix zal overlopen worden voor elke regel die hij bevat
        for item in line:                           # de regel zal overlopen worden voor elk item dat het bevat
            print(item, end="")                     # print elk item van de regel op 1 lijn
        print("")                                   # zorgt voor een nieuwe lijn


def turn_left():
    global LIST
    rotated_list = []

    x = len(LIST[0])
    y = len(LIST)

    for i in range(y):
        rotated_list.append([])
        for j in range(x):
            rotated_list[-1].append(LIST[j][i])

    return rotated_list


def turn_right():
    global LIST
    rotated_list = []

    x = len(LIST[0])
    y = len(LIST)

    for i in range(x):
        rotated_list.append([])
        for j in range(y):
            rotated_list[-1].append(LIST[j][i])

    return rotated_list


def main():
    print_array(LIST)

    print("Maak een kezue:")
    print("1. Draai linksom.")
    print("2. Draai rechtsom.")
    keuze = input()

    if keuze == "1":
        print_array(turn_left())
    elif keuze == "2":
        print_array(turn_right())


if __name__ == '__main__':
    main()
