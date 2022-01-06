def findWidth(liste):
    width = 50
    aliste = liste[len(liste) - 1]
    for i in range (0, len(liste)):
        if liste[i] == aliste + 1:
            width += 50
        
        aliste = liste[i]
    return width


def findHeight(liste):
    pass

def lol():
    rectToDraw = []
    run = True
    locID = 1
    liste = []
    Xline = 1
    Yline = 1
    haut = 1

    Maph=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,
          0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,
          0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,
          0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    while run:
        if Maph[locID] == 1:
            if len(liste) != 0:
                #if dernier == 1
                if (((Yline*20)-20)+Xline) - liste[len(liste) - 1] == 1:
                    liste.append(locID)
                
                #sinon if en haut == 1
                elif (((Yline - 1)*20)-20)+Xline == liste[len(liste) - 1]:
                    liste.append(locID)
                    haut += 1

                #sinon fini et ajouter ce rectangle a la liste a dessiner plus tard
                else:
                    rectToDraw.append((locID, findWidth(liste),haut*50, 50, 50))
                    liste.clear()
                    haut = 0
                    print(rectToDraw)

            else:
                liste.append(locID)

        #print(rectToDraw)
        if Xline != 20:
            Xline += 1

        else:
            Xline = 1
            Yline += 1


        locID += 1

        if locID == len(Maph):
            run = False