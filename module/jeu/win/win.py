import  pygame
from tkinter import *
from hashlib import sha512
import json
import requests
import time
import module.jeu.win.save as save

def win(fenetre,pseudo):
    #save
    save.save(pseudo)

    # Rafraichi la fentre pour afficher la confirmation de l'enregistrement
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
    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                    text="Vous avez échappé à slender ")
    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                           anchor='center', window=Confirm)
    # Rafraichie
    frame.update()
    # Une ptite pause pour laisser le message s'afficher !
    time.sleep(5)
    print("Pas de niveaux 2 pour le moment ...")
    print("La suite dans le prochain DLC")
