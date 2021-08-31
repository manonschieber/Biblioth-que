class Bibliotheque:
    def __init__(self,n):
        self.__nom=n
        self.__lecteurs=[]
        self.__bibliothecaires=[]
        self.__livres=[]
        self.__emprunts=[]
        
    def get_nom(self):     
        return self.__nom

    def set_nom(self,n):   #les opérations set sont pour modifier un attribut
        self.__nom=n

    def get_livres(self):     #retourne la liste des livres de la bibliothèque
        return self.__livres
        
    def get_lecteurs(self):
        return self.__lecteurs

    def get_emprunts(self):
        return self.__emprunts

    def ajout_lecteur(self, nom, prenom, adresse, num, nbemprunts):
        if (Bibliotheque.chercher_lecteur_numero(self,num))[0]==False:  #Si le lecteur n'existe pas déjà dans la base de données
            lecteur=Lecteur(nom,prenom,adresse,num,nbemprunts)
            self.__lecteurs.append(lecteur)    #On l'ajoute à la liste de lecteurs

    def retrait_lecteur(self,numlecteur):
        if Bibliotheque.chercher_lecteur_numero(self,numlecteur)[0]==True:     #Si le lecteur existe déjà dans la base de données
            lecteur=Bibliotheque.chercher_lecteur_numero(self,numlecteur)[1]
            for e in self.__emprunts:   #on retire déjà tous ses emprunts
                if e.get_numlecteur()==numlecteur:
                    for i in range(100,200):
                        Bibliotheque.retour_livre(self,numlecteur,i)
            self.__lecteurs.remove(lecteur)     #On le retire de cette liste
            return "Retrait du lecteur effectué"
        return "Retrait du lecteur impossible"

    def ajout_livre(self,auteur,titre,num, nbtotal, nbdispos):
        if Bibliotheque.chercher_livre_titre(self,titre)[0]==True:    #le livre existe déjà dans la bibliothèque
            livre=Bibliotheque.chercher_livre_titre(self,titre)[1]
            livre.set_nb_total(livre.get_nb_total()+1)    #Le nombre total d'exemplaires de ce livre augmente de 1
            livre.set_nb_dispo(livre.get_nb_dispo()+1)     #Le nombre total d'exemplaires de ce livre augmente de 1
        else:     #le livre n'existe pas encore dans la bibliothèque
            livre=Livre(titre,auteur,num,nbtotal, nbdispos)    
            self.__livres.append(livre)    #on ajoute ce livre à la liste des livres de la bibliothèque
            livre.set_nbtotal(livre.get_nbtotal()+1)      #Le nombre total d'exemplaires de ce livre augmente de 1
            livre.set_nbdispos(livre.get_nbdispos()+1)      #Le nombre total d'exemplaires de ce livre augmente de 1

    def retrait_livre(self,num):
        if Bibliotheque.chercher_livre_numero(self,num)[0]==True:    #si le livre existe dans la bibliothèque
            livre=Bibliotheque.chercher_livre_numero(self,num)[1]    #on récupère les attributs de ce livre
            livre.set_nbtotal(livre.get_nbtotal()-1)     #Le nombre total d'exemplaires de ce livre diminue de 1
            livre.set_nbdispos(livre.get_nbdispos()-1)      #Le nombre total d'exemplaires de ce livre diminue de 1
            if livre.get_nbtotal()==0:   #si c'était le dernier exemplaire
                self.__livres.remove(livre)   #on le retire de la liste de livres de la biliothèque
            return "Le livre a été retiré"

    def ajout_bibliothecaire(self,nom,prenom,adresse,num):
        if Bibliotheque.chercher_bibliothecaire_numero(self,num)[0]==False:    #si le bibliothécaire n'est pas déjà dans la bibliothèque
            b=Bibliothecaire(nom,prenom,adresse,num)   
            self.__bibliothecaires.append(b)    #on l'ajoute

    def retrait_bibliothecaire(self,num):
        if Bibliotheque.chercher_bibliothecaire_numero(self,num)[0]==True:    #si le bibliothécaire est déjà dans la bibliothèque
            b=Bibliotheque.chercher_bibliothecaire_numero(self,num)[1]
            self.__bibliothecaires.remove(b)    #on le retire

    def affiche_lecteurs(self):   
        for l in self.__lecteurs:
            print('-------------------------------')
            print('Nom:',l.get_nom(),'Prenom:',l.get_prenom(),'Adresse:',l.get_adresse(),'Numéro',l.get_num(),"Nombre d'emprunts",l.get_nbemprunts())    #on affiche les différents attributs de chaque lecteur

    def affiche_livres(self):
        for l in self.__livres:
            print('-------------------------------')
            print('Titre:',l.get_titre(),'auteur:',l.get_auteur(),'nb total:',l.get_nbtotal(),'nb dispos',l.get_nbdispos())    #on affiche les différents attributs de chaque livre

    def affiche_emprunts(self):    
        for e in self.__emprunts:
            print('-------------------------------')
            print('Numéro de lecteur:',e.get_numlecteur(),'Numéro de livre:',e.get_numlivre(),"Bibliothecaire responsable:",e.get_bibliothecaire())     #on affiche les différents emprunts

    def chercher_bibliothecaire_numero(self,n):
        for b in self.__bibliothecaires:    #On parcourt la liste de bibliothécaires
            if b.get_num()==n:    #on cherche le bibliothécaire ayant le même numéro que celui donné en argument
                return [True,b]     
        return [False]

    def chercher_lecteur_numero(self,n):    
        for lect in self.__lecteurs:    #On parcourt la liste de lecteurs
            if lect.get_num()==n:     #on cherche le lecteur ayant le même numéro que celui donné en argument
                return [True,lect]
        return [False]

    def chercher_lecteur_nom(self,n,p):
        for lect in self.__lecteurs:   #On parcourt la liste de lecteurs
            if (lect.get_nom())==n:    #on cherche le lecteur ayant le même nom que celui donné en argument
                if (lect.get_prenom())==p:    #on cherche le lecteur ayant le même prénom que celui donné en argument
                    return [True,lect]
        return [False]

    def chercher_livre_numero(self,n):
        for livre in Bibliotheque.get_livres(self):    #On parcourt la liste de livres
            if (livre.get_num())==n:    #on cherche le livre ayant le même numéro que celui donné en argument
                return [True,livre]
        return [False]

    def chercher_livre_titre(self,t):
        for livre in Bibliotheque.get_livres(self):    #On parcourt la liste de livres
            if (livre.get_titre())==t:   #on cherche le livre ayant le même titre que celui donné en argument
                return [True,livre]
        return [False]

    def chercher_emprunt(self,numlecteur,numlivre):
        for e in Bibliotheque.get_emprunts(self):    #On parcourt les emprunts
            if e.get_numlivre()==numlivre:    #on cherche le livre associé à l'emprunt ayant le même numéro que celui donné en argument
                if e.get_numlecteur()==numlecteur:   #on cherche le lecteur associé à l'emprunt ayant le même numéro que celui donné en argument
                    return [True,e]   
        return [False]

    def emprunt_livre(self,numlecteur,numlivre,numbibliothecaire):
        if Bibliotheque.chercher_lecteur_numero(self,numlecteur)[0]==True:   #le lecteur existe
            if Bibliotheque.chercher_livre_numero(self,numlivre)[0]==True:    #le livre existe
                livre=Bibliotheque.chercher_livre_numero(self,numlivre)[1]
                if livre.get_nbdispos()!=0:       #on vérifie s'il reste des exemplaires disponibles
                    if Bibliotheque.chercher_emprunt(self,numlecteur,numlivre)[0]==False:   #l'emprunt n'a pas déjà été effectué
                        livre.set_nbdispos(livre.get_nbdispos()-1)
                        emprunt=Emprunt(numlecteur,numlivre,numbibliothecaire)   #on enregistre l'emprunt
                        self.__emprunts.append(emprunt)   #on l'ajoute à la liste des emprunts
                        lecteur=Bibliotheque.chercher_lecteur_numero(self,numlecteur)[1]
                        lecteur.set_nbemprunts(lecteur.get_nbemprunts()+1)

    def retour_livre(self,numlecteur,numlivre):
        if Bibliotheque.chercher_livre_numero(self,numlivre)[0]==True:    #le livre existe
            livre=Bibliotheque.chercher_livre_numero(self,numlivre)[1]
            if Bibliotheque.chercher_lecteur_numero(self,numlecteur)[0]==True:   #le lecteur existe
                lecteur=Bibliotheque.chercher_lecteur_numero(self,numlecteur)[1]
                if Bibliotheque.chercher_emprunt(self,numlecteur,numlivre)[0]==True:   #l'emprunt existe
                    emprunt=Bibliotheque.chercher_emprunt(self,numlecteur,numlivre)[1]
                    self.__emprunts.remove(emprunt)   #on supprime l'emprunt
                    livre.set_nbdispos(livre.get_nbdispos()+1)    #on remet le livre à disposition
                    lecteur.set_nbemprunts(lecteur.get_nbemprunts()-1)    #on retire un emprunt au lecteur
                    return "Retour du livre effectué"
        return "Retour du livre impossible"

