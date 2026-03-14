import random

# Dictionnaire centralisé : pour chaque météo, avantages et désavantages par type de sort
EFFETS_METEO = {
    "soleil": {
        "avantages": {
            "feu":    ("Le soleil amplifie les sorts de feu !", lambda d: d + 4),
            "nature": ("La lumière solaire nourrit la magie naturelle !", lambda d: int(d * 1.3)),
        },
        "desavantages": {
            "glace":  ("La chaleur affaiblit les sorts de glace.", lambda d: d - 3),
            "ombre":  ("Le soleil dissipe les ténèbres.", lambda d: d // 2),
        },
    },
    "pluie": {
        "avantages": {
            "eau":    ("La pluie renforce les sorts aquatiques !", lambda d: int(d * 1.5)),
            "glace":  ("L'humidité booste la magie glaciale !", lambda d: d + 3),
            "nature": ("La pluie revitalise la magie naturelle !", lambda d: d + 2),
        },
        "desavantages": {
            "feu":    ("La pluie éteint les sorts de feu.", lambda d: d // 2),
            "foudre": ("L'eau conduit la foudre de façon imprévisible.", lambda d: d - 2),
        },
    },
    "orage": {
        "avantages": {
            "foudre": ("L'orage décuple la puissance électrique !", lambda d: d * 2),
            "magique": ("L'énergie orageuse amplifie la magie pure !", lambda d: d + 5),
            "vent":   ("Les rafales boostent la magie aérienne !", lambda d: int(d * 1.4)),
        },
        "desavantages": {
            "feu":    ("L'orage humide étouffe le feu.", lambda d: d - 2),
            "nature": ("La tempête perturbe les esprits naturels.", lambda d: d - 1),
        },
    },
    "brouillard": {
        "avantages": {
            "ombre":  ("Le brouillard renforce les sorts obscurs !", lambda d: int(d * 1.4)),
            "poison": ("Les vapeurs amplifient les poisons !", lambda d: d + 3),
            "esprit": ("Le voile mystique potentialise la magie mentale !", lambda d: d + 4),
        },
        "desavantages": {
            "feu":    ("Le brouillard humide affaiblit les flammes.", lambda d: d - 1),
            "foudre": ("La brume noie l'électricité.", lambda d: d // 2),
            "soleil": ("Le brouillard bloque la lumière.", lambda d: d - 2),
        },
    },
    "neige": {
        "avantages": {
            "glace":  ("Le blizzard surpuissante la glace !", lambda d: d * 2),
            "vent":   ("La tempête de neige amplifie le vent !", lambda d: d + 4),
        },
        "desavantages": {
            "feu":    ("La neige annihile presque le feu.", lambda d: max(1, d // 3)),
            "nature": ("Le gel engourdit la nature.", lambda d: d - 3),
            "foudre": ("La neige isole l'électricité.", lambda d: d - 2),
        },
    },
    "canicule": {
        "avantages": {
            "feu":    ("La canicule rend le feu dévastateur !", lambda d: int(d * 2.0)),
            "ombre":  ("La chaleur crée des mirages obscurs !", lambda d: d + 2),
        },
        "desavantages": {
            "glace":  ("La chaleur extrême fond instantanément la glace.", lambda d: max(1, d // 3)),
            "eau":    ("L'eau s'évapore avant d'agir.", lambda d: d - 3),
        },
    },
}

ICONES_METEO = {
    "soleil":    "☀️",
    "pluie":     "🌧️",
    "orage":     "⛈️",
    "brouillard":"🌫️",
    "neige":     "❄️",
    "canicule":  "🔥",
}


class Meteo:

    def __init__(self, type_meteo: str = None):
        """Crée une météo aléatoire ou avec un type précis."""
        types_disponibles = list(EFFETS_METEO.keys())
        self.type = type_meteo if type_meteo in types_disponibles else random.choice(types_disponibles)

    def afficher(self):
        icone = ICONES_METEO.get(self.type, "🌦️")
        print(f"{icone}  Météo actuelle : {self.type.capitalize()}")
        self._afficher_effets()

    def _afficher_effets(self):
        effets = EFFETS_METEO.get(self.type, {})
        avantages   = effets.get("avantages", {})
        desavantages = effets.get("desavantages", {})
        if avantages:
            print(f"  ✅ Avantageux  : {', '.join(avantages.keys())}")
        if desavantages:
            print(f"  ❌ Désavantageux : {', '.join(desavantages.keys())}")

    def modifier_degats(self, degats: int, type_sort: str) -> int:
        """
        Applique les effets météo aux dégâts d'un sort.
        Retourne les dégâts modifiés (minimum 1).
        """
        effets = EFFETS_METEO.get(self.type, {})
        avantages    = effets.get("avantages", {})
        desavantages = effets.get("desavantages", {})

        if type_sort in avantages:
            message, modificateur = avantages[type_sort]
            print(f"  ⚡ {message}")
            degats = modificateur(degats)

        elif type_sort in desavantages:
            message, modificateur = desavantages[type_sort]
            print(f"  💧 {message}")
            degats = modificateur(degats)

        return max(1, degats)  # Les dégâts ne peuvent jamais être inférieurs à 1

    def get_modificateur(self, type_sort: str) -> float:
        """
        Retourne un descriptif textuel de l'effet météo sur un type de sort.
        Utile pour afficher des infos avant de lancer un sort.
        """
        effets = EFFETS_METEO.get(self.type, {})
        if type_sort in effets.get("avantages", {}):
            return "avantageux"
        if type_sort in effets.get("desavantages", {}):
            return "désavantageux"
        return "neutre"