#!/usr/bin/python3.6
# -*-coding:Utf-8 -*

from initialiser import *
from competiteur import *
from gesionnaire_ui import *

def main():
    #import des données csv et stockage des competiteurs dans un dictionnaire {nom_cat:[competiteur1,competiteur2,etc]}
    competiteurs=Initialiser().competiteurs_par_categorie

    gestionnnaire_UI=GestionnaireUI(competiteurs)

    #chargement de l'UI et connection à la classe contenant ses méthodes
    gui_builder=Gtk.Builder()
    gui_builder.add_from_file('GUI.glade')
    gui_builder.connect_signals(gestionnnaire_UI)

    #instanciation de la fenêtre principale
    fenetre=gui_builder.get_object('f_principale')
    fenetre.set_title("Championat Poomsae")

    #permet l'arrêt du programme en cas de clic sur la croix
    fenetre.connect('delete-event',Gtk.main_quit)
    
    #affichage des widgets et lancement de la boucle d'évenements
    fenetre.show_all()
    Gtk.main()
    
if __name__=='__main__':
    main()