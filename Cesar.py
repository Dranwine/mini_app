def codeur_cesar():

# faire une liste contenant l'alphabet
    liste = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#doubler la liste pour que ne par sortir de la liste quand on appel z
    for x in range(len(liste)):
        liste.append(liste[x])

    message = input("enter ici votre message à chiffrer : ")  
    clef = int(input("donne votre clef de chiffrement de 26 ou moins :")) 

    def chiffrement(liste, clef, lettre): # crée un programe en parametre liste(alphabet), clef de criptage et lettre(la variable qui parcour message caractère par caractère)
        for i in range(len(liste)): #pour variable i dans la liste de la première variable à la dernière
            if liste[i] == lettre: # si liste de i est égale à lettre(variable qui parcour le message)
                return str(liste[i+clef]) #tu retournes la variable qui est i à se moment plus la clef
            elif liste[i] == ' ': # si i est une ' '
                return ' ' #retourne ' '
        return '?' #pour tous caractère qui ne sont pas une lettre dans la liste ou un espace

    message_chiffré = str() #message chiffrer en str 

    for lettre in message:
        message_chiffré += chiffrement(liste, clef, lettre) #pour la variable lettre qui parcour le message de l'utilisateur

    print(message_chiffré)