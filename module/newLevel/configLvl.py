import pygame
from tkinter import *
import module.back as back
import module.newLevel.testMap as test

def newLevel(fenetre):
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
    title_play.pack()
    frame = Frame(fenetre, bg="#1ac0ff")
    # Ajouter la frame
    frame.pack(expand=YES)
    # Création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    Retour = Button(fenetre, text="Retour", font=("caveat", 40), bg="black", fg="white",command=lambda : back.backMenu(fenetre))
    Retour = fenetre.canvas.create_window(fenetre.w // 2 - 800, fenetre.h // 2  - 400, anchor='center',
                                                      window=Retour)

    login = StringVar(frame, value='Matrice 19 L par 14 C max ..')
    champ_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=login)
    champ_login2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                                window=champ_login)

    # Ajout du bouton
    button_inscription = Button(frame, text="Confirmer", font=("caveat", 40), bg="black", fg="white", command=lambda : test.init(fenetre,champ_login.get()))
    button_inscription2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center',
                                                       window=button_inscription)

