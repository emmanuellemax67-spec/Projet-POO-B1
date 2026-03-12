import random

print("Bienvenue dans le système de combat RPG")


def lancer_des(nb_des, faces):
    total = 0
    for i in range(nb_des):
        total += random.randint(1, faces)
    return total


class Creature:

    def __init__(self, nom, description, pv, defense, type_degats):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.etats = []
        self.actions = []
        self.initiative = 0

    def est_vivant(self):
        return self.pv > 0


class Hero(Creature):

    def __init__(self, nom, description, pv, defense, arme):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = arme
        self.etats = []
        self.actions = []
        self.initiative = 0
        self.arme = arme
        self.inventaire = []

    def afficher_caracteristiques(self):
        print("\n--- HÉROS ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.type_degats)
        print("Etats :", self.etats)
        print("Arme :", self.arme)
        print("Inventaire :", self.inventaire)


class Monstre(Creature):

    def __init__(self, nom, description, pv, defense, type_degats, resistances=None):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.type_degats = type_degats
        self.etats = []
        self.actions = []
        self.initiative = 0
        if resistances is None:
            resistances = []
        self.resistances = resistances

    def afficher_caracteristiques(self):
        print("\n--- MONSTRE ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.type_degats)
        print("Etats :", self.etats)
        print("Résistances :", self.resistances)
