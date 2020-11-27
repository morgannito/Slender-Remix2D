from tkinter import *
import pygame

# creer une fenetre
fenetre = Tk()
# donne un titre à la fenetre
fenetre.title("Slender Remix 2D")
# dimension de la fenetre
fenetre.geometry("1920x1080")
# taille minimun de la fenetre
fenetre.minsize(1080, 720)
# logo de la fenetre
fenetre.iconbitmap("ressources/images/logo/slender-remix.ico")
# couleur de fond de la fenetre
fenetre.config(background="black")
# ajout du titre du jeu dans la fenetre
title = Label(fenetre, text="Slender Remix 2D ", font=("caveat", 40), bg="black", fg="white")
# ajoute le titre
title.pack()
# creation d'une frame
frame = Frame(fenetre, bg="#1ac0ff")
# ajouter la frame
frame.pack(expand=YES)
# création de l'image de fond pour la fenetre
fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
fenetre.canvas.pack()
fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
# ajout du bouton play
button_play = Button(frame, text="play", font=("caveat", 40), bg="black", fg="white")
button_play = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=button_play)
# ajout du bouton high score
button_hs = Button(frame, text="high score", font=("caveat", 40), bg="black", fg="white")
button_hs = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center', window=button_hs)

# init pygame pour jouer un fond sonore !
pygame.mixer.init()
song = pygame.mixer.Sound("ressources/musique/aled.ogg")
song.play()



# affiche la fenetre
fenetre.mainloop()

