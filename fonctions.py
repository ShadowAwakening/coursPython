def table(nb, max):
    i = 0
    while i < max:  # Tant que i est strictement inférieure à la variable max,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1


print(table(11, 25))


def carre(valeur):
    return valeur * valeur


variable = carre(5)
print(variable)


############### FONCTION LAMBDA ##################3

f = lambda x, y: x + y
l = lambda x: x * x

print(f(2,3))
print(l(2))