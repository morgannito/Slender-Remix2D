import  pygame
from tkinter import *
import time
from PIL import Image
from PIL import ImageTk
import schedule
import random


# Creer une fenetre
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

# Lance le niveaux 1
fileName = 'ressources/level/1.csv'
# matrice used to display the board
lab = []
# starting position
start_position = [1, 1]
# human position
human_position = start_position


with open(fileName, "r") as file:
    # decode and get the column and row number
    first_line = file.readline()
    row_and_column = first_line.replace('\n', '').split(",")
    row_and_column = [int(i) for i in row_and_column]
    for line in file:
        data = line.replace('\n', '').split(",")
        data = [int(i) for i in data]
        lab.append(data)
    column_number = len(data)
    row_number = len(lab)
    end_position = [row_number - 2, column_number - 2]
file.close()

def jouer(fenetre, lab):
    # affiche la matrice
    for i in lab:
        print(i)
    for widget in fenetre.winfo_children():
        widget.pack_forget()
    title = Label(fenetre, text="Slender Remix 2D ", font=("caveat", 40), bg="black", fg="white")
    # Ajoute le titre
    title.pack()
    # Creation d'une frame
    global frame
    frame = Frame(fenetre, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    global canvas1
    # Création d'un canvas : zone graphique dédié et modifiable
    canvas1 = Canvas(frame, width=1080, height=720, background='white')
    carreau = [[canvas1.create_rectangle(i * 40, j * 40, (i + 1) * 40, (j + 1) * 40)
                for i in range(14)] for j in range(19)]
    # max i 26 max j 18
    canvas1.pack()
    #mur
    mur = Image.open("ressources/images/jeu/buisson.jpg")  # PIL solution
    mur = mur.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    mur = ImageTk.PhotoImage(mur)  # convert to PhotoImage
    #perso
    perso = Image.open("ressources/images/jeu/human.jpg")  # PIL solution
    perso = perso.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    perso = ImageTk.PhotoImage(perso)  # convert to PhotoImage
    #slender
    slender = Image.open("ressources/images/jeu/slenderpng.jpg")  # PIL solution
    slender = slender.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    slender = ImageTk.PhotoImage(slender)  # convert to
    #pages à ramasser
    pages = Image.open("ressources/images/jeu/page.jpg")  # PIL solution
    pages = pages.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    pages = ImageTk.PhotoImage(pages)  # convert to PhotoImage
    #portails de sortie
    sortie = Image.open("ressources/images/jeu/portail.jpg")  # PIL solution
    sortie = sortie.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    sortie = ImageTk.PhotoImage(sortie)  # convert to PhotoImage
    #chemin
    terre = Image.open("ressources/images/jeu/terre.jpg")  # PIL solution
    terre = terre.resize((40, 40), Image.ANTIALIAS)  # The (250, 250) is (height, width)
    terre = ImageTk.PhotoImage(terre)  # convert to PhotoImage
    x = 0
    y = 0
    global page
    page = 0
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
                page = page + 1
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
    if (page == 0):
        title2 = Label(frame, text="Trouvez la sortie vite !!!", font=("caveat", 40), bg="black",
                       fg="white")
        # Ajoute le titre
        title2.pack()
    else :
            title2 = Label(frame, text="Nombre de pages restantes : " + str(page) + "", font=("caveat", 40), bg="black",
                       fg="white")
            title2.pack()


    fenetre.bind("<Key>", key_pressed)
    # Affiche la fenetre
    fenetre.mainloop()

def key_pressed(event):
    if (event.char == "q"):
        for row in lab:
            for i in row:
                if (i == 22):
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if (lab[ligne][colonne - 1] == 99):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne - 1] = 22
                        jouer(fenetre, lab)
                    if (lab[ligne][colonne - 1] == 33):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne - 1] = 22
                        jouer(fenetre, lab)
                    if (lab[ligne][colonne - 1] == 44 and page == 0):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne - 1] = 22
                        print("vous avez gagné")

    if (event.char == "d"):
        for row in lab:
            for i in row:
                if (i == 22):
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if (lab[ligne][colonne+1] == 99):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne+1] = 22
                        jouer(fenetre, lab)
                    if (lab[ligne][colonne+1] == 33):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne+1] = 22
                        jouer(fenetre, lab)
                    if (lab[ligne][colonne+1] == 44 and page == 0):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne+1] = 22
                        print("vous avez gagné")

    if (event.char == "z"):
        for row in lab:
            for i in row :
                if (i ==  22) :
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if(lab[ligne-1][colonne] == 99) :
                        lab[ligne][colonne] = 99
                        lab[ligne- 1][colonne] = 22
                        jouer(fenetre,lab)
                    if(lab[ligne-1][colonne] == 33) :
                        lab[ligne][colonne] = 99
                        lab[ligne- 1][colonne] = 22
                        jouer(fenetre,lab)
                    if(lab[ligne-1][colonne] == 44 and page == 0) :
                        lab[ligne][colonne] = 99
                        lab[ligne- 1][colonne] = 22
                        print("vous avz gagné")

    if (event.char == "s"):
        for row in lab:
            for i in row :
                if (i ==  22) :
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if(lab[ligne+1][colonne] == 99) :
                        lab[ligne][colonne] = 99
                        lab[ligne+ 1][colonne] = 22
                        jouer(fenetre,lab)
                    if (lab[ligne + 1][colonne] == 33):
                        lab[ligne][colonne] = 99
                        lab[ligne + 1][colonne] = 22
                        jouer(fenetre, lab)
                    if (lab[ligne + 1][colonne] == 44 and page == 0):
                        lab[ligne][colonne] = 99
                        lab[ligne + 1][colonne] = 22
                        print("vous avez gagné")



jouer(fenetre, lab)