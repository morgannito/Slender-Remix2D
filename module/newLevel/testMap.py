import  pygame
from tkinter import *
import time
from PIL import Image
from PIL import ImageTk
# import schedule
import random
import module.jeu.win.winTest as winTest
import sys
import module.jeu.lose.lose as lose

# aide à transformer un string en array
import ast


# initialise la map
def init(fenetre , lab):
    # todo changé cette horreur !!
    global gameBoard, map
    gameBoard = fenetre
    # converti le string en array
    global res
    res = ast.literal_eval(lab)
    map = res
    for widget in gameBoard.winfo_children():
        widget.pack_forget()
    title = Label(gameBoard, text="Slender Remix 2D ", font=("caveat", 40), bg="black", fg="white")
    # Ajoute le titre
    title.pack()
    # Creation d'une frame
    global frame
    frame = Frame(gameBoard, bg="black")
    # Ajouter la frame
    frame.pack(expand=YES)
    # lance la function pour  jouer au jeu
    jouer(gameBoard,map)


# permet de jouer la map  et de l'enregistrer si le joueur fini le niveau
def jouer(gameBoard, map):
    # todo changé quand le client aura payé
    # gerer un probleme de recursivité pour le moment j'ai pas mieux ...
    sys.setrecursionlimit(9000)
    # supprime les anciens elements
    for widget in frame.winfo_children():
        widget.pack_forget()
    global canvas1
    # Création d'un canvas : zone graphique dédié et modifiable
    canvas1 = Canvas(frame, width=1080, height=720, background='white')
    carreau = [[canvas1.create_rectangle(i * 40, j * 40, (i + 1) * 40, (j + 1) * 40)
                for i in range(14)] for j in range(19)]
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
    # cette boucle va creer l'affichage avec des image pour chaque element de la matrice , mur, terre , humain , slender , sortie etc..
    for row in map:
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
    gameBoard.bind("<Key>", key_pressed)
    # Affiche la fenetre
    gameBoard.mainloop()

def key_pressed(event):
    # fait bouger slender à chaque touche detecter
    slenderMove()
    # verifie si le  deplacement gauche  est possible et le fait si tel est le cas
    if (event.char == "q"):
        for row in map:
            for i in row:
                if (i == 22):
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if (map[ligne][colonne - 1] == 99):
                        map[ligne][colonne] = 99
                        map[ligne][colonne - 1] = 22
                        jouer(gameBoard, map)
                    if (map[ligne][colonne - 1] == 33):
                        map[ligne][colonne] = 99
                        map[ligne][colonne - 1] = 22
                        jouer(gameBoard, map)
                    if (map[ligne][colonne - 1] == 44 and page == 0):
                        map[ligne][colonne] = 99
                        map[ligne][colonne - 1] = 22
                        winTest.win(gameBoard,res)
    # verifie si le  deplacement droite  est possible et le fait si tel est le cas
    if (event.char == "d"):
        for row in map:
            for i in row:
                if (i == 22):
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if (map[ligne][colonne + 1] == 99):
                        map[ligne][colonne] = 99
                        map[ligne][colonne + 1] = 22
                        jouer(gameBoard, map)
                    if (map[ligne][colonne + 1] == 33):
                        map[ligne][colonne] = 99
                        map[ligne][colonne + 1] = 22
                        jouer(gameBoard, map)
                    if (map[ligne][colonne + 1] == 44 and page == 0):
                        map[ligne][colonne] = 99
                        map[ligne][colonne + 1] = 22
                        winTest.win(gameBoard,res)

    # verifie si le  deplacement haut  est possible et le fait si tel est le cas
    if (event.char == "z"):
        for row in map:
            for i in row :
                if (i ==  22) :
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if(map[ligne - 1][colonne] == 99) :
                        map[ligne][colonne] = 99
                        map[ligne - 1][colonne] = 22
                        jouer(gameBoard, map)
                    if(map[ligne - 1][colonne] == 33) :
                        map[ligne][colonne] = 99
                        map[ligne - 1][colonne] = 22
                        jouer(gameBoard, map)
                    if(map[ligne - 1][colonne] == 44 and page == 0) :
                        map[ligne][colonne] = 99
                        map[ligne - 1][colonne] = 22
                        print("vous avz gagné")
                        winTest.win(gameBoard,res)
    # verifie si le  deplacement bas  est possible et le fait si tel est le cas
    if (event.char == "s"):
        for row in map:
            for i in row :
                if (i ==  22) :
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if(map[ligne + 1][colonne] == 99) :
                        map[ligne][colonne] = 99
                        map[ligne + 1][colonne] = 22
                        jouer(gameBoard, map)
                    if (map[ligne + 1][colonne] == 33):
                        map[ligne][colonne] = 99
                        map[ligne + 1][colonne] = 22
                        jouer(gameBoard, map)
                    if (map[ligne + 1][colonne] == 44 and page == 0):
                        map[ligne][colonne] = 99
                        map[ligne + 1][colonne] = 22
                        print("vous avez gagné")
                        winTest.win(gameBoard,res)
# func qui va permettre les deplacement de slender et lose la partie si slender est à coté du joueurs

def slenderMove():
    for row in map:
        for i in row:
            if (i == 66):
                ligne = map.index(row)
                colonne = row.index(i)
                if (map[ligne][colonne - 1] == 22):
                    lose.lose(gameBoard)
                if (map[ligne][colonne + 1] == 22):
                    lose.lose(gameBoard)
                if (map[ligne - 1][colonne] == 22):
                    lose.lose(gameBoard)
                if (map[ligne + 1][colonne] == 22):
                    lose.lose(gameBoard)
    d = random.randint(0, 3)
    if (d == 0):
        for row in map:
            for i in row:
                if (i == 66):
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if (map[ligne][colonne - 1] == 99):
                        map[ligne][colonne] = 99
                        map[ligne][colonne - 1] = 66

    if (d == 1):
        for row in map:
            for i in row:
                if (i == 66):
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if (map[ligne][colonne + 1] == 99):
                        map[ligne][colonne] = 99
                        map[ligne][colonne + 1] = 66

    if (d == 2):
        for row in map:
            for i in row:
                if (i == 66):
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if (map[ligne - 1][colonne] == 99):
                        map[ligne][colonne] = 99
                        map[ligne - 1][colonne] = 66

    if (d == 3):
        for row in map:
            for i in row:
                if (i == 66):
                    ligne = map.index(row)
                    colonne = row.index(i)
                    if (map[ligne + 1][colonne] == 99):
                        map[ligne][colonne] = 99
                        map[ligne + 1][colonne] = 66


