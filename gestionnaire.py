from mes_fonction import *

class gestionnaire:

    contact = {}


    def __init__(self):
        self.contact = {}

    def affiche_menu(self):
        print("**************************************")
        print("Menu du gestionnaire :")
        print("0. Quitter")
        print("1. créer un contact")
        print("2. supprimer un contact")
        print("3. modifier un contact")
        print("4. afficher les noms")
        print ("5. rechercher un contact")
        return input("Votre choix : ")

    

    def creer(self):

        nom = input("donne ton nom wesh :").lower()
        
        contact_info = {
            'numero': input("Eettt madmoiselle t’as pas un 06? : "),
            'email': input("Ton email man steplai : "),
            'adresse': input("Et tu viens d'où ???? : ")
        }

        self.contact[nom] = contact_info
        return self.contact

    def modifier(self):

        if self.contact:
            print("\nvoici les contact")
            for nom in self.contact.keys():
                print(f"- {nom}\n")

            nom = input("quel contact veux tu modifier : ")
            parametre = input("que veux tu modifier : nom, numéro, email, adresse ? :")
            if nom in self.contact:
                if parametre == 'nom':
                    nouveau_nom = input("donne un nouveau nom")
                    self.contact[nouveau_nom] = self.contact.pop(nom)#tu utilise .pop pour modifier la kelys de ton dictionnaire
                    print(f"Le nom a été modifié de {nom} à {nouveau_nom}.")
                elif parametre == 'numéro':
                    nouveau_numero = input("donne un nouveau numéro: ")
                    self.contact[nom]['numéro'] = nouveau_numero
                    print(f"Le numéro de {nom} a été modifié.")
                elif parametre == 'email':
                    nouveau_email = input("donne une nouvelle adresse mail")
                    self.contact[nom]['email'] = nouveau_email
                    print(f"L'email de {nom} a été modifié.")
                elif parametre == 'adresse':
                    nouvelle_adresse = input("donne une nouvelle adresse")
                    self.contact[nom]['adresse'] = nouvelle_adresse
                    print(f"L'adresse de {nom} a été modifiée.")
                else:
                    print("paramètre non reconnue, aucune modification effectuée")
            else: 
                print("pas de contact de se nom")
        else:
            print("il n'y a aucun contact à modifier")

    def affichage(self):
        
        if self.contact:
            print("\nvoici les contact")
            for nom, info in self.contact.items():
                print(f"{nom}: {info['numero']}, {info['email']}, {info['adresse']}\n")
        else:
            print('pas de contact')


    def supprimer(self):

        if self.contact:
            print("\nvoici les contact")
            for nom in self.contact.keys():
                print(f"- {nom}\n")
        nom = (input("le quel ? :"))
        if nom in self.contact:
            del self.contact[nom]
            print(f"Le contact {nom} a été supprimé.")
        else:
            print("se contacte n'existe pas")

    def recherche(self,_nom):
        if _nom in self.contact.keys():
            for _nom, info in self.contact.items():
                print(f"{_nom}: {info['numero']}, {info['email']}, {info['adresse']}\n")
        else:
            print("le contact n'existe pas")

    def action(self):
        choix = self.affiche_menu()
        while choix != "0":
            match (choix):
                case "1":
                    self.creer()
                case "2":
                    self.supprimer()
                case "3":
                    self.modifier()
                case "4":
                    self.affichage()
                case "5":
                    nom = input("qui recherches tu ? : ")
                    self.recherche(nom)
            choix = self.affiche_menu()







































# def affiche_menu():
#     print("**************************************")
#     print("Menu du gestionnaire :")
#     print("0. Quitter")
#     print("1. créer un contact")
#     print("2. supprimer un contact")
#     print("3. modifier un contact")
#     print("4. afficher les noms")
#     return input("Votre choix : ")

# choix = affiche_menu()

# contact = {}


# def creer(contact):

#     nom = input("donne ton nom wesh :").lower()
    
#     contact_info = {
#         'numero': input("Eettt madmoiselle t’as pas un 06? : "),
#         'email': input("Ton email man steplai : "),
#         'adresse': input("Et tu viens d'où ???? : ")
#     }

#     contact[nom] = contact_info
#     return contact

# def modifier(contact):

#     if contact:
#         print("\nvoici les contact")
#         for nom in contact.keys():
#             print(f"- {nom}\n")

#         nom = input("quel contact veux tu modifier : ")
#         parametre = input("que veux tu modifier : nom, numéro, email, adresse ? :")
#         if nom in contact:
#             if parametre == 'nom':
#                 nouveau_nom = input("donne un nouveau nom")
#                 contact[nouveau_nom] = contact.pop(nom)#tu utilise .pop pour modifier la kelys de ton dictionnaire
#                 print(f"Le nom a été modifié de {nom} à {nouveau_nom}.")
#             elif parametre == 'numéro':
#                 nouveau_numero = input("donne un nouveau numéro: ")
#                 contact[nom]['numéro'] = nouveau_numero
#                 print(f"Le numéro de {nom} a été modifié.")
#             elif parametre == 'email':
#                 nouveau_email = input("donne une nouvelle adresse mail")
#                 contact[nom]['email'] = nouveau_email
#                 print(f"L'email de {nom} a été modifié.")
#             elif parametre == 'adresse':
#                 nouvelle_adresse = input("donne une nouvelle adresse")
#                 contact[nom]['adresse'] = nouvelle_adresse
#                 print(f"L'adresse de {nom} a été modifiée.")
#             else:
#                 print("paramètre non reconnue, aucune modification effectuée")
#         else: 
#             print("pas de contact de se nom")
#     else:
#         print("il n'y a aucun contact à modifier")

# def affichage(contact):
    
#     if contact:
#         print("\nvoici les contact :")
#         for nom, info in contact.items(): #nom viens afficher la kleys de ton premier tableau et info viens afficher se qui il y dans ta kleys numéro, email etc...
#             print(f"{nom}: {info['numero']}, {info['email']}, {info['adresse']}\n")
#     else:
#         print('pas de contact')


# def supprimer(contact):

#     if contact:
#         print("\nvoici les contact")
#         for nom in contact.keys():
#             print(f"- {nom}\n")
#     nom = (input("le quel ? :"))
#     if nom in contact:
#         del contact[nom]
#         print(f"Le contact {nom} a été supprimé.")
#     else:
#         print("se contacte n'existe pas")


# while choix != "0":
#     match (choix):
#         case "1":
#             creer(contact)
#         case "2":
#             supprimer(contact)
#         case "3":
#             modifier(contact)
#         case "4":
#             affichage(contact)
#     choix = affiche_menu()

# print("*** FIN DU PROGRAMME ***")