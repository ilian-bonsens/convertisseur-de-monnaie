from forex_python.converter import CurrencyRates, RatesNotAvailableError
import datetime
historique = ""

def convertisseur():
    global historique 
    taux = CurrencyRates()
    while True:
        try:
            entree = input("Entrez la devise à convertir : ").upper()
            sortie = input("Entrez la devise de conversion : ").upper()
            taux_de_change = taux.get_rate(entree, sortie)
            montant = int(input("Montant à convertir : "))
            resultat = taux.convert(entree, sortie, montant)
            print(f"{resultat:.2f}")
            historique += f"{montant:.2f} {entree} en {resultat:.2f} {sortie}\n"
        except RatesNotAvailableError:
            print("Erreur : entrez un code de devise valide.")
        except ValueError:
                print("Erreur : entrez un montant valide.")
        with open('historique_des_conversions.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()}: Converti {montant:.2f} {entree} en {resultat:.2f} {sortie}. Le taux de conversion est : {taux_de_change:.2f}.\n")

convertisseur()