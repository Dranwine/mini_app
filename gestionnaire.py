from mes_fonction import *
#faire un gestionnaire de contact

# def gestionnaire_de_contact():

contact = {}


def creer(contact):

    nom = input("donne ton nom wesh :").lower
    
    contact_info = {
        'numero': input("Eettt madmoiselle t’as pas un 06? : "),
        'email': input("Ton email man steplai : "),
        'adresse': input("Et tu viens d'où ???? : ")
    }

    contact[nom] = contact_info
    return contact, nom

def affichage():  
    for nom, infos in contact.items():
        print(f"Nom : {nom}")
        print(f"Numéro : {infos['numero']}")
        print(f"Email : {infos['email']}")
        print(f"Adresse : {infos['adresse']}")

def supprimer(contact):
    reponse = (input("veux tu suprimer un contact, oui ou non ?")).lower()
    while reponse != 'oui' or reponse != 'non':
        reponse = (input("veux tu suprimer un contact, oui ou non ?")).lower()
    if reponse == 'oui':
        nom = (input("le quel ? :"))
        if nom in contact:
            del contact[nom]
        else:
            print("se contacte n'existe pas")
    else:
        print('aucun contact supprimer')

contact, _ = creer(contact)


# rep = (input("veux tu créer un autre contact, oui ou non ?"))

# if rep == "oui":
#     choix = creer(contact)
#     affichage()
# elif rep == "non":
#     print("*** FIN DU PROGRAMME ***")
#     choix = fin()

rep = (input("veux tu suprimer un  contact, oui ou non ?"))

if rep == "oui":
    choix = supprimer(contact)
    affichage()
elif rep == "non":
    print("*** FIN DU PROGRAMME ***")
    choix = fin()



# for nom, infos in contacts.items():
#     print(f"Nom: {nom}")
#     print(f"  Numéro: {infos['numero']}")
#     print(f"  Email: {infos['email']}")
#     print(f"  Adresse: {infos['adresse']}")
#     print()  # Ligne vide pour séparer les contacts





# def chercher(contact):

#     reponse = input("donne un nom : ").lower()
#     if reponse in contact:
#         print(f"contact trouver : {reponse}")
#         print(contact[reponse])