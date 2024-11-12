import random

class calcul:
    
    def __init__(self):
        montant = int(input('Montant : '))
        remise = int(input('La remise : '))
        self.montant = montant
        self.remise = remise

    def calcul_remise(self):
        resultat = self.montant - self.montant * (self.remise/100)
        return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")
    

# def calcul_remise(_montant, _remise): 
#     # print(_montant)
#     # print(_remise)
#     resultat = _montant - _montant * (_remise/100)
#     return print("Le prix de l'article après la remise est de : " + str(resultat) + " €")

class lancer_de_de():

    def __init__(self):
        de = int(input("choisisé le nombre de face du dé: "))
        fois = int(input("choisissez le nombre de fois que vous voulez lancer le dé: "))
        self.de = de
        self.fois = fois

    def destin(self):
        i = 1
        while i <= self.fois:
            resultat = random.randint(0, self.de)
            print("le dé donne :" + str(resultat))
            i = i + 1
# def lancer_de_de(_mama):
#     resultat = random.randint(0, _mama)
#     return print("le dé donne : " + str(resultat))

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

def fin():
    i = "0"
    return i

class jeu_du_juste_prix():
    prix = 0
    juste_prix = 0
    def __init__(self):
        self.prix = int(input("donner un prix : "))
        self.juste_prix = random.randint(100,10000)

    def le_prix(self):
        while self.prix != self.juste_prix:
            if self.prix > self.juste_prix:
                print("c'est moins")
                self.prix = int(input("donner un nouveau prix : "))
            elif self.prix < self.juste_prix:
                print("c'est plus")
                self.prix = int(input("donner un nouveau prix : "))
        if self.prix == self.juste_prix:
            print("bravo toi avoir trouver prix juste de : " + str(self.juste_prix))

# def jeu_du_juste_prix():
#     prix = int(input("donner un prix : "))

#     juste_prix = random.randint(100,10000)

#     while prix != juste_prix:
#         if prix > juste_prix:
#             print("c'est moins")
#             prix = int(input("donner un nouveau prix : "))
#         elif prix < juste_prix:
#             print("c'est plus")
#             prix = int(input("donner un nouveau prix : "))
    

#     if prix == juste_prix:
#         print("bravo toi avoir trouver prix juste de : " + str(juste_prix))



# import time
# # Importer Tkinter
# from tkinter import *

# fenetre =Tk()                    #créer une fenêtre racine de l'interface
# fenetre.title("horloge digitale") #créer une fenêtre racine de l'interface

# #créer la variable horloge et tu met dedans label qui contruire la fenetre ou sera afficher l'horloge. label prend en argument
# #  fenetre qui est la variable ou sera l'horloge, se que tu vas afficher dans la fenetre ici texte et pour finir la largeur et hauteur
# horloge = Label(fenetre, text="demander l'heure", width=30, height=5)
# #horloge = Label(fenetre, text="Affichage de l'heure", width=30, height=5)

# #fonction qui met à jour l'heure
# def mise_a_jour():

#     heure = time.strftime("%H:%M:%S")         # crée une variable heure est met dans cette variable l'heure local actuet et va afficher l'heure la minute et les seconde
#     horloge.config(text=heure)         #avec cette ligne tu configure horloge en dissant que texte dans horloge est égale à la variable heure
#     horloge.after(1000, mise_a_jour)   #tu réaffiche horloge après 1 seconde

# #création de 2 bouton pour démarrer et quitter la fenêtre


# #1er façon de faire
# demarrer = Button(fenetre, text="demarrer", command=mise_a_jour)  #tu créer la variable bouton et tu met de dans la fonction bouton de tkinter et en argument présise ou sera le bouton (dans fenetre), le texte dans le bouton et se qui se passe quand tu clique dessus

# quitter = Button(fenetre, text="quitter", command=fenetre.destroy)


# # Affichage du label et des boutons dans la fenêtre

# horloge.grid(row=0, column=0, columnspan=2)
# demarrer.grid(row=1, column=0)
# quitter.grid(row=1, column=1)


# fenetre.mainloop()