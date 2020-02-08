#!/usr/bin/python3
# -*-coding:UTF-8 -*

# OUVRIR UN FICHIER -> open():
## Mode d'ouverture : r-> Read ; w-> Write(ecrase le fichier) ; a-> Append
# ( mode ajout sans ecraser le fichier)


monFichier = open("/opt/lampp/htdocs/coursPython/fichiers.py", "r")
print(monFichier)
print(type(monFichier))
monFichier.close()

## Lire l'integralite du fichier -> read() :

# monFichier = open("fichiers.py", "r")
# contenu = monFichier.read()
# print(contenu)
# monFichier.close()

## Ecrire dans un fichier w ou a :
# La méthodewriten'accepte en paramètre que des chaînes de caractères.
# Si vous voulez écrire dans votre fichier des nombres, des scores par
# exemple, il vous faudra les convertir en chaîne avant de les écrire et
# les convertir en entier après les avoir lus.

monFichierTest = open("/opt/lampp/htdocs/coursPython/monFichierTest.py", "w")
monFichierTest.write("Premier test d'ecriture dans un fichier avec write")
monFichierTest.close()
monFichierTest = open("/opt/lampp/htdocs/coursPython/monFichierTest.py", "r")
contenuLecture = monFichierTest.read()
print(contenuLecture)
monFichierTest.close()

# LE MOT CLE WITH : with open(monFichier, modeOuverture) as variable:
                        # Operation sur le fichier ...
                        # Fermeture automatique du fichier, plus besoin
                        # de fichier.close()

with open("monFichierTest.py", "r") as alias:
    texte = alias.read()
    print(texte)
    # Fermeture fichier auto !

# ENREGISTRER DES OBJETS DANS DES FICHIERS avec "Pickle" :

import pickle

# Creation de notre objet : pickle.Pickler()
with open("/opt/lampp/htdocs/coursPython/donnees", "wb") as fichier:
    monPickler = pickle.Pickler(fichier)

score = {
  "joueur 1":    5,
  "joueur 2":   35,
  "joueur 3":   20,
  "joueur 4":    2,
}
# Pour créer notre objetPickler, nous allons l'appeler en passant en
# paramètre le fichier dans lequel nous allons enregistrer notre objet.
# Utilisation de la methode dump() du pickler pour enregistrer l'objet
with open('donnees', 'wb') as fichier:
    mon_pickler = pickle.Pickler(fichier)
    mon_pickler.dump(score)

# RECUPERER NOS OBJETS ENREGISTRES : pickle.Unpickler() + Methode : load()

with open("donnees", "rb") as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    # Lecture des objets contenus dans le fichier
    score_recupere = mon_depickler.load()
    print(score_recupere)

# Remarque : Pour lire l'objet dans notre fichier, il faut appeler la
# méthode load de notre depickler. Elle renvoie le premier objet qui a été
# lu (s'il y en a plusieurs, il faut l'appeler plusieurs fois). !!!
