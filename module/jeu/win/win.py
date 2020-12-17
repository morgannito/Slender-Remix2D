from tkinter import *
import time
import module.jeu.win.save as save
import module.jeu.decode as decode
import module.jeu.board as board
import module.jeu.win.erreur404 as erreur

def win(fenetre,pseudo):
    # save le niveau de l'utilisateur
    lvl = save.save(pseudo)
    # Rafraichi la fentre pour afficher la confirmation de l'enregistrement
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    # affiche un label
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
    # affiche un message de winners
    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                    text="Vous avez échappé à slender, Chargement du lvl "+ str(lvl) + "en cours ..")
    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                           anchor='center', window=Confirm)
    # Rafraichie
    frame.update()
    # Une ptite pause pour laisser le message s'afficher !
    time.sleep(2)
    try:
        # essaie de lancer le prochain niveau si il existe.
        next = decode.decode(lvl)
        # si il existe lance le niveau !
        board.init(fenetre,next,pseudo)
    except:
        # si le niveau existe pas affiche message d'erreur.
            erreur.erreur(fenetre)
