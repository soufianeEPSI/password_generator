#!/usr/bin/env python

import tkinter as tk
import passgenlib.passgen as pg

# Fonction qui sera appelée lors du clic sur le bouton# Fonction qui sera appelée lors du clic sur le bouton
def on_click():
    s = pg.genrandompass(5,5,4,4)  # Complexité recomandée par l'ANSSI suprérieure à 100 bits
    mdp.delete(0, 'end')
    mdp.insert(0, s)

# TODO - Ajouter possibilité de choisir la complexité du mot de passe dans la fenêtre
# TODO - Ajouter fonction pour calcul de l'entropie
# TODO - Ajouter fonction real random 
# TODO - Ajouter stockage login / mdp dans BDD
# TODO - Ajouter plugin combinaison de touches pour écrire login et mot de passe dans app

# TODO - Ajouter un bouton pour afficher le mot de passe en clair
# TODO - Fonction copier dans le presse-papier 10 secondes et supprimer du presse-papier

# Création de la fenêtre
root = tk.Tk()
root.title('EPSI Password Generator')
root.geometry('300x200')
root.resizable(True, True)
root.img = tk.PhotoImage(file='icons/passwordGenerator.png')
root.iconphoto(False,root.img)

# Création des widgets
# Création  du champ de saisie où sera affiché le mot de passe
mdp = tk.Entry(root,width=30,justify='center') # On crée le widget Entry qui permet de saisir du texte
mdp.pack(side='top',fill='none',pady=60) # La fonction pack permet de positionner le widget dans la fenêtre

# Création du bouton
btn = tk.Button(root, text = 'Générer un mot de passe', bd = '5', command = on_click) # Le bouton a un bord de 5px et appelle la fonction on_click
btn.pack(side = tk.BOTTOM)

# Lancement de la fenêtre
root.mainloop()