from tkinter import *
import time
import module.back as back
# function appelé en cas de probleme (exemple le niveau suivant n'existe pas encore )
def erreur(fenetre):
    # efface les element de la fenetre precedente
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    # rajoute un label
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
    # rajoute un label avec le message d'erreur
    Confirm = Label(frame, font=("caveat", 40), bg="black", fg="white",
                    text="le level suivant est inexistant veuillez le créer ou attendre qu'un créateur le créer ")
    Confirm = fenetre.canvas.create_window(fenetre.w // 2, fenetre.h // 2,
                                           anchor='center', window=Confirm)
    # Rafraichie
    frame.update()
    # Une ptite pause pour laisser le message s'afficher !
    time.sleep(3)
    back.backMenu(fenetre)