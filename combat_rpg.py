import random
print("Bienvenue dans le système de combat RPG")


def lancer_des(nb_des, faces):
    total = 0

    for i in range(nb_des):
        total += random.randint(1, faces)
    return total


class Creature:

    def __init__(self, nom, description, pv, defense, typeDegats):

        self.nom = nom
        self.description = description
        self.pv = pv
        self.defense = defense
        self.typeDegats = typeDegats

        self.etats = []
        self.actions = []
        self.initiative = 0

    def est_vivant(self):
        return self.pv > 0

    def afficher_caracteristiques(self):

        print("\n--- PERSONNAGE ---")
        print("Nom :", self.nom)
        print("Description :", self.description)
        print("PV :", self.pv)
        print("Défense :", self.defense)
        print("Type dégâts :", self.typeDegats)
        print("Etats :", self.etats)
