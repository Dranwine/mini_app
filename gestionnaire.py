#faire un gestionnaire de contact

# def gestionnaire_de_contact():

contact = {}


def creer(contact):

    nom = input("donne ton nom wesh :")
    
    contact_info = {
        'numero': input("Eettt madmoiselle t’as pas un 06? : "),
        'email': input("Ton email man steplai : "),
        'adresse': input("Et tu viens d'où ???? : ")
    }

    contact[nom] = contact_info
    return contact


contact = creer(contact)  
print(contact)
# for nom, infos in contacts.items():
#     print(f"Nom: {nom}")
#     print(f"  Numéro: {infos['numero']}")
#     print(f"  Email: {infos['email']}")
#     print(f"  Adresse: {infos['adresse']}")
#     print()  # Ligne vide pour séparer les contacts


# def suprimer():


# def chercher(contact):

#     clef = input("donne un nom : ")
#     for clef in contact.keys():
#         print(clef)