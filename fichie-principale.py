# from mon-document_qui_stock import les élément que je souhaite utiliser
from mes_fonction import *
from horloge_numérique import horloge
from pendu import jeupendu
from Cesar import codeur


choix = affiche_menu()

while choix != "0":
    match (choix):
        case "1":
            resultat = calcul()
            resultat.calcul_remise()
        case "2":
            resultat = lancer_de_de()
            resultat.destin()
            # print("Lancé de dé ...") # Choix du nb de faces par l'utilisateur
        case "3":
            resultat = jeu_du_juste_prix()
            resultat.le_prix()
        case "4":
            heure = horloge()
            heure.mise_a_jour()
        case "5":
            jeux = jeupendu()
            jeux.jeux_du_pendu()
        case "6":
            jeux = codeur()
            jeux.affichage()
        case "7":
            print("Lancement du Gestionnaire de contact ...")
    
    rep = (input("veux tu revenir au menu ? oui ou non : "))

    if rep == "oui":
       choix = affiche_menu()
    elif rep == "non":
     print("*** FIN DU PROGRAMME ***")
     choix = fin()