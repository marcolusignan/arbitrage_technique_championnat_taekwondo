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
        self.index_poomsae_en_cours=0
        self.passage_termine=False

        self.tour_en_cours=""
        
        self.notes_arbitres=[]
        self.notes_valides=False

        #stockage des ID des widgets
        self.entries_arbitres=[]
        self.labels_notes_poomsaes=[]

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
        if self.poomsae2_en_cours==": AUCUN":
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

    #initialisation des labels sur la vue competiteur
    def set_identite_competiteur_su_vc(self,l_identite_competiteur_vc):
        l_identite_competiteur_vc.set_text("{} {}".format(self.competiteur_en_cours.nom,self.competiteur_en_cours.prenom))
    def set_tour_categorie_sur_vc(self,l_tour_categorie_vc):
        l_tour_categorie_vc.set_text("{}  {}".format(self.tour_en_cours,self.categorie_en_cours))
    def set_poomsae1_sur_vc(self,l_poomsae1_vc):
        l_poomsae1_vc.set_text("Poomsae {}".format(self.poomsae1_en_cours))
    def set_poomsae2_sur_vc(self,l_poomsae2_vc):
        l_poomsae2_vc.set_text("Poomsae {}".format(self.poomsae2_en_cours))
    #prévoir récupération de l'ID des labels poomsae VC pour mettre en gras le poomsae en cours

#--------------Callbacks des notes arbitres-----------------------------------------------#

    def get_note_arbitre_1(self,e_arb1):
        if e_arb1.get_text()!="":
            self.notes_arbitres.append(e_arb1.get_text())
            self.entries_arbitres.append(e_arb1)
    def get_note_arbitre_2(self,e_arb2):
        if e_arb2.get_text()!="":
            self.notes_arbitres.append(e_arb2.get_text())
            self.entries_arbitres.append(e_arb2)
    def get_note_arbitre_3(self,e_arb3):
        if e_arb3.get_text()!="":
            self.notes_arbitres.append(e_arb3.get_text())
            self.entries_arbitres.append(e_arb3)
    def get_note_arbitre_4(self,e_arb4):
        if e_arb4.get_text()!="":
            self.notes_arbitres.append(e_arb4.get_text())
            self.entries_arbitres.append(e_arb4)
    def get_note_arbitre_5(self,e_arb5):
        if e_arb5.get_text()!="":
            self.notes_arbitres.append(e_arb5.get_text())
            self.entries_arbitres.append(e_arb5)

    def message_note_invalide(self,md):
        """affiche une boite de dialogue si les notes sont invalides ou vides, sinon passe self.notes_valides à True"""
        index_en_erreur=[]
        #determine l'index des entries en erreur
        for i,elt in enumerate(self.notes_arbitres):
            try:
                elt=float(elt)
                if elt <0 or elt>10:
                    raise ValueError
            except ValueError:
                index_en_erreur.append(str(i+1))
        index_en_erreur=",".join(index_en_erreur)
        #affiche un message d'erreur si une ou plusieurs entries sont en erreur
        if index_en_erreur!="":
            md.format_secondary_text("Merci de saisir une valeur numérique comprise entre 0 et 10 pour le(s) arbitre(s) {}".format(index_en_erreur))
            md.run()
            md.hide()
            self.notes_arbitres.clear()
        #affiche un message d'erreur si toutes les entries sont vides
        elif self.notes_arbitres==[]:
            md.format_secondary_text("Aucune note n'a été saisie")
            md.run()
            md.hide()
        #valide et convertie en float les notes des arbitres
        else:
            self.notes_valides=True
            self.notes_arbitres=[float(note)for note in self.notes_arbitres]
        index_en_erreur=""

    def get_label_poomsae_1(self,l_note_poomsae1):
        """stocke l'ID du label poomsae1 dans self.labels_notes_poomsaes"""
        if len(self.labels_notes_poomsaes)<1:
            self.labels_notes_poomsaes.append(l_note_poomsae1)
    def get_label_poomsae_2(self,l_note_poomsae2):
        """stocke l'ID du label poomsae2 dans self.labels_notes_poomsaes"""
        if len(self.labels_notes_poomsaes)<2:
            self.labels_notes_poomsaes.append(l_note_poomsae2)

# ajouter un effet de transition du poomsae 1 à 2 sur vc
    def set_note_poomsae_en_cours(self,l_note_vc):
        """Calcule la note du poomsae en cours, l'affecte au competiteur en cours et l'affiche dans le label de l'UI admin"""
        if self.notes_valides==True and self.passage_termine==False:
            #calcule la note
            note_poomsae_en_cours=0
            for note in self.notes_arbitres:
                note_poomsae_en_cours+=note
            note_poomsae_en_cours/=len(self.notes_arbitres)
            note_poomsae_en_cours=round(note_poomsae_en_cours,3)
            l_note_vc.set_text("{}".format(note_poomsae_en_cours))
            #vide la liste des notes et les entries arbitres
            self.notes_arbitres.clear()
            for entry in self.entries_arbitres:
                entry.set_text("")
            self.entries_arbitres.clear()
            # cas sans poomsae 2
            if self.nb_poomsae_a_presenter==1:
                self.competiteur_en_cours.note_poomsae1=note_poomsae_en_cours
                self.labels_notes_poomsaes[0].set_text("Note Poomsae 1 : \n {}".format(note_poomsae_en_cours))
                self.labels_notes_poomsaes[1].set_text("Note Poomsae 2 : \n NC ")
                self.passage_termine=True                        
            # cas passage 1 poomsae 2
            elif self.nb_poomsae_a_presenter==2 and self.index_poomsae_en_cours==0:
                self.competiteur_en_cours.note_poomsae1=note_poomsae_en_cours
                self.labels_notes_poomsaes[0].set_text("Note Poomsae 1 : \n {}".format(note_poomsae_en_cours))
                self.index_poomsae_en_cours+=1
            # cas 2e passage poomsae 2
            elif self.nb_poomsae_a_presenter==2 and self.index_poomsae_en_cours==1:
                self.competiteur_en_cours.note_poomsae2=note_poomsae_en_cours
                self.labels_notes_poomsaes[1].set_text("Note Poomsae 2 : \n {}".format(note_poomsae_en_cours))
                self.index_poomsae_en_cours=0
                self.passage_termine=True

# ajouter un message d erreur si validation alors que les notes sont déja validées

#-------------------Callbacks compétiteur suivant-------------------------------------------#

    def message_competiteur_suivant_invalide(self,md):
        """affiche une boite de dialogue d'erreur si le compétiteur en cours n'a pas terminé son passage ou si tous les compétiteurs sont passés"""
        if self.passage_termine==False:
            md.format_secondary_text("{} {} n'a pas terminé son passage".format(self.competiteur_en_cours.nom,self.competiteur_en_cours.prenom))
            md.run()
            md.hide()
        elif self.passage_termine==True and self.ordre_passage_competiteur_en_cours>=self.nb_competiteur_categorie_en_cours:
            md.format_secondary_text("Tous les compétiteurs de la catégorie sont passés")
            md.run()
            md.hide()
            
# initialisation : 
# - remettre a False self.passage_termine 
# - remettre a 0 index poomsae en cours
# - vider les labels note poomsae 1 et note poomsae 2
# - vider le label note sur vc
# 
# chargement du competiteur suivant(modifier self.competiteur_en_cours) et mise a jour des labels :
#   - nom prenom sur UI admin
#   - nom prenom sur vc
#   - incrementer self.ordre_passage_competiteur_en_cours et mettre a jour label ordre passage

