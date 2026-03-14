import random
from meteo import Meteo

# Dictionnaire centralisé des pièges
# Chaque piège a : description, type, degats_base, chance_evitement (0-100), effet_special
TYPES_PIEGES = {
    "lame_cachee": {
        "nom":             "Lame cachée",
        "icone":           "🗡️",
        "description":     "Une lame jaillit du sol.",
        "type":            "physique",
        "degats_base":     12,
        "chance_evitement": 40,
        "effet_special":   None,
    },
    "fosse_ardente": {
        "nom":             "Fosse ardente",
        "icone":           "🔥",
        "description":     "Le sol s'ouvre sur un gouffre de flammes.",
        "type":            "feu",
        "degats_base":     18,
        "chance_evitement": 30,
        "effet_special":   "brulure",  # dégâts sur plusieurs tours
    },
    "nuage_poison": {
        "nom":             "Nuage de poison",
        "icone":           "☠️",
        "description":     "Un gaz toxique envahit la zone.",
        "type":            "poison",
        "degats_base":     10,
        "chance_evitement": 50,
        "effet_special":   "empoisonnement",
    },
    "eclair_runique": {
        "nom":             "Éclair runique",
        "icone":           "⚡",
        "description":     "Une rune électrique s'active sous tes pieds.",
        "type":            "foudre",
        "degats_base":     15,
        "chance_evitement": 35,
        "effet_special":   "paralysie",  # saute un tour
    },
    "tempete_glace": {
        "nom":             "Tempête de glace",
        "icone":           "❄️",
        "description":     "Un souffle glacial surgit des murs.",
        "type":            "glace",
        "degats_base":     14,
        "chance_evitement": 45,
        "effet_special":   "gel",  # réduit la vitesse
    },
    "toile_ombre": {
        "nom":             "Toile d'ombre",
        "icone":           "🕸️",
        "description":     "Des filaments d'obscurité t'enveloppent.",
        "type":            "ombre",
        "degats_base":     11,
        "chance_evitement": 55,
        "effet_special":   "aveuglissement",
    },
    "chute_rochers": {
        "nom":             "Chute de rochers",
        "icone":           "🪨",
        "description":     "Des rochers dégringolent du plafond.",
        "type":            "physique",
        "degats_base":     20,
        "chance_evitement": 25,
        "effet_special":   "etourdissement",
    },
    "malediction": {
        "nom":             "Malédiction ancienne",
        "icone":           "💀",
        "description":     "Une inscription maudite brille sur le sol.",
        "type":            "magique",
        "degats_base":     16,
        "chance_evitement": 30,
        "effet_special":   "malediction",  # réduit les stats temporairement
    },
}

DESCRIPTIONS_EFFETS = {
    "brulure":       "🔥 Brûlure — subira des dégâts chaque tour pendant 3 tours.",
    "empoisonnement":"☠️ Empoisonné — perd des PV progressivement.",
    "paralysie":     "⚡ Paralysé — rate son prochain tour.",
    "gel":           "❄️ Gelé — vitesse réduite de moitié.",
    "aveuglissement": "🌑 Aveuglé — précision réduite au prochain tour.",
    "etourdissement":"💫 Étourdi — rate son prochain tour.",
    "malediction":   "💀 Maudit — stats réduites pendant 3 tours.",
}


class Piege:

    def __init__(self, type_piege: str = None):
        """Crée un piège précis ou aléatoire."""
        types_disponibles = list(TYPES_PIEGES.keys())
        self.type_piege = type_piege if type_piege in types_disponibles else random.choice(types_disponibles)
        self.data = TYPES_PIEGES[self.type_piege]
        self.actif = True  # Un piège ne se déclenche qu'une fois

    def afficher(self):
        d = self.data
        print(f"{d['icone']}  Piège détecté : {d['nom']}")
        print(f"   {d['description']}")
        print(f"   Type : {d['type']} | Dégâts de base : {d['degats_base']}")
        if d["effet_special"]:
            print(f"   Effet : {DESCRIPTIONS_EFFETS.get(d['effet_special'], d['effet_special'])}")

    def declencher(self, cible, meteo: Meteo) -> dict:
        """
        Déclenche le piège sur la cible avec prise en compte de la météo.
        Retourne un dict avec : degats, evite, effet_special
        """
        if not self.actif:
            print("   Ce piège a déjà été déclenché.")
            return {"degats": 0, "evite": False, "effet_special": None}

        self.actif = False
        d = self.data

        print(f"\n{d['icone']}  {d['nom']} se déclenche ! {d['description']}")

        # Tentative d'évitement
        evite = self._tenter_evitement(cible)
        if evite:
            return {"degats": 0, "evite": True, "effet_special": None}

        # Calcul des dégâts avec modificateur météo
        degats = d["degats_base"]
        degats = meteo.modifier_degats(degats, d["type"])

        # Application des dégâts à la cible
        if hasattr(cible, "pv"):
            cible.pv = max(0, cible.pv - degats)
            print(f"   💥 {cible.nom if hasattr(cible, 'nom') else 'La cible'} subit {degats} dégâts !")
            print(f"   ❤️  PV restants : {cible.pv}")

        # Application de l'effet spécial
        effet = d["effet_special"]
        if effet:
            self._appliquer_effet(cible, effet)

        return {"degats": degats, "evite": False, "effet_special": effet}

    def _tenter_evitement(self, cible) -> bool:
        """Vérifie si la cible évite le piège selon sa chance d'évitement."""
        seuil = self.data["chance_evitement"]

        # Bonus d'agilité si la cible a un attribut agilite/vitesse
        if hasattr(cible, "agilite"):
            seuil += cible.agilite // 5
        elif hasattr(cible, "vitesse"):
            seuil += cible.vitesse // 5

        jet = random.randint(1, 100)
        evite = jet <= seuil

        if evite:
            nom = cible.nom if hasattr(cible, "nom") else "La cible"
            print(f"   💨 {nom} esquive le piège ! (jet {jet} ≤ {seuil})")
        return evite

    def _appliquer_effet(self, cible, effet: str):
        """Applique l'effet spécial du piège à la cible."""
        print(f"   {DESCRIPTIONS_EFFETS.get(effet, effet)}")

        # Si la cible a un attribut 'effets_actifs', on y ajoute l'effet
        if hasattr(cible, "effets_actifs"):
            cible.effets_actifs.append(effet)


# ─── Fonctions utilitaires ────────────────────────────────────────────────────

def generer_pieges_aleatoires(nb: int, meteo: Meteo = None) -> list:
    """Génère une liste de pièges aléatoires."""
    return [Piege() for _ in range(nb)]


def piege_adapte_meteo(meteo: Meteo) -> "Piege":
    """
    Génère un piège dont le type est AVANTAGEUX par rapport à la météo actuelle.
    Utile pour des donjons thématiques.
    """
    from meteo import EFFETS_METEO
    effets = EFFETS_METEO.get(meteo.type, {})
    types_avantageux = list(effets.get("avantages", {}).keys())

    pieges_compatibles = [
        cle for cle, val in TYPES_PIEGES.items()
        if val["type"] in types_avantageux
    ]

    if pieges_compatibles:
        return Piege(random.choice(pieges_compatibles))
    return Piege()  # fallback aléatoire
