import  pygame
from tkinter import *
from hashlib import sha512
import json
import requests
import time
from PIL import Image
from PIL import ImageTk

import module.jeu.decode as decode


def jouer(fenetre):
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
    title_play.pack()
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    # Création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du champ login
    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                    text="Connexion en cours ...")
    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                           anchor='center', window=Confirm)
    # Rafraichie
    frame.update()
    # Une ptite pause pour laisser le message s'afficher !
    time.sleep(5)
    # Lance le niveaux 1
    fileName = 'ressources/level/1.csv'
    # matrice used to display the board
    global lab
    lab = []
    # starting position
    start_position = [1, 1]
    # human position
    human_position = start_position
    decode.decode_csv(fileName)
    # affiche la matrice
    for i in lab:
        print(i)
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    title = Label(fenetre, text="Slender Remix 2D ", font=("caveat", 40), bg="black", fg="white")
    # Ajoute le titre
    title.pack()
    # Creation d'une frame
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)

    # Création d'un canvas : zone graphique dédié et modifiable
    canvas1 = Canvas(frame, width=1080, height=720, background='white')
    carreau = [[canvas1.create_rectangle(i * 40, j * 40, (i + 1) * 40, (j + 1) * 40)
                for i in range(14)] for j in range(19)]
    # max i 26 max j 18
    canvas1.pack()

    mur = Image.open("ressources/images/jeu/buisson.jpg")  # PIL solution
    mur = mur.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    mur = ImageTk.PhotoImage(mur)  # convert to PhotoImage

    perso = Image.open("ressources/images/jeu/human.jpg")  # PIL solution
    perso = perso.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    perso = ImageTk.PhotoImage(perso)  # convert to PhotoImage

    slender = Image.open("ressources/images/jeu/slenderpng.jpg")  # PIL solution
    slender = slender.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    slender = ImageTk.PhotoImage(slender)  # convert to

    pages = Image.open("ressources/images/jeu/page.jpg")  # PIL solution
    pages = pages.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    pages = ImageTk.PhotoImage(pages)  # convert to PhotoImage

    sortie = Image.open("ressources/images/jeu/portail.jpg")  # PIL solution
    sortie = sortie.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    sortie = ImageTk.PhotoImage(sortie)  # convert to PhotoImage

    terre = Image.open("ressources/images/jeu/terre.jpg")  # PIL solution
    terre = terre.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    terre = ImageTk.PhotoImage(terre)  # convert to PhotoImage
    x = 0
    y = 0
    for row in lab:
        for i in row:
            # Wall visual
            if i == -1:
                canvas1.itemconfigure(carreau[x][y], fill="white")
                w, p, g, l = canvas1.coords(carreau[x][y])
                canvas1.create_image(w, p, anchor=NW, image=mur)
            # pages
            if i == 33:
                canvas1.itemconfigure(carreau[x][y], fill="white")
                w, p, g, l = canvas1.coords(carreau[x][y])
                canvas1.create_image(w, p, anchor=NW, image=pages)
            # human
            if i == 22:
                canvas1.itemconfigure(carreau[x][y], fill="white")
                w, p, g, l = canvas1.coords(carreau[x][y])
                canvas1.create_image(w, p, anchor=NW, image=perso)
            # libre
            if i == 99:
                canvas1.itemconfigure(carreau[x][y], fill="white")
                w, p, g, l = canvas1.coords(carreau[x][y])
                canvas1.create_image(w, p, anchor=NW, image=terre)

            #  sortie
            if i == 44:
                canvas1.itemconfigure(carreau[x][y], fill="white")
                w, p, g, l = canvas1.coords(carreau[x][y])
                canvas1.create_image(w, p, anchor=NW, image=sortie)

            #  slender
            if i == 66:
                canvas1.itemconfigure(carreau[x][y], fill="white")
                w, p, g, l = canvas1.coords(carreau[x][y])
                canvas1.create_image(w, p, anchor=NW, image=slender)
            y = y + 1
        x = x + 1
        y = 0
    song = pygame.mixer.Sound("ressources/musique/aled.ogg")
    # Loop = repete la musique , time = à quel moment de demarrage  la musique doit etre jouer ,fadein = fondu sonore
    song.play(10, 0, 10000)
    # Affiche la fenetre
    fenetre.mainloop()
