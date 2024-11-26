import tkinter as tk
import random

fenetre = tk.Tk()
fenetre.title("Grille de Mots Mêlés")



quel_mot = input("quelle type de mots ? 1 : tous les mots / 2 : animaux / 3 : mot commun : ")

if quel_mot == "1":
    # Charger les mots depuis le fichier .txt dans une liste (comme expliqué précédemment)
    with open('dict.txt', 'r') as file:
        mots = [mot.strip() for mot in file.readlines()]

elif quel_mot == "2":
    # Lire le contenu du fichier texte
    with open('animaux.txt', 'r') as file:
        contenu = file.read()

    # Diviser le contenu en mots
    mots = contenu.split('\n')

    # Filtrer les animaux en plusieurs mots (avec espace)
    mots = [mot for mot in mots if ' ' not in mot]

    mots = [mot.upper() for mot in mots]

elif quel_mot == "3":
    # Charger les mots français à partir du fichier dict.txt
    with open('dict.txt', 'r', encoding='utf-8') as dict_file:
        mots_francais = set(dict_file.read().split())

    # Charger l'autre liste à partir du fichier mots_comun.txt
    with open('mots_comun.txt', 'r', encoding='utf-8') as mots_comun_file:
        mots_comun = mots_comun_file.read().replace('\n', ' ').split()

    print(mots_comun)
    # Créer une nouvelle liste pour stocker les mots présents dans la liste des mots français
    mots_valides = []

    # Vérifier l'appartenance et ajouter à la nouvelle liste
    for groupe in mots_comun:
        chiffre = False

        for cara in groupe:
            if cara in "1234567890":
                chiffre = True
                break

        if not chiffre:
            groupe_maj = groupe.upper()

        if groupe_maj in mots_francais:
            mots_valides.append(groupe_maj)

    mots = set(mots_valides)



nombre_mot = int(input("nombre de mot(s) ?"))

# Filtrer les mots avec plus de 6 lettres
mots_plus_de_six_lettres = [mot for mot in mots if len(mot) > 4]

# Choisir aléatoirement 10 mots
liste_mot = random.sample(mots_plus_de_six_lettres, nombre_mot)


liste_mot.sort()
print(liste_mot)


# Taille de la grille
taille_grille = int(input("taille de grille :"))
# Création de la matrice initiale avec des valeurs vides
grille = [['' for _ in range(taille_grille)] for _ in range(taille_grille)]

labels = []

for i in range(taille_grille):
    row_labels = []
    for j in range(taille_grille):
        label = tk.Label(fenetre, text="", width=2, height=1, font=("Arial", 10))
        label.grid(row=i, column=j)
        row_labels.append(label)
    labels.append(row_labels)

for mot in liste_mot:
    last_peut_ecrire = False

    while not last_peut_ecrire:
        direction_mot_num = int(random.randint(1, 8))
        print("direction :", direction_mot_num)
        x = int(random.randint(0, taille_grille - 1))
        print("x :", x)
        y = int(random.randint(0, taille_grille - 1))
        print("y :", y)

        direction_x, direction_y = 0, 0

        # direction_mot_num = int(input("direction :"))
        # x = int(input("x :"))
        # y = int((input("y :")))

        if direction_mot_num == 1:
            direction_y = -1
        elif direction_mot_num == 2:
            direction_x, direction_y = 1, -1
        elif direction_mot_num == 3:
            direction_x = 1
        elif direction_mot_num == 4:
            direction_x, direction_y = 1, 1
        elif direction_mot_num == 5:
            direction_y = 1
        elif direction_mot_num == 6:
            direction_x, direction_y = -1, 1
        elif direction_mot_num == 7:
            direction_x = -1
        elif direction_mot_num == 8:
            direction_x, direction_y = -1, -1

        peut_ecrire = True
        x_test, y_test = x, y

        for lettre_num in mot:
            print(" ")
            print("lettre :", lettre_num)
            print(f"position x_test : {x_test} | y_test : {y_test}")
            print(f"matrice position : '{grille[y_test][x_test]}'")
            if not (0 <= x_test < taille_grille and 0 <= y_test < taille_grille):
                peut_ecrire = False
                print("impossible")
                break
            if grille[y_test][x_test] != '' and grille[y_test][x_test] != lettre_num:
                peut_ecrire = False
                print("impossible")
                break
            print("je crois que c'est possible")
            x_test += direction_x
            y_test += direction_y

            # Ajoutez cette vérification pour éviter de dépasser les limites de la grille
            if not (0 <= x_test < taille_grille and 0 <= y_test < taille_grille):
                peut_ecrire = False
                print("impossible")
                break

        if peut_ecrire:
            last_peut_ecrire = True
        else:
            last_peut_ecrire = False

    # x, y = x - direction_x, y - direction_y
    r = random.randint(100, 255)
    g = random.randint(100, 255)
    b = random.randint(100, 255)
    couleur_hex = "#{:02X}{:02X}{:02X}".format(r, g, b)
    for lettre_num in mot:
        print(f"lettre à écrire : {lettre_num}")
        print(f"x : {x}")
        print(f"y : {y}")
        if 0 <= y < taille_grille and 0 <= x < taille_grille:
            print("oui")

            labels[y][x].config(text=lettre_num, bg=couleur_hex)
            grille[y][x] = lettre_num
        else:
            print("non")
        x += direction_x
        y += direction_y

# Ajouter des lettres aléatoires dans les emplacements vides
for i in range(taille_grille):
    for j in range(taille_grille):
        if grille[i][j] == '':
            grille[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            labels[i][j].config(text=grille[i][j])

print(grille)
bas = 0
droite = 40
for mot_num in liste_mot:
    if bas == taille_grille:
        bas, droite = 0, droite + 40

    label = tk.Label(fenetre, text=mot_num, width=20, height=1, font=("Arial", 10))
    label.grid(row=bas, column=droite)
    bas += 1

fenetre.mainloop()
