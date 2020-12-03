import  pygame
from tkinter import *
from hashlib import sha512
import json
import requests
import time

import module.play.button as play

import module.jeu.board as start

# Fonction boutton login
# Lancement du jeu apres connection
def login(fenetre,login,mdp ):
    # Verifie si les champs sont plein
    if (login):
        if (mdp):
            mdp = mdp.encode()
            mdp_hash = sha512(mdp).hexdigest()
            # Mot de passe hashé , pour plus de sécurité ;)
            dic = {"login": login, "mdp": mdp_hash}
            jsondata = json.dumps(dic).encode("utf8")
            url = 'http://morgannito.com/apiSlender/login.php'
            x = requests.post(url, data=jsondata)
            x = json.loads(x.text)
            if (x['erreur'] == 1):
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
                Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                                text="Erreur Mot de passe invalide ou login "
                                     "")
                Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                                       anchor='center', window=Confirm)
                # Rafraichie
                frame.update()
                # Une ptite pause pour laisser le message s'afficher !
                time.sleep(5)
                # Renvoie sur la page de login  cause erreur mdp!
                play.play(fenetre)
            else:
                # Lance le niveaux 1
                fileName = 'ressources/level/1.csv'
                # matrice used to display the board
                lab = []
                # starting position
                start_position = [1, 1]
                # human position
                human_position = start_position

                with open(fileName, "r") as file:
                    # decode and get the column and row number
                    first_line = file.readline()
                    row_and_column = first_line.replace('\n', '').split(",")
                    row_and_column = [int(i) for i in row_and_column]
                    for line in file:
                        data = line.replace('\n', '').split(",")
                        data = [int(i) for i in data]
                        lab.append(data)
                    column_number = len(data)
                    row_number = len(lab)
                    end_position = [row_number - 2, column_number - 2]
                file.close()
                start.jouer(fenetre,lab)


