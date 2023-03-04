#importation du module random
import random

#declaration des illustrations
pierre='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


papier='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

ciseaux='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#fin declaration

#creation d'une liste contenant les illustrations
tab=[pierre,papier,ciseaux]

#affichage message de bienvenue
print("Bienvenue a vous. Amusons nous un peu...")

#affichage des outils du jeu
print(f"PIERRE:{tab[0]}\n  PAPIER:{tab[1]}\n CISEAUX:{tab[2]}")

#recuperation du choix de l'utilisateur
choixUser=int(input("Que choisissez vous? Tapez 1 pour 'Pierre', 2 pour 'Papier' et 3  pour 'Ciseaux': "))

#verification de la validité de saisie de l'utilisateur
if choixUser<0 or choixUser>3:
  print("Vous avez fait une mauvaise saisie. Fin de la partie.")

#condition verifiee, suite de l'excecution
else:

  #affichage du choix de l'utilisateur
  print(f"Votre choix:\n{tab[choixUser-1]}")

  #choix de l'ordinateur
  choixComputer=(random.randint(0,2))

  #affichage du choix de l'ordinateur
  print(f"L'ordinateur a choisi:\n{tab[choixComputer]}")
  
  #verification de la condition de match nul
  if choixUser-1==choixComputer:
    print("Match nul")

  #si pas de match nul, verification du sort de l'utilisateur
  else:
    #conditions d'echec
    if (choixUser==1 and choixComputer==1) or (choixUser==2 and choixComputer==2) or (choixUser==3 and choixComputer==0):
      print("Vous avez perdu!")
    #condition de victoire
    else:
      print("Vous avez gagné")