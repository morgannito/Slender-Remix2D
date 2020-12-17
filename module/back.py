# buttonQuit.py
import module.quit.buttonQuit as homeExit
# play.py
import module.play.play as homePlay
# config.py
import module.newLevel.configLvl as config
from functools import partial
import pygame
from tkinter import *


# Page Home sert de boutton de retour sans creer une nouvelle fenetre
def backMenu(fenetre):
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    # Logo de la fenetre
    # fenetre.iconbitmap("ressources/images/logo/slender-remix.ico")
    # Couleur de fond de la fenetre
        fenetre.config(background="black")
    # Ajout du titre du jeu dans la fenetre
    title = Label(fenetre, text="Slender Remix 2D ", font=("caveat", 40), bg="black", fg="white")
    # Ajoute le titre
    title.pack()
    # Creation d'une frame
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    # Création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du bouton play qui permettra de changer de jouer
    button_play = Button(frame, text="play", font=("caveat", 40), bg="black", fg="white",
                         command=partial(homePlay.play, fenetre))
    button_play = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 -200 , anchor='center',
                                               window=button_play)
    # Ajout du bouton new level qui permettra d'ajouter un level à partir d'une matrice
    button_level = Button(frame, text="New level", font=("caveat", 40), bg="black", fg="white",
                         command=partial(config.newLevel, fenetre))
    button_level = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 , anchor='center',
                                               window=button_level)
    # Ajout du bouton Quitter
    button_quit = Button(frame, text="Quitter", font=("caveat", 40), bg="black", fg="white",
                         command=partial(homeExit.quit, fenetre))
    button_quit = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center',
                                               window=button_quit)
    # Affiche la fenetre
    fenetre.mainloop()
