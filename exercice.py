#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes, print_recipe
import json

# TODO: Définissez vos fonction ici
# exo 1


def compare(fichier1, fichier2):
    with open(fichier1, encoding='utf-8') as f:
        liste1 = f.readlines()
    with open(fichier2, encoding='utf-8') as g:
        liste2 = g.readlines()
    for i in range(len(liste1)):
        if liste1[i] != liste2[i]:
            for j in liste1[i]:
                if j != liste2[i][liste1[i].index(j)]:
                    position = (i, liste1[i].index(j))
                    return f"Le fichier {fichier1} a un {j} au caractère {position[1]} de la ligne {position[0]} que le fichier {fichier2} a un {liste2[i][liste1[i].index(j)]} à la même position"
    return "Les deux fichiers sont identiques"

# exo 2


def recopie(fichier):
    with open(fichier, encoding='utf-8') as f:
        liste = f.readlines()
    fichier = fichier[:-4]
    with open(fichier+'_recopie', 'w', encoding='utf-8') as g:
        chaine = ''
        for i in range(len(liste)):
            for c in liste[i]:
                if c != ' ':
                    chaine += c
                elif c == ' ':
                    chaine += '   '
        g.write(chaine)

# exo 3


def notes(fichier):
    with open(fichier, encoding='utf-8') as f:
        liste = f.readlines()
        for j in range(len(liste)-1):
            liste[j] = int(liste[j][:-1])
        liste[-1] = int(liste[-1])
    with open('notes_pourcentages.txt', 'w', encoding='utf-8') as g:
        for i in liste:
            for k in PERCENTAGE_TO_LETTER:
                if i >= PERCENTAGE_TO_LETTER[k][0] and i < PERCENTAGE_TO_LETTER[k][1]:
                    g.write(str(i)+' : ')
                    g.write(k+"\n")

# exo 4


def fichier_recettes():
    with open("recettes.json") as f:
        dict = json.load(f)
    var = input("'A' : Ajouter une recette\n'M' : Modifier une recette\n'S' : Supprimer une recette\n'R' : Afficher une recette\n'Q' : Quitter le programme\n")
    if var == 'A':
        ajouter()
    elif var == 'M':
        modifier()
    elif var == 'S':
        supprimer()
    elif var == 'R':
        print_recipe(dict)
    elif var == 'Q':
        return "Vous avez quitté le programme\n"
    fichier_recettes()


def ajouter():
    with open("recettes.json") as f:
        dict = json.load(f)
    with open("recettes.json", "w") as f:
        dict_recette = add_recipes({})
        for cle in dict_recette:
            dict[cle] = dict_recette[cle]
        json.dump(dict, f)


def modifier():
    with open("recettes.json") as f:
        dict = json.load(f)
    with open("recettes.json", "w") as f:
        var = input("'R' : Modifier le nom de la recette\n'I' : Modifier les ingrédients\n")
        if var == 'R':
            noms = input("Entrer l'ancien nom et le nouveau nom de la recette séparés par une virgule\n").split(',')
            for cle in dict:
                if cle == noms[0]:
                    dict[noms[1]] = dict[noms[0]]
                    del dict[noms[0]]
                    break
            json.dump(dict, f)
        elif var == 'I':
            var1 = input("Entrer le nom de la recette dont vous voulez modifier les ingrédients\n")
            for cle in dict:
                if cle == var1:
                    ingredients = input("Entrez la liste d'ingrédiants de la recette, svp séparer les ingrédiants par une ,\n").split(',')
                    dict[cle] = ingredients
                    json.dump(dict, f)
                    break


def supprimer():
    with open("recettes.json") as f:
        dict = json.load(f)
    var = input("Enter le nom de la recette à supprimer\n")
    with open("recettes.json", "w") as f:
        for cle in dict:
            if var == cle:
                del dict[var]
                json.dump(dict, f)
                break

# exo 5


def extrait_nb():
    with open("exemple.txt", encoding='utf-8') as f:
        liste1 = f.readlines()
    liste_nb = []
    for i in liste1:
        liste2 = i.split(' ')
        for j in liste2:
            for k in range(10):
                if j.find(str(k)) != -1:
                    liste_nb.append(int(j))
                    break
    return sorted(liste_nb)

# exo 6


def copie1sur2(fichier1, fichier2):
    with open(fichier1, encoding='utf-8') as f:
        liste = f.readlines()
    liste1 = []
    for i in range(len(liste)):
        if i % 2 == 0:
            liste1.append(liste[i])
    with open(fichier2, "w", encoding='utf-8') as g:
        for j in liste1:
            g.write(j)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # os.chdir("../") : recule le chemin d'un dossier
    # sys.stdout = open('./file.txt, 'w') : tous les print ne renvoient plus dans la console mais écrit dans le fichier file

    #print(compare("exemple.txt", "exemple1.txt"))
    #recopie("exemple.txt")
    #notes("notes.txt")
    fichier_recettes()
    #print(extrait_nb())
    #copie1sur2("exemple.txt", "exemple1sur2.txt")
    pass
