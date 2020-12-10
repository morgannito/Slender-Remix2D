import  pygame
from tkinter import *
import module.play.login as login
import module.play.signup.inscription as signup

import module.play.login
# Fonction boutton Home/play
# Page du Play
def play(fenetre):
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
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du bouton inscription
    Retour = Button(fenetre, text="Retour", font=("caveat", 40), bg="black", fg="white")
    Retour = fenetre.canvas.create_window(fenetre.w // 2 - 800, fenetre.h // 2  - 400, anchor='center',
                                                      window=Retour)
    # Ajout du champ login
    pseudo = StringVar(frame, value='Login')
    champ_login_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=pseudo)
    champ_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                               window=champ_login_login)
    # Ajout du champ mdp
    mdp = StringVar(frame, value='Mot de passe')
    champ_mdp_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", show="*", textvariable=mdp)
    champ_mdp = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=champ_mdp_login)
    # Ajout du bouton login
    button_login = Button(frame, text="Login", font=("caveat", 40), bg="black", fg="white", command=lambda: login.login(fenetre,champ_login_login.get(),champ_mdp_login.get()) )
    button_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center',
                                                window=button_login)
    # Ajout du bouton inscription
    button_inscription = Button(frame, text="inscription", font=("caveat", 40), bg="black", fg="white", command=lambda : signup.signup(fenetre))
    button_inscription = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center',
                                                      window=button_inscription)