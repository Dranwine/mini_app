# from mon-document_qui_stock import les élément que je souhaite utiliser
from mes_fonction import *
from horloge_numérique import mise_a_jour
from pendu import jeux_du_pendu
from Cesar import codeur_cesar


choix = affiche_menu()

while choix != "0":
    match (choix):
        case "1":
            montant = int(input('Montant : '))
            remise = int(input('La remise : '))
            calcul_remise(montant, remise)
        case "2":
            mama = int(input("choisisé le nombre de face du dé: "))
            lancer_de_de(mama)
            # print("Lancé de dé ...") # Choix du nb de faces par l'utilisateur
        case "3":
            jeu_du_juste_prix()
        case "4":
            mise_a_jour()
        case "5":
            jeux_du_pendu()
        case "6":
            codeur_cesar()
        case "7":
            print("Lancement du Gestionnaire de contact ...")
    
    rep = (input("veux tu revenir au menu ? oui ou non : "))

    if rep == "oui":
       choix = affiche_menu()
    elif rep == "non":
     print("*** FIN DU PROGRAMME ***")
     choix = fin()