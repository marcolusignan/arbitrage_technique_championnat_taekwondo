#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class GestionnaireUI():

    def __init__(self,competiteurs):
        
        #stockage du dictionnaire des compétiteurs par catégorie
        self.competiteurs_par_categorie=competiteurs

        #initialisation des parametres de l'UI administrateur
        self.competiteur_en_cours=None
        self.ordre_passage_competiteur_en_cours=0
        self.nb_competiteur_categorie_en_cours=0

        self.categorie_en_cours=""
        
        self.poomsae1_en_cours=""
        self.poomsae2_en_cours=""
        self.nb_poomsae_a_presenter=2
        self.index_poomsae_en_cours=1

        self.tour_en_cours=""
        
        self.notes_arbitres=[]

#------------Callbacks du bouton Valider rubrique choix catégorie/poomsae-----------------#
    def get_categorie_en_cours(self,cbbox):
        """récupère la catégorie choisie"""
        self.categorie_en_cours=cbbox.get_active_text()
    def get_poomsae1_en_cours(self,cbbox):
        """récupère le poomsae 1 choisi"""
        self.poomsae1_en_cours=cbbox.get_active_text()
    def get_poomsae2_en_cours(self,cbbox):
        """récupère le poomsae 2 choisi et modifie le nb de poomsae a présenter si AUCUN est choisi"""
        self.poomsae2_en_cours=cbbox.get_active_text()
        if self.poomsae2_en_cours=="AUCUN":
            self.nb_poomsae_a_presenter=1
    
    def initialiser_competiteur_en_cours(self,l_nom_prenom):
        """affiche l'identité du 1er compétiteur de la catégorie dans le label de l'UI admin"""
        try:
            self.competiteur_en_cours=self.competiteurs_par_categorie[self.categorie_en_cours][0]
            l_nom_prenom.set_text("{} {}".format(self.competiteur_en_cours.nom,self.competiteur_en_cours.prenom))
        except IndexError:
            l_nom_prenom.set_text("Catégorie Vide")

    def message_categorie_vide(self,md):
        """ouvre une boite de dialogue si la catégorie est vide"""
        if self.competiteurs_par_categorie[self.categorie_en_cours]==[]:
            md.format_secondary_text("la catégorie choisie est vide, veuillez en choisir une autre")
            md.run()
            md.hide()

    def initialiser_ordre_passage(self,l_ordre_passage):
        """initialise l'ordre de passage et l'affiche dans le label de l'UI admin"""
        self.nb_competiteur_categorie_en_cours=len(self.competiteurs_par_categorie[self.categorie_en_cours])
        self.ordre_passage_competiteur_en_cours=1
        l_ordre_passage.set_text("{}/{}".format(self.ordre_passage_competiteur_en_cours,self.nb_competiteur_categorie_en_cours))

    def initialiser_tour_en_cours(self,l_tour_en_cours):
        if len(self.competiteurs_par_categorie[self.categorie_en_cours])<=20:
            self.tour_en_cours="Demi-Finale"
        else :
            self.tour_en_cours="1er Tour"
        l_tour_en_cours.set_text(self.tour_en_cours)

#--------------Callbacks des notes arbitres-----------------------------------------------#

    def get_note_arbitre_1(self,e_arb1):
        if e_arb1.get_text()!="":
            self.notes_arbitres.append(e_arb1.get_text())
    def get_note_arbitre_2(self,e_arb2):
        if e_arb2.get_text()!="":
            self.notes_arbitres.append(e_arb2.get_text())
    def get_note_arbitre_3(self,e_arb3):
        if e_arb3.get_text()!="":
            self.notes_arbitres.append(e_arb3.get_text())
    def get_note_arbitre_4(self,e_arb4):
        if e_arb4.get_text()!="":
            self.notes_arbitres.append(e_arb4.get_text())
    def get_note_arbitre_5(self,e_arb5):
        if e_arb5.get_text()!="":
            self.notes_arbitres.append(e_arb5.get_text())

    def message_note_invalide(self,md):
        """affiche une boite de dialogue si les notes sont invalides"""
        index_en_erreur=[]
        for i,elt in enumerate(self.notes_arbitres):
            try:
                elt=float(elt)
                if elt <0 or elt>10:
                    raise ValueError
            except ValueError:
                index_en_erreur.append(str(i+1))
        index_en_erreur=",".join(index_en_erreur)
        if index_en_erreur!="":
            md.format_secondary_text("Merci de saisir une valeur numérique comprise entre 0 et 10 pour le(s) arbitre(s) {}".format(index_en_erreur))
            md.run()
            md.hide()
            index_en_erreur=""
            self.notes_arbitres.clear()
            
    def set_note_poomsae_1(self,l_note_poomsae1):
        #doit incrementer index poomsae en cours
        # doit afficher la note dans le label
        # doit affecter la note a l instande de competiteur en cours
        pass
    
    def set_note_poomsae_2(self,l_note_poomsae2):
        pass
    
