from functools import partial
import pygame
from tkinter import *
# Init pygame pour jouer un fond sonore !
pygame.mixer.init()
# buttonHighScore.py
import module.highScore.buttonHighScore as highscore
# buttonQuit.py
import module.quit.buttonQuit as homeExit
import module.play.button as homePlay

# Page Home
def main():
    # Creer une fenetre
    fenetre = Tk()
    # Fullscreen
    # fenetre.attributes('-fullscreen', 1)
    # Donne un titre à la fenetre
    fenetre.title("Slender Remix 2D")
    # Dimension de la fenetre
    fenetre.geometry("1920x1080")
    # Taille minimun de la fenetre
    fenetre.minsize(1080, 720)
    # Logo de la fenetre
    # fenetre.iconbitmap("ressources/images/logo/slender-remix.ico")
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
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # Ajout du bouton play
    button_play = Button(frame, text="play", font=("caveat", 40), bg="black", fg="white",
                         command=partial(homePlay.play, fenetre))
    button_play = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 - 200, anchor='center',
                                               window=button_play)
    # Ajout du bouton high score
    button_hs = Button(frame, text="high score", font=("caveat", 40), bg="black", fg="white", command=highscore.fenetre)
    button_hs = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2, anchor='center', window=button_hs)
    # Ajout du bouton Quitter
    button_quit = Button(frame, text="Quitter", font=("caveat", 40), bg="black", fg="white",
                         command=partial(homeExit.quit, fenetre))
    button_quit = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2 + 200, anchor='center',
                                               window=button_quit)
    song = pygame.mixer.Sound("ressources/musique/aled.ogg")
    # Loop = repete la musique , time = à quel moment de demarrage  la musique doit etre jouer ,fadein = fondu sonore
    song.play(10, 0, 10000)
    # Affiche la fenetre
    fenetre.mainloop()


# Lance le programme :) !
main()
