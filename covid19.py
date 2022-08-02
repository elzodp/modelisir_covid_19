import matplotlib.pyplot as plt
import numpy as np
import datetime


def calcul_s(i, b, s, p):
    snew = ((-b * s * i) / p) + s

    return snew


def calcul_i(i, b, s, I, p):
    inew = (((b * s * i) / p) - ((1/I)*i)) + i

    return inew


def calcul_r(i, I, r):
    rnew = ((1/I)*i) + r

    return rnew


# Déclaration des variables de depart
i = int(input("Veillez entrer le nombre d'infectés initiale "))
r = int(input("Veillez entre le nombre de rétablies initial "))
p = int(input("Veillez entrer la population totale "))
s = p - r - i


beta = float(input("Veillez entrer le taux de transmission "))
lamb = float(input("Veillez entrer la durée moyenne d'infection en jour "))
tmax = int(input("Veillez entrer la durée en jour maximum de l'étude "))


# Déclaration des tableaux contenant le nombre de sains, infectés, rétablis, au cours du temps

tab_s = []
tab_i = []
tab_r = []

# Calcul de S(t), I(t), R(t) et ajout dans le tableau

for t in range(0, tmax):
    # On ajoute les valeurs de s, i et r
    tab_s.append(s)
    tab_i.append(i)
    tab_r.append(r)


# On calcule grace aux fonctions fonction 1, fonction 2 et fonction 3, les nouvelles valeures de s,i et r à t+1

    s = calcul_s(i, beta, s, p)
    i = calcul_i(i, beta, s, lamb, p)
    r = calcul_r(i, lamb, r)

# On trace les courbes

# On définit les valeurs de t pour toutes les courbes

t = np.array(range(0, tmax))

# On définit la suite de valeur en y pour chacune des courbes

ys = np.array(tab_s)
yi = np.array(tab_i)
yr = np.array(tab_r)

# On ajoute les trois courbes
plt.plot(t, ys, label="Sains")
plt.plot(t, yi, label="Infectés")
plt.plot(t, yr, label="Rétablis")

plt.legend()

# On ajoute un titre et un label aux axes

plt.title("Modèle S.I.R")
plt.xlabel("Jours")
plt.ylabel("Taux")

# On crée le nom du fichier et on sauvegarde notre courbe dans une image .png

nom = "SIR"+str(datetime.datetime.now())+".png"
plt.savefig(nom)
plt.close()
