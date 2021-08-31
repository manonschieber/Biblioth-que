from bibliotheque import *


# Creation d'une bibliotheque
b = Bibliotheque('Bibliotheque ECL')

# Ajout de lecteurs
b.ajout_lecteur('Duval','Pierre','rue de la Paix',1,0)
b.ajout_lecteur('Dupond','Laurent','rue de la Gare',2,0)
b.ajout_lecteur('Martin','Marie','rue La Fayette',3,0)
b.ajout_lecteur('Dubois','Sophie','rue du Stade',4,0)

# Ajout de livres
b.ajout_livre('Le Pere Goriot','Honore de Balzac',101,2,2)
b.ajout_livre("Les Hauts de Hurlevent",'Emilie Bronte',102,2,2)
b.ajout_livre('Le Petit Prince','Antoine de Saint Exupery',103,2,2)
b.ajout_livre("L'Etranger",'Albert Camus',104,2,2)


# # Affichage des lecteurs et des livres
# print('\n--- Liste des lecteurs :')
# print('-------------------------------')
# b.affiche_lecteurs()
# 
# print('\n--- Liste des livres :')
# print('-------------------------------')
# b.affiche_livres()


# # Recherches de lecteurs par numero
# print('\n--- Recherche de lecteurs par numéro:')
# print('-------------------------------')
# 
# if b.chercher_lecteur_numero(1)[0]==True:
#     print(b.chercher_lecteur_numero(1)[1])
# else:
#     print('Lecteur non trouve')
#     
# lect = b.chercher_lecteur_numero(6)
# if b.chercher_lecteur_numero(6)[0]==True:
#     print(b.chercher_lecteur_numero(6)[1])
# else:
#     print('Lecteur non trouve')
#     
#     
# # Recherches de lecteurs par nom
# print('\n--- Recherche de lecteurs par nom :')
# print('-------------------------------')
# 
# if b.chercher_lecteur_nom('Martin','Marie')[0]==True:    
#     print(b.chercher_lecteur_nom('Martin','Marie')[1])
# else:
#     print('Lecteur non trouve')
# 
# if b.chercher_lecteur_nom('Le Grand','Paul')[0]==True:   
#     print(b.chercher_lecteur_nom('Le Grand','Paul')[1])
# else:
#     print('Lecteur non trouve')
        

    
    
# # Recherches de livres par numero
# print('\n--- Recherche de livres :')
# print('-------------------------------')
# 
# if b.chercher_livre_numero(101)[0]==True:
#     print('Livre trouve :',b.chercher_livre_numero(101)[1])
# else:
#     print('Livre non trouve')
#     
# if b.chercher_livre_numero(106)[0]==True:
#     print('Livre trouve :',b.chercher_livre_numero(106)[1])
# else:
#     print('Livre non trouve')
#     
#     
# # Recherches de livres par titre
# if b.chercher_livre_titre('Le Pere Goriot')[0]==True:
#     print('Livre trouve :',b.chercher_livre_titre('Le Pere Goriot')[1])
# else:
#     print('Livre non trouve')
#     
# if b.chercher_livre_titre('Madame Bovarie')[0]==True:
#     print('Livre trouve :',b.chercher_livre_titre('Madame Bovarie')[1])
# else:
#     print('Livre non trouve')
    
    
# Quelques emprunts

b.emprunt_livre(1,101,1)
b.emprunt_livre(1,104,1)
b.emprunt_livre(2,101,1)
b.emprunt_livre(2,105,1)
b.emprunt_livre(3,101,1)
b.emprunt_livre(3,104,1)
b.emprunt_livre(4,102,1)
b.emprunt_livre(4,103,1)


# # Affichage des emprunts, des lecteurs et des livres
# print('\n--- Liste des emprunts :')
# print('-------------------------------')
# b.affiche_emprunts()
# 
# print('\n--- Liste des lecteurs :')
# print('-------------------------------')
# b.affiche_lecteurs()
# 
# print('\n--- Liste des livres :')
# print('-------------------------------')
# b.affiche_livres()


# # Quelques retours de livres
# # print('\n--- Quelques retours de livres :')
# # print('-------------------------------')
# b.retour_livre(1,101)
# b.retour_livre(1,102)
# b.retour_livre(3,104)
# b.retour_livre(10,108)
# 
# 
# # Affichage des emprunts, des lecteurs et des livres
# print('\n--- Liste des emprunts :')
# print('-------------------------------')
# b.affiche_emprunts()
# 
# print('\n--- Liste des lecteurs :')
# print('-------------------------------')
# b.affiche_lecteurs()
# 
# print('\n--- Liste des livres :')
# print('-------------------------------')
# b.affiche_livres()


# Suppression de quelques livres
print(b.retrait_livre(101))

print(b.retour_livre(2,101))



# Suppression de quelques lecteurs
print(b.retrait_lecteur(1))

print(b.retour_livre(1,104))

print(b.retrait_lecteur(1))


# Affichage des emprunts, des lecteurs et des livres
print('\n--- Liste des emprunts :')
print('-------------------------------')
b.affiche_emprunts()

print('\n--- Liste des lecteurs :')
print('-------------------------------')
b.affiche_lecteurs()

print('\n--- Liste des livres :')
print('-------------------------------')
b.affiche_livres()