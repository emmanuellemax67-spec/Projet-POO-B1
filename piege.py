from meteo import choisir_meteo, appliquer_meteo
from piege import verifier_piege
import random

class Creature:
    def __init__(self, nom, pv, type_degats):
        self.nom = nom
        self.pv = pv
        self.type_degats = type_degats

    def attaque(self, cible):
        degats = random.randint(5, 10)
        degats = appliquer_meteo(degats, self.type_degats, meteo)
        cible.pv -= degats
        print(f"{self.nom} attaque {cible.nom} et inflige {degats} PV !")

joueur = Creature("Guerrier", 50, "feu")
monstre = Creature("Gobelin", 30, "tranchant")

meteo = choisir_meteo()

tour = 1
while joueur.pv > 0 and monstre.pv > 0:
    print(f"\n--- Tour {tour} ---")
    
    # Vérification des pièges
    verifier_piege(joueur)
    verifier_piege(monstre)
    
    # Attaques
    joueur.attaque(monstre)
    monstre.attaque(joueur)
    
    print(f"{joueur.nom} PV : {joueur.pv} | {monstre.nom} PV : {monstre.pv}")
    
    tour += 1
