import json
import time
from hashlib import sha512
from tkinter import *
from PIL import Image
from PIL import ImageTk
import pygame
import requests

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
    button_play = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                               window=button_play)
    # Ajout du bouton high score
    button_hs = Button(frame, text="high score", font=("caveat", 40), bg="black", fg="white", command=highScore)
    button_hs = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=button_hs)
    # Ajout du bouton Quitter
    button_quit = Button(frame, text="Quitter", font=("caveat", 40), bg="black", fg="white", command=quit)
    button_quit = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center',
                                               window=button_quit)
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
    champ_login_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=pseudo)
    champ_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                               window=champ_login_login)
    # Ajout du champ mdp
    mdp = StringVar(frame, value='Mot de passe')
    global champ_mdp_login
    champ_mdp_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", show="*", textvariable=mdp)
    champ_mdp = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=champ_mdp_login)
    # Ajout du bouton high score
    button_login = Button(frame, text="Login", font=("caveat", 40), bg="black", fg="white", command=login)
    button_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center',
                                                window=button_login)
    # Ajout du bouton high score
    button_inscription = Button(frame, text="inscription", font=("caveat", 40), bg="black", fg="white", command=signup)
    button_inscription = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center',
                                                      window=button_inscription)


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
                fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
                fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
                fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
                fenetre.canvas.pack()
                fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
                # Ajout du champ login
                Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                                text="Erreur Mot de passe invalide ou login invalide")
                Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                                       anchor='center', window=Confirm)
                # Rafraichie
                frame.update()
                # Une ptite pause pour laisser le message s'afficher !
                time.sleep(5)
                # Renvoie sur la page de login  cause erreur mdp!
                play()
            else:
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
                # Lance le niveaux 1
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
    champ_confirm_mdp2 = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 100, anchor='center',
                                                      window=champ_confirm_mdp)

    # Ajout du bouton
    button_inscription = Button(frame, text="Confirmer", font=("caveat", 40), bg="black", fg="white",
                                command=confirm_inscription)
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
                    dic = {"login": login, "mdp": mdp_sign}
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
                    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
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


def quit():
    fenetre.destroy()


# Lance le programme :) !
# main()

# decode the .csv file
def decode_csv(fileName):
    with open(fileName, "r") as file:
        # decode and get the column and row number
        first_line = file.readline()
        row_and_column = first_line.replace('\n', '').split(",")
        row_and_column = [int(i) for i in row_and_column]
        for line in file:
            data = line.replace('\n', '').split(",")
            data = [int(i) for i in data]
            lab.append(data)
        global row_number, column_number
        column_number = len(data)
        row_number = len(lab)
        end_position = [row_number - 2, column_number - 2]
    file.close()
#############################################################################################"
# todo finir cette phase de test
fileName = 'level/1.csv'
# matrice used to display the board
lab = []
# starting position
start_position = [1, 1]
# human position
human_position = start_position
decode_csv(fileName)

# affiche la matrice
for i in lab:
    print(i)

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

# Création d'un canvas : zone graphique dédié et modifiable
canvas1 = Canvas(frame, width=1080, height=720, background='white')
carreau = [[canvas1.create_rectangle(i * 40, j * 40, (i + 1) * 40, (j + 1) * 40)
            for i in range(14)] for j in range(19)]
            #max i 26 max j 18
canvas1.pack()

mur = Image.open("ressources/images/buisson.jpg")  # PIL solution
mur = mur.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
mur = ImageTk.PhotoImage(mur)  # convert to PhotoImage

perso = Image.open("ressources/images/human.jpg")  # PIL solution
perso = perso.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
perso = ImageTk.PhotoImage(perso)  # convert to PhotoImage

slender = Image.open("ressources/images/slenderpng.jpg")  # PIL solution
slender = slender.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
slender = ImageTk.PhotoImage(slender)  # convert to

pages = Image.open("ressources/images/page.jpg")  # PIL solution
pages = pages.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
pages = ImageTk.PhotoImage(pages)  # convert to PhotoImage

sortie = Image.open("ressources/images/portail.jpg")  # PIL solution
sortie = sortie.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
sortie = ImageTk.PhotoImage(sortie)  # convert to PhotoImage

terre = Image.open("ressources/images/terre.jpg")  # PIL solution
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




