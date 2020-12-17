from tkinter import *
import pygame
import module.back as back
import time
# affiche une fenetre pour le perdant et le fait retourner au menu
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
    # initialise le fichier audio
    song = pygame.mixer.Sound("ressources/musique/slender.ogg")
    # joue l'audio
    song.play(1, 0, 0)
    # rafraichie la fenetre
    fenetre.update()
    # marque un temps de pause
    time.sleep(10)
    # retour au menu apres 10s
    back.backMenu(fenetre)

