# a = 0
#
# if a > 0:
#     print('a est superieur a 0')
# elif a < 0:
#     print('a est inferieur a 0')
# else:
#     print('a est egale a 0')



# Tp1 : l'anne est elle bissextile ?


# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")

    
# annee = input ("Saisissez une annee :")
# annee = int(annee)
#
# if annee % 4 != 0:
#     print("l'annee n'est pas B")
# elif annee % 4 == 0 and annee % 100 == 0:
#     if annee % 400 == 0:
#         print("Annee B")
#     else:
#         print("Annee NON B")
# else:
#     print("Annee B")



############## AUTRE METHODE #########################

# Programme testant si une année, saisie par l'utilisateur,
# est bissextile ou non

# annee = input("Saisissez une année : ") # On attend que l'utilisateur saisisse l'année qu'il désire tester
# annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
# bissextile = False # On crée un booléen qui vaut vrai ou faux
#                    # selon que l'année est bissextile ou non
#
# if annee % 400 == 0:
#     bissextile = True
# elif annee % 100 == 0:
#     bissextile = False
# elif annee % 4 == 0:
#     bissextile = True
# else:
#     bissextile = False
#
# if bissextile: # Si l'année est bissextile
#     print("L'année saisie est bissextile.")
# else:
#     print("L'année saisie n'est pas bissextile.")