while True:
    try:
        taille_sapin = int(input("Quel est la taille de votre sapin en cm : "))
    except ValueError:
        print('Merci d’entrer la taille de votre sapin en cm sans décimal (nombre entier) !')
        continue
    else:
        break

taille_guirlande_classique = round(13 * 3.14 / 8 * taille_sapin)
taille_guirlande_lumineuse = round(3.14 * taille_sapin)
nb_boules = round((17**0.5 / 20) * taille_sapin)
diametre_etoile = round(taille_sapin / 10, 2)

print(f'Pour réaliser un sapin idéal de {taille_sapin} cm, il vous faudra les éléments suivants :')
print(f' - Une guirlande classique de {taille_guirlande_classique} cm')
print(f' - Une guirlande lumineuse de {taille_guirlande_lumineuse} cm')
print(f' - {nb_boules} boules')
print(f' - Une étoile de {diametre_etoile} cm')