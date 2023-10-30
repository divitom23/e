#cree par max divito
#creer en 2024
#projet de combat tp 3


from random import randint as e

#defenir les variables et expliquer les regles du jeu
victoireConsequtifs = 0
pv = 20
forceMonstre = e(1, 11)
choixMenu = 0
deeCombat = 0
deeCombat2 = 0
totalDee = 0
print("vous vous retrouver dans un couloir remplie de portes. chaque porte contient des monstres que vous devez combattre.")
print("vous commencer la partie avec 20 point de vie et vous perdez 1 si vous choisisser de combattre un monstre et si vous perder la batail contre un monstre, vous perder le nombre de vie egale au pouvoir du monstre")

#boucle while qui fait que le jeu continue a jouer
while pv > 0:

    #definir si le monstre est un boss ou pas
    if victoireConsequtifs %3== 0 and victoireConsequtifs > 0:
        print("vous tomber contre le boss avec pouvoir de 6-11")
        forceMonstre = e(6,11)
        print('Que voulez-vous faire ?')
        choixMenu = int(input('1- combatre ladversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie'))

    else:
        print('Vous tombez face à face avec un adversaire de difficulté : %d' %(forceMonstre))
        print('Que voulez-vous faire ?')
        choixMenu = int(input('1- combatre ladversaire\n2- Contourner cet adversaire et aller ouvrir une autre porte\n3- Afficher les règles du jeu\n4- Quitter la partie'))

        #choix de combattre le monstre
    if choixMenu == 1:
        print('vous combatter le monstre')
        deeCombat = e(1, 6)
        deeCombat2 = e(1, 6)
        totalDee = deeCombat + deeCombat2
        print("vous rouler un %d et un %d pour un total de %d" %(deeCombat, deeCombat2, totalDee ))
        if totalDee > forceMonstre:
            victoireConsequtifs = victoireConsequtifs + 1
            print("bravo, vous avez vaincu le monstre ")
            print("%d point de vie restant" %(pv))
            print("vous avez %d victoires consequtifs." %(victoireConsequtifs))


        else:
            pv = pv - forceMonstre
            victoireConsequtifs = 0
            print("vous perdez le combat")
            print("vous avez mantenant %d vies restant"%(pv))
        forceMonstre = e(1, 11)

    #choix d'eviter le monstre
    elif choixMenu == 2:
        pv = pv - 1
        print('Vous contourner le monstre et vous perdez un point de vie')
        print("points de vies: %d" %(pv))

        print("vous avez maintenant 0 victoires consequtifs")
        forceMonstre = e(1, 11)

    #choix de verifier les regles
    elif choixMenu == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
    # choix de quitter le jeu et terminer la boucle
    elif choixMenu == 4:
        print('merci et au revoir')
        exit()
    else:
        print("vous avez missclick, essailler encore")

print("vous perdez le combat")
#maz