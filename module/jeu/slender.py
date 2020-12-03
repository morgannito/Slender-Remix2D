def slenderMove():
    d = random.randint(0, 3)
    if (d == 0):
        for row in lab:
            for i in row:
                if (i == 22):
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if (lab[ligne][colonne - 1] == 99):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne - 1] = 22
                        jouer(fenetre, lab)

    if (d == 1):
        for row in lab:
            for i in row:
                if (i == 22):
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if (lab[ligne][colonne + 1] == 99):
                        lab[ligne][colonne] = 99
                        lab[ligne][colonne + 1] = 22
                        jouer(fenetre, lab)

    if (d == 2):
        for row in lab:
            for i in row:
                if (i == 22):
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if (lab[ligne - 1][colonne] == 99):
                        lab[ligne][colonne] = 99
                        lab[ligne - 1][colonne] = 22
                        jouer(fenetre, lab)

    if (d == 3):
        for row in lab:
            for i in row:
                if (i == 22):
                    ligne = lab.index(row)
                    colonne = row.index(i)
                    if (lab[ligne + 1][colonne] == 99):
                        lab[ligne][colonne] = 99
                        lab[ligne + 1][colonne] = 22
                        jouer(fenetre, lab)