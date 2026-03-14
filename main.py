from meteo import Meteo
from pieges import Piege, piege_adapte_meteo

# ─── Faux héros pour le test ──────────────────────────────────────────────────
class HeroTest:
    def __init__(self, nom, pv, agilite=10):
        self.nom = nom
        self.pv  = pv
        self.agilite = agilite
        self.effets_actifs = []

# ─── Météo ────────────────────────────────────────────────────────────────────
print("=" * 50)
print("          ⚔️  TEST DU JEU DE COMBAT ⚔️")
print("=" * 50)
print()

meteo = Meteo()
meteo.afficher()
print()

# ─── Test sorts ───────────────────────────────────────────────────────────────
print("─" * 50)
print("🔮  SORTS")
print("─" * 50)

sorts_test = [
    ("Boule de feu",    "feu",    18),
    ("Vague de glace",  "glace",  14),
    ("Éclair",          "foudre", 20),
    ("Poison mystique", "poison",  9),
    ("Lame d'ombre",    "ombre",  12),
]

for nom_sort, type_sort, degats_base in sorts_test:
    effet = meteo.get_modificateur(type_sort)
    print(f"🔮 {nom_sort} ({type_sort}) — {degats_base} dégâts de base [météo : {effet}]")
    degats_finaux = meteo.modifier_degats(degats_base, type_sort)
    print(f"   → Dégâts finaux : {degats_finaux}")
    print()

# ─── Test pièges ──────────────────────────────────────────────────────────────
print("─" * 50)
print("🪤  PIÈGES")
print("─" * 50)
print()

hero = HeroTest(nom="Aldric", pv=100, agilite=15)
print(f"🧙 Héros : {hero.nom} | PV : {hero.pv} | Agilité : {hero.agilite}")
print()

# Test 1 : piège aléatoire
print("[ Piège 1 — Aléatoire ]")
piege1 = Piege()
piege1.afficher()
piege1.declencher(hero, meteo)
print(f"   Effets actifs : {hero.effets_actifs if hero.effets_actifs else 'aucun'}")
print()

# Test 2 : piège thématique selon la météo
print("[ Piège 2 — Adapté à la météo ]")
piege2 = piege_adapte_meteo(meteo)
piege2.afficher()
piege2.declencher(hero, meteo)
print(f"   Effets actifs : {hero.effets_actifs if hero.effets_actifs else 'aucun'}")
print()

# Test 3 : piège précis (lame cachée)
print("[ Piège 3 — Lame cachée (forcé) ]")
piege3 = Piege("lame_cachee")
piege3.afficher()
piege3.declencher(hero, meteo)
print()

# Bilan final
print("─" * 50)
print(f"📊  BILAN FINAL — {hero.nom}")
print(f"   ❤️  PV restants  : {hero.pv} / 100")
print(f"   ⚠️  Effets actifs : {hero.effets_actifs if hero.effets_actifs else 'aucun'}")
print("─" * 50)