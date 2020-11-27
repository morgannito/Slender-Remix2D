from tkinter import *
import pygame

pygame.mixer.init()

def main():
    # creer une fenetre
    global fenetre
    fenetre = Tk()
    # fullscreen
    fenetre.attributes('-fullscreen', 1)
    # donne un titre à la fenetre
    fenetre.title("Slender Remix 2D")
    # dimension de la fenetre
    fenetre.geometry("1920x1080")
    # taille minimun de la fenetre
    fenetre.minsize(1080, 720)
    # logo de la fenetre
    fenetre.iconbitmap("ressources/images/logo/slender-remix.ico")
    # couleur de fond de la fenetre
    fenetre.config(background="black")
    # ajout du titre du jeu dans la fenetre
    title = Label(fenetre, text="Slender Remix 2D ", font=("caveat", 40), bg="black", fg="white")
    # ajoute le titre
    title.pack()
    # creation d'une frame
    frame = Frame(fenetre, bg="#1ac0ff")
    # ajouter la frame
    frame.pack(expand=YES)
    # création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # ajout du bouton play
    button_play = Button(frame, text="play", font=("caveat", 40), bg="black", fg="white", command=play)
    button_play = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=button_play)
    # ajout du bouton high score
    button_hs = Button(frame, text="high score", font=("caveat", 40), bg="black", fg="white", command=highScore)
    button_hs = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center', window=button_hs)
    # init pygame pour jouer un fond sonore !
    song = pygame.mixer.Sound("ressources/musique/aled.ogg")
    # loop = repete la musique , time = à quel moment de demarrage  la musique doit etre jouer ,fadein = fondu sonore
    song.play(10, 0, 10000)
    # affiche la fenetre
    fenetre.mainloop()

# fonnction boutton play
def play():
    song2 = pygame.mixer.Sound("ressources/musique/battement.wav")
    song2.play()
    for widget in fenetre.winfo_children():
        ## CHOIX 1:
        widget.pack_forget()  # Si vous utilisez .pack()
    title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
    title_play.pack()
    frame = Frame(fenetre, bg="#1ac0ff")
    # ajouter la frame
    frame.pack(expand=YES)
    # création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # ajout du champ login
    pseudo = StringVar(frame, value='Login')
    champ_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable = pseudo)
    champ_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center', window=champ_login)
    # ajout du champ mdp
    mdp = StringVar(frame, value='Mot de passe')
    champ_mdp = Entry(frame, font=("caveat", 40), bg="black", fg="white",show="*", textvariable = mdp)
    champ_mdp = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 , anchor='center', window=champ_mdp)
    # ajout du bouton high score
    button_login = Button(frame, text="Login", font=("caveat", 40), bg="black", fg="white",command=login)
    button_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center', window=button_login)
    # ajout du bouton high score
    button_inscription = Button(frame, text="inscription", font=("caveat", 40), bg="black", fg="white",command=signup)
    button_inscription = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center', window=button_inscription)


# fonction boutton login , Lancement du jeu apres connection
def login():
    print("Lance le jeu si login ok")


# fonction button inscription,  Inscription au jeu
def signup():
    for widget in fenetre.winfo_children():
        ## CHOIX 1:
        widget.pack_forget()  # Si vous utilisez .pack()
    title_play = Label(fenetre, text="Slender Remix 2D", font=("caveat", 40), bg="black", fg="white")
    title_play.pack()
    frame = Frame(fenetre, bg="#1ac0ff")
    # ajouter la frame
    frame.pack(expand=YES)
    # création de l'image de fond pour la fenetre
    fenetre.image = PhotoImage(file='ressources/images/menu/fantasy-2847724_1920.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # ajout du champ login
    login = StringVar(frame, value='Login')
    champ_login = Entry(frame, font=("caveat", 40), bg="black", fg="white", textvariable=login)
    champ_login = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                               window=champ_login)
    # ajout du champ mdp
    mdp = StringVar(frame, value='Mot de passe')
    champ_mdp = Entry(frame, font=("caveat", 40), bg="black", fg="white", show="*", textvariable=mdp)
    champ_mdp = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=champ_mdp)

    # ajout du bouton
    button_inscription = Button(frame, text="inscription", font=("caveat", 40), bg="black", fg="white")
    button_inscription = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 350, anchor='center',
                                                      window=button_inscription)

# Affiche les highScore
def highScore():
    print("Lance la fentre des high Score")

main()