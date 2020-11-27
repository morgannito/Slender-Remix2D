from tkinter import *
from PIL import Image, ImageTk

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
fenetre.config(background="black")
#ajout du titre du jeu dans la fenetre
title = Label(fenetre, text="Slender Remix 2D ", font=("caveat",40),bg="black",fg="white")
#ajoute le titre
title.pack()
fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
fenetre.canvas = Canvas(fenetre, width=fenetre.w, height=fenetre.h,bd=0 ,highlightthickness=0)
fenetre.canvas.pack(expand=YES)
fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)

#creation d'une frame
frame = Frame(fenetre, bg="#1ac0ff")




#ajout d'un bouton dans la frame
button_play = Button(fenetre, text="play",font=("caveat",40),bg="black",fg="white")
button_play.pack()


#ajouter la frame
frame.pack()

#affiche la fenetre
fenetre.mainloop()