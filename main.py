from math import pi
from math import sqrt

# On demande à l’utilisateur la taille du sapin tant qu’il n’a pas entré un entier 
while True:
    try:
        taille_sapin = int(input("Quel est la taille de votre sapin en cm : "))
    except ValueError:
        print('Merci d’entrer la taille de votre sapin en cm sans décimal (nombre entier) !')
        continue
    else:
        break

# Calcul des différentes valeurs du sapin idéal
taille_guirlande_classique = round(13 * pi / 8 * taille_sapin)
if taille_guirlande_classique > 100:
    taille_guirlande_classique = taille_guirlande_classique / 100
    taille_guirlande_classique_mes = 'm'
else:
    taille_guirlande_classique_mes = 'cm'
    
taille_guirlande_lumineuse = round(3.14 * taille_sapin)
if taille_guirlande_lumineuse > 100:
    taille_guirlande_lumineuse = taille_guirlande_lumineuse / 100
    taille_guirlande_lumineuse_mes = 'm'
else:
    taille_guirlande_lumineuse_mes = 'cm'

nb_boules = round((sqrt(17) / 20) * taille_sapin)

diametre_etoile = round(taille_sapin / 10, 2)
if diametre_etoile > 100:
    diametre_etoile = diametre_etoile / 100
    diametre_etoile_mes = 'm'
else:
    diametre_etoile_mes = 'cm'

# Affichage des résultats
print(f'Pour réaliser un sapin idéal de {taille_sapin} cm, il vous faudra les éléments suivants :')
print(f' - Une guirlande classique de {taille_guirlande_classique} {taille_guirlande_classique_mes}')
print(f' - Une guirlande lumineuse de {taille_guirlande_lumineuse} {taille_guirlande_lumineuse_mes}')
print(f' - {nb_boules} boules')
print(f' - Une étoile de {diametre_etoile} {diametre_etoile_mes}')