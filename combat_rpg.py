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


CATALOGUE_HEROS = [

    {"nom": "Guerrier", "description": "Brave combattant proche du corps à corps",
        "pv": 35, "defense": 12, "arme": "Epée"},

    {"nom": "Mage", "description": "Maître de la magie offensive",
        "pv": 25, "defense": 10, "arme": "Bâton"},

    {"nom": "Archer", "description": "Expert du combat à distance",
        "pv": 28, "defense": 11, "arme": "Arc"},

    {"nom": "Paladin", "description": "Guerrier sacré protecteur",
        "pv": 40, "defense": 14, "arme": "Marteau"},

    {"nom": "Assassin", "description": "Combattant furtif et rapide",
        "pv": 26, "defense": 13, "arme": "Dague"},

    {"nom": "Barbare", "description": "Guerrier sauvage très puissant",
        "pv": 45, "defense": 10, "arme": "Hache"},

    {"nom": "Sorcier", "description": "Utilisateur de magie élémentaire",
        "pv": 30, "defense": 9, "arme": "Sceptre"},

    {"nom": "Chevalier", "description": "Protecteur lourdement armé",
        "pv": 38, "defense": 15, "arme": "Epée longue"},

    {"nom": "Ranger", "description": "Chasseur des forêts",
        "pv": 32, "defense": 12, "arme": "Arc long"},

    {"nom": "Moine", "description": "Combattant agile et spirituel",
        "pv": 33, "defense": 13, "arme": "Bâton de combat"}

]
