############# IMPORT DE LA TOTALITE DU MODULE ##############

import math  # Import du module

a = math.gamma(16)  # Utilisation de la methode gamma du module math
print(a)

""" Pour 
la partie import
on pourrai aussi renommer le modules 
a notre convenance pour que son nom soit plus clair
comme ceci : 

import math as mathematique                IMPORTANT

par exemple
"""

############# IMPORT D'UNE METHODE DU MODULE ##############


from math import fabs
a = fabs(-6)
print(a)
"""
fabs() renvoi une valeur absolu

Importe uniquement la methode gamma dont nous
avons besoin

"""

from math import *
a = sqrt(36)
print(a)
b = fabs(-5)
print(b)


"""
* permet d'importer toute les methodes du module
en les placants dans l'espace de nom courant
cela permet d'appeller les methodes directement ->< methode()
au lieu de devoir appeller le nom du module avant -> math.method()
"""