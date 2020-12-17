import  pygame
from tkinter import *
from hashlib import sha512
import json
import requests
import time
import  module.back as menu

# function qui va sauvegardé le niveau que l'utilisateur à crée
# cette fonction verifie que l'utilisateur à créer un niveau valide en le jouant et gagnant la partie.
def win(fenetre , lab ):
    # prepare le json avec la matrice du niveau
    dic = {"matrice": lab}
    jsondata = json.dumps(dic).encode("utf8")
    # lien de l'api
    url = 'http://morgannito.com/apiSlender/newlvl.php'
    # request post
    x = requests.post(url, data=jsondata)
    x = json.loads(x.text)
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
                    text="Votre level à etait ajouté avec succes")
    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                           anchor='center', window=Confirm)
    # Rafraichie
    frame.update()
    # Une ptite pause pour laisser le message s'afficher !
    time.sleep(1)
    menu.backMenu(fenetre)
