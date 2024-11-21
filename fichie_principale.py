# from mon-document_qui_stock import les élément que je souhaite utiliser
from mes_fonction import *
from horloge_numérique import horloge
from pendu import jeupendu
from Cesar import codeur
from gestionnaire import gestionnaire

class miniapp():

    choix = ''
    rep = ''

    def affiche_menu(self):
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


    def decision(self):

        self.choix = self.affiche_menu()
        while self.choix != "0":
            match (self.choix):
                case "1":
                    resultat = calcul()
                    resultat.calcul_remise()
                case "2":
                    resultat = lancer_de_de()
                    resultat.destin()
                    
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
                    jeux.decision()
                case "7":
                    contact = gestionnaire()
                    contact.action()

            self.rep = (input("veux tu revenir au menu ? oui ou non : "))

            if self.rep == "oui":
                self.choix = self.affiche_menu()
            elif self.rep == "non":
                self.choix = fin()
            print("*** FIN DU PROGRAMME ***")    