# !/usr/bin/env python

"""
            ／￣￣￣￣￣￣￣￣
　　　　　　  |　Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
　　　　　　  |　De lijst mag je kiezen:
　　　　　　  |　  1. ofwel uit een bestand lezen
　　　　　　  |　  2. ofwel zelf een lijst samenstellen in je script
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
from random import choice

# CONFIG
KAZEN = ["Gouda", "Brie", "Mozzarella", "Emmental", "Feta", "Cheddar"]   # Lijst van een aantal kazen

# AUTHOR INFORMATION
__author__ = "Tibo Smet"
__email__ = "tibo.smet@student.kdg.be"
__status__ = "Development"


def main():
    for kaas in KAZEN:                                                  # Overloopt alle kazen in de lijst
        print(kaas, end="     ")                                        # Print alle kazen in de lijst
    print("")
    print("")

    willekeurige_kaas = choice(KAZEN)                                   # Kiest een willekeurige kaas uit de lijst
    print("Raad de kaas die willekeurig uit de lijst werd gekozen.")
    keuze = input()                                                     # Vraagt de gebruiker om een kaas te raden

    if keuze == willekeurige_kaas:                                      # Controlleerd of de keuze van de gebruiker correct is
        print("Gefeliciteerd! Je rade de juiste kaas, ", willekeurige_kaas)
    else:
        print("Jammer je antwoord was fout. Het antwoord was", willekeurige_kaas, "probeer opnieuw.")


if __name__ == '__main__':
    main()
