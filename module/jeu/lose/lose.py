from tkinter import *
import pygame
import module.back as back
import time
import module.quit.buttonQuit as ragequit
# affiche une fenetre pour le perdant et lui fait quitter le jeu apres un screamer o/
def lose(fenetre):
    # permet d'initialiser le mixer de pygame
    pygame.mixer.init()
    # efface les element de la fenetre precedentes
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    # ajoute une image dans le background
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    # affiche un message de winners
    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                    text="Vous avez perdu ")
    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                           anchor='center', window=Confirm)
    # initialise le fichier audio
    song = pygame.mixer.Sound("ressources/musique/slender.ogg")
    # joue l'audio
    song.play(1, 0, 0)
    # rafraichie la fenetre
    fenetre.update()
    # marque un temps de pause
    time.sleep(5)
    # rage quit
    ragequit.quit(fenetre)

