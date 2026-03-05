import random
print("Bienvenue dans le système de combat RPG")


def lancer_des(nb_des, faces):
    total = 0

    for i in range(nb_des):
        total += random.randint(1, faces)

    return total
