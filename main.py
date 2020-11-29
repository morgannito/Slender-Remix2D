import pygame
import time
import json
import requests
from urllib import request, parse
from tkinter import *
from hashlib import sha512


# Init pygame pour jouer un fond sonore !
pygame.mixer.init()


# Page Home
def main():
    # Creer une fenetre
    global fenetre
    fenetre = Tk()
    # Fullscreen
    fenetre.attributes('-fullscreen', 1)
    # Donne un titre à la fenetre
    fenetre.title("Slender Remix 2D")
    # Dimension de la fenetre
    fenetre.geometry("1920x1080")
    # Taille minimun de la fenetre
    fenetre.minsize(1080, 720)
    # Logo de la fenetre
    fenetre.iconbitmap("ressources/images/logo/slender-remix.ico")
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
    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du bouton play
    button_play = Button(frame, text="play", font=("caveat", 40), bg="black", fg="white", command=play)
    button_play = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=button_play)
    # Ajout du bouton high score
    button_hs = Button(frame, text="high score", font=("caveat", 40), bg="black", fg="white", command=highScore)
    button_hs = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center', window=button_hs)
    song = pygame.mixer.Sound("ressources/musique/aled.ogg")
    # Loop = repete la musique , time = à quel moment de demarrage  la musique doit etre jouer ,fadein = fondu sonore
    song.play(10, 0, 10000)
    # Affiche la fenetre
    fenetre.mainloop()

# Fonction boutton Home/play
# Page du Play
def play():
    song2 = pygame.mixer.Sound("ressources/musique/battement.wav")
    song2.play()
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
    title_play.pack()
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    # Création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du champ login
    pseudo = StringVar(frame, value='Login')
    global champ_login_login
    champ_login_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable = pseudo)
    champ_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center', window=champ_login_login)
    # Ajout du champ mdp
    mdp = StringVar(frame, value='Mot de passe')
    global champ_mdp_login
    champ_mdp_login = Entry(frame, font=("caveat", 40), bg="black", fg="white",show="*", textvariable = mdp)
    champ_mdp = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 , anchor='center', window=champ_mdp_login)
    # Ajout du bouton high score
    button_login = Button(frame, text="Login", font=("caveat", 40), bg="black", fg="white",command=login)
    button_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center', window=button_login)
    # Ajout du bouton high score
    button_inscription = Button(frame, text="inscription", font=("caveat", 40), bg="black", fg="white",command=signup)
    button_inscription = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center', window=button_inscription)


# Fonction boutton login
# Lancement du jeu apres connection
def login():
    login = champ_login_login.get()
    mdp = champ_mdp_login.get()
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
            if (x['erreur'] == 1) :
                # Rafraichi la fentre pour afficher la confirmation de l'enregistrement
                for widget in fenetre.winfo_children():
                    widget.pack_forget()
                title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
                title_play.pack()
                frame = Frame(fenetre, bg="black")
                # Ajouter la frame
                frame.pack(expand=YES)
                # Création de l'image de fond pour la fenetre
                fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
                fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
                fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
                fenetre.canvas.pack()
                fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
                # Ajout du champ login
                Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white", text="Erreur Mot de passe invalide ou login invalide")
                Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                                       anchor='center', window=Confirm)
                # Rafraichie
                frame.update()
                # Une ptite pause pour laisser le message s'afficher !
                time.sleep(5)
                # Renvoie sur la page de login  cause erreur mdp!
                play()
            else :
                for widget in fenetre.winfo_children():
                    widget.pack_forget()
                title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
                title_play.pack()
                frame = Frame(fenetre, bg="black")
                # Ajouter la frame
                frame.pack(expand=YES)
                # Création de l'image de fond pour la fenetre
                fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
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
                # Renvoie sur la page de login  cause erreur mdp!
                play()
                print("Lance le jeu ")

# Fonction button inscription
# Page Inscription au jeu
def signup():
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
    title_play.pack()
    frame = Frame(fenetre, bg="#1ac0ff")
    # Ajouter la frame
    frame.pack(expand=YES)
    # Création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du champ login
    global champ_login
    login = StringVar(frame, value='Login')
    champ_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=login)
    champ_login2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                               window=champ_login)
    # Ajout du champ mdp
    global champ_mdp
    mdp = StringVar(frame, value='Mot de passe')
    champ_mdp = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=mdp)
    champ_mdp2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=champ_mdp)
    # Ajout du champ mdp
    global champ_confirm_mdp
    confirm_mdp = StringVar(frame, value=' Confirm Mot de passe')
    champ_confirm_mdp = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=confirm_mdp)
    champ_confirm_mdp2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2+100, anchor='center', window=champ_confirm_mdp)

    # Ajout du bouton
    button_inscription = Button(frame, text="Confirmer", font=("caveat", 40), bg="black", fg="white", command=confirm_inscription)
    button_inscription2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center',
                                                      window=button_inscription)

# function du bouton de confirmation d'inscription
def confirm_inscription():
    # Recupere les données des champs
    login = champ_login.get()
    mdp = champ_mdp.get()
    confirm_mdp = champ_confirm_mdp.get()
    # Verifie si les champs sont plein
    if (login):
        if (mdp):
            if (confirm_mdp):
                # Verifie si les mdp sont les memes
                if (mdp == confirm_mdp):
                    mdp = mdp.encode()
                    mdp_sign = sha512(mdp).hexdigest()
                    # Mot de passe hashé , pour plus de sécurité ;)
                    dic = {"login" : login , "mdp" : mdp_sign}
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
                    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
                    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
                    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
                    fenetre.canvas.pack()
                    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
                    # Ajout du champ login
                    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white", text="Vous etes bien Inscrit")
                    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 ,
                                                               anchor='center', window=Confirm)
                    # Rafraichie
                    frame.update()
                    # Une ptite pause pour laisser le message s'afficher !
                    time.sleep(5)
                    # Renvoie sur la page de login !
                    play()

# Func Bouton Home/High Score
# Affiche les highScore
def highScore():
    print("Lance la fentre des high Score")


# Lance le programme :) !
main()