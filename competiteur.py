#!/usr/bin/python3.6
# -*-coding:Utf-8 -*
import datetime

class Competiteur:

    def __init__(self,nom,prenom,sexe,date_naissance):
        self.nom=nom.upper()
        self.prenom=prenom.capitalize()
        self.sexe=sexe.lower()
        self.date_naissance=date_naissance
        self.age=self.affecter_age()
        self.categorie=self.affecter_categorie()
        self.note_poomsae1=0
        self.note_poomsae2=0
        self.note_finale=0

    def affecter_age(self):
        """affecte l'age du competiteur en fonction de sa date de naissance et la date du jour"""
        
        date_du_jour=datetime.datetime.now()
        jour_courant=date_du_jour.day
        mois_courant=date_du_jour.month
        annee_courante=date_du_jour.year

        jour_naissance=int(self.date_naissance[0:2])
        mois_naissance=int(self.date_naissance[3:5])
        annee_naissance=int(self.date_naissance[6:10])

        age=annee_courante-annee_naissance
        if mois_naissance>mois_courant:
            age-=1
        elif mois_naissance==mois_courant and jour_naissance<jour_courant:
            age-=1

        return age

    def affecter_categorie(self):
        """affecte une catégorie en fonction de l'age et du sexe du compétiteur"""

        if self.sexe=="m":
            categories=("M Cadet","M Junior","M Senior 1","M Senior 2","M Master 1","M Master 2","M Master 3","M Master 4")
        else :
            categories=("F Cadet","F Junior","F Senior 1","F Senior 2","F Master 1","F Master 2","F Master 3","F Master 4")

        if self.age<12:
            return "Trop jeune pour championnat"# voir avec éric comment on traite ce cas
        elif self.age<=14:
            return categories[0]
        elif self.age<=17:
            return categories[1]
        elif self.age<=30:
            return categories[2]
        elif self.age<=40:
            return categories[3]
        elif self.age<=50:
            return categories[4]
        elif self.age<=60:
            return categories[5]
        elif self.age<=65:
            return categories[6]
        else:
            return categories[7]
        
    def __repr__(self):
        """Formate l'affichage de l'objet Compétiteur avec print """

        return "Compétiteur {} {} Categorie : {} Note finale : {}".format(self.nom,self.prenom,self.categorie,self.note_finale)

