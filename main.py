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


#affiche la fenetre
fenetre.mainloop()