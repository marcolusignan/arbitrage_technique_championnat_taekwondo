#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

import os
from competiteur import *
from random import shuffle

class Initialiser():
    """Classe permettant de récupérer dans une liste de tuples les données des compétiteurs"""

    def __init__(self):
        """lors de l'appel du constructeur, importe les données compétiteurs depuis des fichiers csv
        les trie par catégorie dans un dictionnaire d'objets compétiteurs """
        self.charger_repertoire_csv()
        self.noms_fichiers_csv=os.listdir(os.getcwd())
        self.donnees_competiteurs=[]
        self.charger_donnees_competiteurs()
        self.competiteurs_par_categorie={}
        self.instancier_competiteurs()
        self.melanger_ordre_passage()

    def charger_repertoire_csv():
        """place le programme dans le répertoire contenant les fichiers .csv"""
        classeur_path='fichiers_csv'
        os.chdir(classeur_path)
    charger_repertoire_csv=staticmethod(charger_repertoire_csv)

    def charger_donnees_competiteurs(self):
        """parcours chaque fichier csv, convertit chaque ligne (sauf en-tete) en tuple
        et met à jour la liste des competiteurs"""
        
        for fichier_csv in self.noms_fichiers_csv:
            fichier=open(fichier_csv,"r")
            contenu=fichier.read()
            fichier.close()
            contenu=contenu.replace("\n",",")
            contenu=contenu.split(",")
            del contenu[0:4]
            del contenu[len(contenu)-1]
    
            nb_competiteurs_a_inserer=len(contenu)/4
            borne1=0
            borne2=4
            while nb_competiteurs_a_inserer>0:
                tuple_a_inserer=contenu[borne1:borne2]
                tuple_a_inserer=tuple(tuple_a_inserer)
                self.donnees_competiteurs.append(tuple_a_inserer)
                borne1+=4
                borne2+=4
                nb_competiteurs_a_inserer-=1
        os.chdir("..")

    def instancier_competiteurs(self):
        """Instancie les compétiteurs, créé une liste de competiteurs pour chaque catégorie
        regroupe les 16 listes dans le dictionnaire self.competiteur_par_categorie """
        
        liste_competiteurs=[]

        for competiteur in self.donnees_competiteurs:
            liste_competiteurs.append(Competiteur(*competiteur))

        noms_categories=("M Cadet","M Junior","M Senior 1","M Senior 2","M Master 1","M Master 2","M Master 3","M Master 4","F Cadet","F Junior","F Senior 1","F Senior 2","F Master 1","F Master 2","F Master 3","F Master 4")

        for categorie in noms_categories:
            self.competiteurs_par_categorie[categorie]=[competiteur for competiteur in liste_competiteurs if competiteur.categorie==categorie]

    def melanger_ordre_passage(self):
        """mélange alétoirement l'ordre de passage dans chaque catégorie"""
        for categorie in self.competiteurs_par_categorie.keys():
            shuffle(self.competiteurs_par_categorie[categorie])

