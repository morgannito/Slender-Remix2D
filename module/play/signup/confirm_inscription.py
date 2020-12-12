import  pygame
from tkinter import *
from hashlib import sha512
import json
import requests
import time

import module.play.button as connection
# function du bouton de confirmation d'inscription
def confirm_inscription(fenetre ,login,mdp,confirm_mdp ):
    # Verifie si les champs sont plein
    if (login):
        if (mdp):
            if (confirm_mdp):
                # Verifie si les mdp sont les memes
                if (mdp == confirm_mdp):
                    mdp = mdp.encode()
                    mdp_sign = sha512(mdp).hexdigest()
                    # Mot de passe hashé , pour plus de sécurité ;)
                    dic = {"login": login, "mdp": mdp_sign , "lvl" : "0" }
                    jsondata = json.dumps(dic).encode("utf8")
                    url = 'http://morgannito.com/apiSlender/inscription.php'
                    x = requests.post(url, data=jsondata)
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
                    # Ajout du champ login
                    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white", text="Vous etes bien Inscrit")
                    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                                           anchor='center', window=Confirm)
                    # Rafraichie
                    frame.update()
                    # Une ptite pause pour laisser le message s'afficher !
                    time.sleep(2)
                    # Renvoie sur la page de login !
                    connection.play(fenetre)
