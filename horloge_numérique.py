import time
from tkinter import *
import os
import tkinter

# # 4.afficher une Horloge numérique (HH:MM:SS qui défile)


# fenetre = Tk()
# fenetre.title('Horloge Digitale')

# t = time.strftime("%H:%M:%S")
# t2 = time.strftime("%H:%M:%S")

# print(t)

# import time
# import Tkinter
# from tkinter import *

# def mise_a_jour():
    
#     fenetre =Tk()                    #créer une fenêtre racine de l'interface
#     fenetre.title("horloge digitale") #créer une fenêtre racine de l'interface

# #créer la variable horloge et tu met dedans label qui contruire la fenetre ou sera afficher l'horloge. label prend en argument
# #  fenetre qui est la variable ou sera l'horloge, se que tu vas afficher dans la fenetre ici texte et pour finir la largeur et hauteur
#     horloge = Label(fenetre, text="demander l'heure", width=30, height=5)
# #horloge = Label(fenetre, text="Affichage de l'heure", width=30, height=5)

# #fonction qui met à jour l'heure
#     def mise_a_jourr():

#         heure = time.strftime("%H:%M:%S")         # crée une variable heure est met dans cette variable l'heure local actuet et va afficher l'heure la minute et les seconde
#         horloge.config(text=heure)         #avec cette ligne tu configure horloge en dissant que texte dans horloge est égale à la variable heure
#         horloge.after(1000, mise_a_jourr)   #tu réaffiche horloge après 1 seconde

# #création de 2 bouton pour démarrer et quitter la fenêtre


# #1er façon de faire
#     demarrer = Button(fenetre, text="demarrer", command=mise_a_jourr)  #tu créer la variable bouton et tu met de dans la fonction bouton de tkinter et en argument présise ou sera le bouton (dans fenetre), le texte dans le bouton et se qui se passe quand tu clique dessus

#     quitter = Button(fenetre, text="quitter", command=fenetre.destroy)


# # Affichage du label et des boutons dans la fenêtre

#     horloge.grid(row=0, column=0, columnspan=2)
#     demarrer.grid(row=1, column=0)
#     quitter.grid(row=1, column=1)


#     fenetre.mainloop()



def mise_a_jour():

     rep = 0
    
     while rep != 10:
         heure = time.strftime("%H:%M:%S")
         print(heure)
         time.sleep(1)
         rep = rep +1
         os.system('cls' if os.name == 'nt' else 'clear')
