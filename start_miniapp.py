# python c:/Users/Bukowski/Desktop/Python-algo/Mini_app/start_miniapp.py
def affiche_menu():
    print("**************************************")
    print("Menu de l'application :")
    print("0. Quitter")
    print("1. Calculer une remise en %")
    print("2. Lancé de dé")
    print("3. Jeu du juste prix")
    print("4. Horloge numérique (HH:MM:SS qui défile)")
    print("5. Jeu du pendu")
    print("6. Décodeur César")
    print("7. Gestionnaire de contact")
    print("**************************************")
    return input("Votre choix : ")

def calcul_remise(_montant, _remise): 
    # print(_montant)
    # print(_remise)
    resultat = _montant - _montant * (_remise/100)
    return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

choix = affiche_menu()

while choix != "0":
    match (choix):
        case "1":
            montant = int(input('Montant : '))
            remise = int(input('La remise : '))
            calcul_remise(montant, remise)
        case "2":
            print("Lancé de dé ...") # Choix du nb de faces par l'utilisateur
        case "3":
            print("Lancement du juste prix ...")
        case "4":
            print("Lancement de l'horloge numérique ...")
        case "5":
            print("Lancement du Jeu du pendu ...")
        case "6":
            print("Lancement du Décodeur César ...")
        case "7":
            print("Lancement du Gestionnaire de contact ...")
    
    choix = affiche_menu()

print("*** FIN DU PROGRAMME ***")