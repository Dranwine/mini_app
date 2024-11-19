import random

# class jeux_du_pendu():

#     liste_mots = []
#     mot = ''
#     mot_user = []
#     stock = []
#     rep_if = 0

#     def __init__(self):

#         self.liste_mots = ["tocard","bruno","bonjour", "salsifis"]


#     def jeux_du_pendu(liste_mots,mot_user):



#         mot = random.choice(liste_mots) #choisir un mot au hazard dans ma liste
#         print(mot)

#         while len(mot_user) != len(mot): 
#             mot_user.append("-") 

#         while mot_user != list(mot):
#             print("".join(mot_user))
#             if rep_if == 0:
#                 lettre = str(input("vassy la donne une lettre toi la : "))
#             stock = mot_user.copy()
#             i = 0
#             rep_if = 0
#             print (stock)
#             while i <= len(mot)-1:
#                 if lettre == mot[i]:
#                     mot_user[i] = mot[i]
#                 i = i + 1
#             i = 0
#             print(stock)
#             if stock == mot_user:
#                 print("".join(mot_user))
#                 lettre = input("vassy la ta lettre et pa dedans donne autre lettre : ")
#                 rep_if = 1
#         print("bravo la ta trouver le mot", mot)















# def jeux_du_pendu():


#     liste_mots = ["tocard","bruno","bonjour", "salsifis"] #je défini un tableau avec les mot que l'utilisateur doit deviner


#     mot = random.choice(liste_mots) #choisir un mot au hazard dans ma liste
#     mot_user = []
#     stock = []
#     rep_if = 0
#     print(mot)

#     while len(mot_user) != len(mot): #tant que que la longeur de la liste mot_user et différente de la liste mot
#         mot_user.append("-") #remplir chaque possition de mot_user avec des "-"

#     while mot_user != list(mot):
#         print("".join(mot_user))
#         if rep_if == 0:
#             lettre = str(input("vassy la donne une lettre toi la : "))
#         stock = mot_user.copy()
#         i = 0
#         rep_if = 0
#         print (stock)
#         while i <= len(mot)-1:
#             if lettre == mot[i]:
#                 mot_user[i] = mot[i]
#             i = i + 1
#         i = 0
#         print(stock)
#         if stock == mot_user:
#             print("".join(mot_user))
#             lettre = input("vassy la ta lettre et pa dedans donne autre lettre : ")
#             rep_if = 1
#     print("bravo la ta trouver le mot", mot)



# Initialisation de la liste des mots
liste_mots = ["tocard", "bruno", "bonjour", "salsifis"]
mot = random.choice(liste_mots)  # Choisir un mot au hasard dans la liste
mot_user = ["-"] * len(mot)  # Initialisation du mot deviné avec des tirets
print("Mot à deviner :", mot)

# Boucle principale pour demander des lettres jusqu'à ce que le mot soit trouvé
while mot_user != list(mot):
    print("".join(mot_user))
    lettre = input("Vas-y, donne une lettre : ")
    lettre_trouvee = False  # Drapeau pour savoir si la lettre est trouvée

    # Vérification de chaque lettre dans le mot
    for i in range(len(mot)):
        if lettre == mot[i]:
            mot_user[i] = mot[i]
            lettre_trouvee = True  # Marquer la lettre comme trouvée

    # Si la lettre n'est pas trouvée dans le mot
    if not lettre_trouvee:
        print("Cette lettre n'est pas dans le mot, essaie encore.")

# Afficher le mot final quand il est deviné
print("Bravo, tu as trouvé le mot :", mot)