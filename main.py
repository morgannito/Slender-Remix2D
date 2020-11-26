from tkinter import *

#creer une fenetre
fenetre = Tk()
#donne un titre à la fenetre
fenetre.title("Slender Remix 2D")
#dimension de la fenetre
fenetre.geometry("1920x1080")
#taille minimun de la fenetre
fenetre.minsize(1080,720)
#logo de la fenetre
fenetre.iconbitmap("ressources/images/logo/slender-remix.ico")
#couleur de fond de la fenetre
fenetre.config(background='#1ac0ff')
#ajout du titre du jeu dans la fenetre
title = Label(fenetre, text="Slender Remix 2D ", font=("caveat",40),bg="#1ac0ff",fg="white")
title.pack()

#affiche la fenetre
fenetre.mainloop()