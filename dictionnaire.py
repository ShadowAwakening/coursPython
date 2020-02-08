#!/usr/bin/python3
# -*-coding:UTF-8 -*

############################################
################   DICTIONNAIRES     ########
#############################################

# Creer un dictionnaire vide :

dictionnaire1 = dict()
print(dictionnaire1)

dictionnaire2 = {}
print(dictionnaire2)

# Ajouter des valeurs au dictionnaire :

dictionnaire3 = {}
dictionnaire3["pseudo"] = "Shadow"
dictionnaire3["mot de passe"] = "**"
print(dictionnaire3)

# remplacement de la valeur pour la cle "pseudo" :

dictionnaire3["pseudo"] = "Hadrin"
print(dictionnaire3)

# Acceder a la valeur d'une cle precise :

print(dictionnaire3["mot de passe"])
print(dictionnaire3["pseudo"])
## Si la cle n'existe pas dans le dictionnaire,
# une exception de type KeyError est levee.
# !! Remarque : on peut utilise presque tout les types
# cle et absolument tout les types comme valeurs !!

# On peut aussi utilise des entiers comme cle :

dictionnaire4 = {}
dictionnaire4[0] = "a"
dictionnaire4[1] = "b"
dictionnaire4[2] = "c"
dictionnaire4[3] = "d"

print(dictionnaire4)

# Creation d'un echiquier ou les cle sont des tuples
# contenant la lettre et le chiffre identifiant de la
# auxquelles on associe comme valeurs le nom des pieces

echiquier = {}
# Ici on sous entend les tuples et Python les comprends
# On aurai pu ecrire : [('a', 1)] - explicite les tuples
echiquier['a', 1] = "tour blanche"
echiquier['b', 1] = "cavalier blanc"
echiquier['c', 1] = "fou blanc"
echiquier['d', 1] = "reine blanche"
echiquier['e', 1] = "roi blanc"
echiquier['f', 1] = "fou blanc"
echiquier['g', 1] = "cavalier blanc"
echiquier['h', 1] = "tour blanche"

print(echiquier)

# Creer un dictionnaire prerempli (a l'instanciation)

dictionnaire5 = {"chemise": 5, "pantalon": 6}
print(dictionnaire5)

# Supprimer un dictionnaire : del ou pop()
# En plus de supprimer la cle et la valeur associee
# pop() renvoie cette valeur. Peut etre utile...

dictionnaire6 = {"chaussures": 12, "casquettes": 8}
print(dictionnaire6)
# supression cle/valeur avec del
del dictionnaire6["chaussures"]
print(dictionnaire6)
# supression cle/valeur avec pop()
dictionnaire6.pop("casquettes")
print(dictionnaire6)


# Utilisation des dictionnaires pour stocker des fonctions :

def fete():
    print("C'est la fête.")


def oiseau():
    print("Fais comme l'oiseau...")


fonctions = {}
fonctions["fete"] = fete  # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]()  # on essaye de l'appeler

# LES METHODES DE PARCOURS :

# Parcours des cles :

fruits = {"pomme": 4, "banane": 8, "poire": 3}
for cle in fruits:
    print(cle)

# Parcours des cles avec la methode de class key():

for cle in fruits.keys():
    print(cle)

# Parcours des valeurs:

# Parcourir les valeurs avec la methode value():

for valeur in fruits.values():
    print(valeur)

# Utilisation dans une condition:

if 8 in fruits.values():
    print("Un des fruits a comme quantite 21")

# Parcourir les cles et valeurs simultanement:

## Pour avoir en même temps les indices et les objets
# d'une liste, on utilise la fonction enumerate, j'espère
# que vous vous en souvenez. Pour faire de même avec les
# dictionnaires, on utilise la méthode items. Elle renvoie
# une liste, contenant les couples clé : valeur, sous la
# forme d'un tuple.

for cle, valeur in fruits.items():
    print("La cle {} contient la valeur {}".format(cle, valeur))


# DICTIONNAIRES ET PARAMETRES DE FONCTIONS :
## Recuperer les parametres nommes dans un dictionnaire

def fonction_inconnue(**parametres_nommes):  ## Pour capturer tous les
    # parametres nommes non precises dans un dictionnaire , il faut lui mettre
    # 2 etoiles ** avant le nom du parametre
    print("J'ai recus en parametres nommes : {}".format(parametres_nommes))


print(fonction_inconnue())  # Aucun parametres

fonction_inconnue(p=4, d=8)


# Si on passe des parametres non nommes a cette fonction
# Python levera une erreur. Pour pallier a cela, il faut avoir
# une fonction quui accepte nimporte quel tpe de parametres
# nommes ou non :

def fonction_inconnu_complete(*en_liste, **en_dictionnaire):
    print(
        "J'ai recus les parametres : {}, {}".format(en_liste, en_dictionnaire))


fonction_inconnu_complete()
# Ainsi tous les parametres non nommes se retrouveront dans la variable
# en_liste et tous les parametres nommes se retrouverons
# dans la variable en_dictionnaire


# Transformer un dictionnaire en parametres nommes d'une fonction

parametres = {"sep": " >> ", "end": " -\n"}
print("Voici", "un", "exemple", "d'appel", **parametres)