class Emprunt(Bibliotheque):
    def __init__(self,numlecteur,numlivre,bibliothecaire):
        self.__numlecteur=numlecteur
        self.__numlivre=numlivre
        self.__bibliothecaire=bibliothecaire

    def get_numlecteur(self):
        return self.__numlecteur

    def get_numlivre(self):
        return self.__numlivre

    def get_bibliothecaire(self):
        return self.__bibliothecaire


class Livre(Bibliotheque):
    def __init__(self,titre,auteur,numéro,nbtotal,nbdispos):
        self.__titre=titre
        self.__auteur=auteur
        self.__num=numéro      #numéro de livre
        self.__nbtot=nbtotal   #nombre d'exemplaires achetés
        self.__nbdispos=nbdispos   #nombre d'exemplaires disponibles à l'emprunt

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_num(self):
        return self.__num

    def get_nbtotal(self):
        return self.__nbtot

    def get_nbdispos(self):
        return self.__nbdispos

    def set_nbtotal(self,n):
        self.__nbtot=n

    def set_nbdispos(self,n):
        self.__nbdispos=n


class Personne:
    def __init__(self,nom,prenom,adresse):
        self.__nom=nom
        self.__prenom=prenom
        self.__adresse=adresse

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_adresse(self):
        return self.__adresse

    def set_adresse(self,ad):
        self.__adresse=ad

    def set_nom(self,n):
        return self.__nom
    

class Lecteur(Personne):
    def __init__(self,nom, prenom, adresse,num,nbemprunts):
        Personne.__init__(self,nom,prenom,adresse)
        self.__num=num
        self.__nbemprunts=nbemprunts
        
    def get_num(self):
        return self.__num

    def get_nbemprunts(self):
        return self.__nbemprunts

    def set_nbemprunts(self,n):
        self.__nbemprunts=n


class Bibliothecaire(Personne):
    def __init__(self,nom,prenom,adresse,numéro):
        Personne.__init__(self,nom,prenom,adresse)
        self.__num=numéro

    def get_num(self):
        return self.__num



    
        
    
        