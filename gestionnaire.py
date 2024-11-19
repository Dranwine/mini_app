from mes_fonction import *


def affiche_menu():
    print("**************************************")
    print("Menu du gestionnaire :")
    print("0. Quitter")
    print("1. créer un contact")
    print("2. supprimer un contact")
    print("3. modifier un contact")
    print("4. afficher les noms)")
    return input("Votre choix : ")

choix = affiche_menu()

contact = {}


def creer(contact):

    nom = input("donne ton nom wesh :").lower()
    
    contact_info = {
        'numero': input("Eettt madmoiselle t’as pas un 06? : "),
        'email': input("Ton email man steplai : "),
        'adresse': input("Et tu viens d'où ???? : ")
    }

    contact[nom] = contact_info
    return contact, nom

def modifier(contact):

    if contact:
        print("\nvoici les contact")
        for nom in contact.keys():
            print(f"- {nom}\n")

        nom = input("quel contact veux tu modifier : ")
        parametre = input("que veux tu modifier : nom, numéro, email, adresse ? :")
        if nom in contact:
            if parametre == 'nom':
                nouveau_nom = input("donne un nouveau nom")
                contact[nouveau_nom] = contact.pop(nom)#tu utilise .pop pour modifier la kelys de ton dictionnaire
                print(f"Le nom a été modifié de {nom} à {nouveau_nom}.")
            elif parametre == 'numéro':
                nouveau_numero = input("donne un nouveau numéro: ")
                contact[nom]['numéro'] = nouveau_numero
                print(f"Le numéro de {nom} a été modifié.")
            elif parametre == 'email':
                nouveau_email = input("donne une nouvelle adresse mail")
                contact[nom]['email'] = nouveau_email
                print(f"L'email de {nom} a été modifié.")
            elif parametre == 'adresse':
                nouvelle_adresse = input("donne une nouvelle adresse")
                contact[nom]['adresse'] = nouvelle_adresse
                print(f"L'adresse de {nom} a été modifiée.")
            else:
                print("paramètre non reconnue, aucune modification effectuée")
        else: 
            print("pas de contact de se nom")
    else:
        print("il n'y a aucun contact à modifier")

def affichage(contact):
    
    if contact:
        print("\nvoici les contact")
        for nom, info in contact.items():
            print(f"{nom}: {info['numero']}, {info['email']}, {info['adresse']}\n")
    else:
        print('pas de contact')


def supprimer(contact):

    if contact:
        print("\nvoici les contact")
        for nom in contact.keys():
            print(f"- {nom}\n")
    nom = (input("le quel ? :"))
    if nom in contact:
        del contact[nom]
        print(f"Le contact {nom} a été supprimé.")
    else:
        print("se contacte n'existe pas")


while choix != "0":
    match (choix):
        case "1":
            creer(contact)
        case "2":
            supprimer(contact)
        case "3":
            modifier(contact)
        case "4":
            affichage(contact)
    choix = affiche_menu()

print("*** FIN DU PROGRAMME ***")