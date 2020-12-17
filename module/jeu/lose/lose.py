from tkinter import *
import pygame
import module.back as back
import time

def lose(fenetre):
    pygame.mixer.init()

    for widget in fenetre.winfo_children():
        widget.pack_forget()
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    fenetre.image = PhotoImage(file='ressources/images/menu/background.png')
    fenetre.w, fenetre.h = fenetre.image.width(), fenetre.image.height()
    fenetre.canvas = Canvas(frame, width=fenetre.w, height=fenetre.h, bd=0, highlightthickness=0)
    fenetre.canvas.pack()
    fenetre.canvas.create_image((fenetre.w // 2, fenetre.h // 2), image=fenetre.image)
    song = pygame.mixer.Sound("ressources/musique/slender.ogg")
    song.play(1, 0, 0)
    fenetre.update()
    time.sleep(10)
    back.backMenu(fenetre)

