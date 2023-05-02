import json
import random
class Pokemon:
    def __init__(self, nom, type, vie=100, niveau=0, attaque=0, defense=0):
        self.__nom = nom
        self.type = type
        self.__vie = vie
        self.niveau = niveau
        self.attaque = attaque
        self.defense = defense
    
    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.__nom = value

    @property
    def vie(self):
        return self.__vie

    @vie.setter
    def vie(self, value):
        self.__vie = value
    
    def attaquer(self, autre_pokemon):
        # probabilité de réussir l'attaque
        proba_reussite = 0.8
        # probabilité d'infliger un coup critique
        proba_critique = 0.2
        # multiplicateur de dégâts pour les coups critiques
        multiplicateur_critique = 2
        # générer un nombre aléatoire entre 0 et 1
        chance = random.random()
        # vérifier si l'attaque réussit
        if chance < proba_reussite:
            # l'attaque réussit, calculer les dégâts infligés à l'autre Pokémon
            degats = self.attaque - autre_pokemon.defense
            # appliquer le multiplicateur de dégâts en fonction des types de Pokémon
            degats *= multiplicateurs_degats[(self.type, autre_pokemon.type)]
            # vérifier si l'attaque est un coup critique
            if chance < proba_critique:
                # l'attaque est un coup critique, multiplier les dégâts par le multiplicateur de coups critiques
                degats *= multiplicateur_critique
                print(f"{self.nom} inflige un coup critique à {autre_pokemon.nom}")
            else:
                print(f"{self.nom} inflige {degats} points de dégâts à {autre_pokemon.nom}")
            # infliger les dégâts à l'autre Pokémon
            autre_pokemon.vie = autre_pokemon.vie - degats
        else:
            # l'attaque échoue
            print(f"{self.nom} rate son attaque")

multiplicateurs_degats = {
    ("normal", "feu"): 1,
    ("normal", "eau"): 1,
    ("normal", "plante"): 1,
    ("normal", "electrique"): 1,
    ("normal", "glace"): 1,
    ("normal", "combat"): 1,
    ("normal", "poison"): 1,
    ("normal", "sol"): 1,
    ("normal", "vol"): 1,
    ("normal", "psy"): 1,
    ("normal", "insecte"): 1,
    ("normal", "roche"): 0.5,
    ("normal", "spectre"): 0,
    ("normal", "dragon"): 1,
    ("normal", "tenebres"): 1,
    ("normal", "acier"): 0.5,
    ("normal", "fee"): 1,
    ("plante", "feu"): 0.5,
    ("plante", "eau"): 2,
    ("plante", "plante"): 0.5,
    ("plante", "electrique"): 0.5,
    ("plante", "glace"): 1,
    ("plante", "combat"): 1,
    ("plante", "poison"): 0.5,
    ("plante", "sol"): 2,
    ("plante", "vol"): 0.5,
    ("plante", "psy"): 1,
    ("plante", "insecte"): 0.5,
    ("plante", "roche"): 2,
    ("plante", "spectre"): 1,
    ("plante", "dragon"): 0.5,
    ("plante", "tenebres"): 1,
    ("plante", "acier"): 0.5,
    ("plante", "fee"): 1,
    ("feu", "feu"): 0.5,
    ("feu", "eau"): 0.5,
    ("feu", "plante"): 2,
    ("feu", "electrique"): 1,
    ("feu", "glace"): 2,
    ("feu", "combat"): 1,
    ("feu", "poison"): 1,
    ("feu", "sol"): 1,
    ("feu", "vol"): 1,
    ("feu", "psy"): 1,
    ("feu", "insecte"): 2,
    ("feu", "roche"): 0.5,
    ("feu", "spectre"): 1,
    ("feu", "dragon"): 0.5,
    ("feu", "tenebres"): 1,
    ("feu", "acier"): 2,
    ("feu", "fee"): 1,
    ("eau", "feu"): 2,
    ("eau", "eau"): 0.5,
    ("eau", "plante"): 0.5,
    ("eau", "electrique"): 1,
    ("eau", "glace"): 1,
    ("eau", "combat"): 1,
    ("eau", "poison"): 1,
    ("eau", "sol"): 2,
    ("eau", "vol"): 1,
    ("eau", "psy"): 1,
    ("eau", "insecte"): 1,
    ("eau", "roche"): 2,
    ("eau", "spectre"): 1,
    ("eau", "dragon"): 0.5,
    ("eau", "tenebres"): 1,
    ("eau", "acier"): 1,
    ("eau", "fee"): 1,
    ("electrique", "normal"): 1,
    ("electrique", "combat"): 1,
    ("electrique", "poison"): 1,
    ("electrique", "sol"): 0,
    ("electrique", "roche"): 1,
    ("electrique", "insecte"): 1,
    ("electrique", "spectre"): 1,
    ("electrique", "acier"): 1,
    ("electrique", "feu"): 1,
    ("electrique", "eau"): 2,
    ("electrique", "plante"): 0.5,
    ("electrique", "electrique"): 0.5,
    ("electrique", "psy"): 1,
    ("electrique", "glace"): 1,
    ("electrique", "dragon"): 0.5,
    ("electrique", "tenebres"): 1,
    ("electrique", "fee"): 1,
    ("glace", "feu"): 0.5,
    ("glace", "eau"): 0.5,
    ("glace", "plante"): 2,
    ("glace", "electrique"): 1,
    ("glace", "glace"): 0.5,
    ("glace", "combat"): 1,
    ("glace", "poison"): 1,
    ("glace", "sol"): 2,
    ("glace", "vol"): 2,
    ("glace", "psy"): 1,
    ("glace", "insecte"): 1,
    ("glace", "roche"): 1,
    ("glace", "spectre"): 1,
    ("glace", "dragon"): 2,
    ("glace", "tenebres"): 1,
    ("glace", "acier"): 0.5,
    ("glace", "fee"): 1,
    ("combat", "normal"): 2,
    ("combat", "feu"): 1,
    ("combat", "eau"): 1,
    ("combat", "plante"): 1,
    ("combat", "electrique"): 1,
    ("combat", "glace"): 2,
    ("combat", "combat"): 1,
    ("combat", "poison"): 0.5,
    ("combat", "sol"): 1,
    ("combat", "vol"): 0.5,
    ("combat", "psy"): 0.5,
    ("combat", "insecte"): 0.5,
    ("combat", "roche"): 2,
    ("combat", "spectre"): 0,
    ("combat", "dragon"): 1,
    ("combat", "tenebres"): 2,
    ("combat", "acier"): 2,
    ("combat", "fee"): 0.5,
    ("poison", "normal"): 1,
    ("poison", "feu"): 1,
    ("poison", "eau"): 1,
    ("poison", "plante"): 2,
    ("poison", "electrique"): 1,
    ("poison", "glace"): 1,
    ("poison", "combat"): 1,
    ("poison", "poison"): 0.5,
    ("poison", "sol"): 0.5,
    ("poison", "vol"): 1,
    ("poison", "psy"): 1,
    ("poison", "insecte"): 1,
    ("poison", "roche"): 0.5,
    ("poison", "spectre"): 0.5,
    ("poison", "dragon"): 1,
    ("poison", "tenebres"): 1,
    ("poison", "acier"): 0,
    ("poison", "fee"): 2,
    ("sol", "feu"): 2,
    ("sol", "eau"): 1,
    ("sol", "plante"): 0.5,
    ("sol", "electrique"): 2,
    ("sol", "glace"): 1,
    ("sol", "combat"): 1,
    ("sol", "poison"): 2,
    ("sol", "sol"): 1,
    ("sol", "vol"): 0,
    ("sol", "psy"): 1,
    ("sol", "insecte"): 0.5,
    ("sol", "roche"): 2,
    ("sol", "spectre"): 1,
    ("sol", "dragon"): 1,
    ("sol", "tenebres"): 1,
    ("sol", "acier"): 2,
    ("sol", "fee"): 1,
    ("vol", "normal"): 1,
    ("vol", "feu"): 1,
    ("vol", "eau"): 1,
    ("vol", "plante"): 2,
    ("vol", "electrique"): 0.5,
    ("vol", "glace"): 1,
    ("vol", "combat"): 2,
    ("vol", "poison"): 1,
    ("vol", "sol"): 1,
    ("vol", "vol"): 1,
    ("vol", "psy"): 1,
    ("vol", "insecte"): 2,
    ("vol", "roche"): 0.5,
    ("vol", "spectre"): 1,
    ("vol", "dragon"): 1,
    ("vol", "tenebres"): 1,
    ("vol", "acier"): 0.5,
    ("vol", "fee"): 1,
    ("psy", "normal"): 1,
    ("psy", "feu"): 1,
    ("psy", "eau"): 1,
    ("psy", "plante"): 1,
    ("psy", "electrique"): 1,
    ("psy", "glace"): 1,
    ("psy", "combat"): 2,
    ("psy", "poison"): 2,
    ("psy", "sol"): 1,
    ("psy", "vol"): 1,
    ("psy", "psy"): 0.5,
    ("psy", "insecte"): 1,
    ("psy", "roche"): 1,
    ("psy", "spectre"): 1,
    ("psy", "dragon"): 1,
    ("psy", "tenebres"): 0,
    ("psy", "acier"): 0.5,
    ("psy", "fee"): 1,
    ("insecte", "normal"): 1,
    ("insecte", "feu"): 0.5,
    ("insecte", "eau"): 1,
    ("insecte", "plante"): 2,
    ("insecte", "electrique"): 1,
    ("insecte", "glace"): 1,
    ("insecte", "combat"): 0.5,
    ("insecte", "poison"): 0.5,
    ("insecte", "sol"): 1,
    ("insecte", "vol"): 0.5,
    ("insecte", "psy"): 2,
    ("insecte", "insecte"): 1,
    ("insecte", "roche"): 1,
    ("insecte", "spectre"): 0.5,
    ("insecte", "dragon"): 1,
    ("insecte", "tenebres"): 2,
    ("insecte", "acier"): 0.5,
    ("insecte", "fee"): 0.5,
    ("roche", "normal"): 1,
    ("roche", "feu"): 2,
    ("roche", "eau"): 1,
    ("roche", "plante"): 1,
    ("roche", "electrique"): 1,
    ("roche", "glace"): 2,
    ("roche", "combat"): 0.5,
    ("roche", "poison"): 1,
    ("roche", "sol"): 0.5,
    ("roche", "vol"): 2,
    ("roche", "psy"): 1,
    ("roche", "insecte"): 2,
    ("roche", "roche"): 1,
    ("roche", "spectre"): 1,
    ("roche", "dragon"): 1,
    ("roche", "tenebres"): 1,
    ("roche", "acier"): 0.5,
    ("roche", "fee"): 1,
    ("spectre", "normal"): 0,
    ("spectre", "feu"): 1,
    ("spectre", "eau"): 1,
    ("spectre", "plante"): 1,
    ("spectre", "electrique"): 1,
    ("spectre", "glace"): 1,
    ("spectre", "combat"): 1,
    ("spectre", "poison"): 0.5,
    ("spectre", "sol"): 1,
    ("spectre", "vol"): 1,
    ("spectre", "psy"): 2,
    ("spectre", "insecte"): 0.5,
    ("spectre", "roche"): 1,
    ("spectre", "spectre"): 2,
    ("spectre", "dragon"): 1,
    ("spectre", "tenebres"): 0.5,
    ("spectre", "acier"): 1,
    ("spectre", "fee"): 1,
    ("dragon", "normal"): 1,
    ("dragon", "feu"): 1,
    ("dragon", "eau"): 1,
    ("dragon", "plante"): 1,
    ("dragon", "electrique"): 1,
    ("dragon", "glace"): 1,
    ("dragon", "combat"): 1,
    ("dragon", "poison"): 1,
    ("dragon", "sol"): 1,
    ("dragon", "vol"): 1,
    ("dragon", "psy"): 1,
    ("dragon", "insecte"): 1,
    ("dragon", "roche"): 1,
    ("dragon", "spectre"): 1,
    ("dragon", "dragon"): 2,
    ("dragon", "tenebres"): 1,
    ("dragon", "acier"): 0.5,
    ("dragon", "fee"): 0,
    ("tenebres", "normal"): 1,
    ("tenebres", "feu"): 1,
    ("tenebres", "eau"): 1,
    ("tenebres", "plante"): 1,
    ("tenebres", "electrique"): 1,
    ("tenebres", "glace"): 1,
    ("tenebres", "combat"): 0.5,
    ("tenebres", "poison"): 1,
    ("tenebres", "sol"): 1,
    ("tenebres", "vol"): 1,
    ("tenebres", "psy"): 2,
    ("tenebres", "insecte"): 1,
    ("tenebres", "roche"): 1,
    ("tenebres", "spectre"): 2,
    ("tenebres", "dragon"): 1,
    ("tenebres", "tenebres"): 0.5,
    ("tenebres", "acier"): 1,
    ("tenebres", "fee"): 0.5,
    ("acier", "normal"): 1,
    ("acier", "feu"): 0.5,
    ("acier", "eau"): 0.5,
    ("acier", "plante"): 1,
    ("acier", "electrique"): 0.5,
    ("acier", "glace"): 2,
    ("acier", "combat"): 1,
    ("acier", "poison"): 1,
    ("acier", "sol"): 1,
    ("acier", "vol"): 1,
    ("acier", "psy"): 1,
    ("acier", "insecte"): 1,
    ("acier", "roche"): 2,
    ("acier", "spectre"): 1,
    ("acier", "dragon"): 1,
    ("acier", "tenebres"): 1,
    ("acier", "acier"): 0.5,
    ("acier", "fee"): 2,
    ("fee", "normal"): 1,
    ("fee", "feu"): 0.5,
    ("fee", "eau"): 1,
    ("fee", "plante"): 1,
    ("fee", "electrique"): 1,
    ("fee", "glace"): 1,
    ("fee", "combat"): 2,
    ("fee", "poison"): 0.5,
    ("fee", "sol"): 1,
    ("fee", "vol"): 1,
    ("fee", "psy"): 1,
    ("fee", "insecte"): 1,
    ("fee", "roche"): 1,
    ("fee", "spectre"): 1,
    ("fee", "dragon"): 2,
    ("fee", "tenebres"): 2,
    ("fee", "acier"): 0.5
}

class Pokemons_Normal(Pokemon):
    def __init__(self, nom):
        super().__init__(nom, "normal", attaque=74, defense=61)
class pokemons_Feu(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "feu", attaque=82, defense=68)

class pokemons_Plante(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "plante", attaque=76, defense=74)

class pokemons_Eau(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "eau", attaque=75, defense=75)

class pokemons_Electrique(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "electrique", attaque=75, defense=70)

class pokemons_Glace(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "glace", attaque=84, defense=76)
        
class xxx(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "combat", attaque=107, defense=77)
        
class pokemons_Poison(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "poison", attaque=72, defense=68)
        
class pokemons_Sol(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "sol", attaque=92, defense=87)
        
class pokemons_Vol(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "vol", attaque=80, defense=68)
        
class pokemons_Psy(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "psy", attaque=73, defense=74)
        
class pokemons_Insecte(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "insecte", attaque=72, defense=71)
        
class pokemons_Roche(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "roche", attaque=91, defense=104)
        
class pokemons_Spectre(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "spectre", attaque=79, defense=80)
        
class pokemons_Dragon(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "dragon", attaque=102, defense=90)
        
class pokemons_Tenebre(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "tenebre", attaque=92, defense=68)
        
class pokemons_Acier(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "acier", attaque=97, defense=110)
        
class pokemons_Fee(Pokemon):
    def __init__(self,nom):
        super().__init__(nom, "fee", attaque=69, defense=89)

pokemons_combat = []
pokemons_combat.append(pokemons_Feu("Salamèche"))
pokemons_combat.append(pokemons_Feu("Reptincel"))
pokemons_combat.append(pokemons_Feu("Dracaufeu"))
pokemons_combat.append(pokemons_Feu("Goupix"))
pokemons_combat.append(pokemons_Feu("Feunard"))
pokemons_combat.append(pokemons_Feu("Caninos"))
pokemons_combat.append(pokemons_Feu("Arcanin"))
pokemons_combat.append(pokemons_Feu("Ponyta"))
pokemons_combat.append(pokemons_Feu("Galopa"))
pokemons_combat.append(pokemons_Feu("Magmar"))
pokemons_combat.append(pokemons_Feu("Pyroli"))
pokemons_combat.append(pokemons_Eau("Carapuce"))
pokemons_combat.append(pokemons_Eau("Carabaffe"))
pokemons_combat.append(pokemons_Eau("Tortank"))
pokemons_combat.append(pokemons_Eau("Psykokwak"))
pokemons_combat.append(pokemons_Eau("Akwakwak"))
pokemons_combat.append(pokemons_Eau("Poissirène"))
pokemons_combat.append(pokemons_Eau("Poissoroy"))
pokemons_combat.append(pokemons_Eau("Leviator"))
pokemons_combat.append(pokemons_Eau("Magicarpe"))
pokemons_combat.append(pokemons_Eau("Lokhlass"))
pokemons_combat.append(pokemons_Plante("Bulbizarre"))
pokemons_combat.append(pokemons_Plante("Herbizarre"))
pokemons_combat.append(pokemons_Plante("Florizarre"))
pokemons_combat.append(pokemons_Plante("Paras"))
pokemons_combat.append(pokemons_Plante("Parasect"))
pokemons_combat.append(pokemons_Plante("Chétiflor"))
pokemons_combat.append(pokemons_Plante("Boustiflor"))
pokemons_combat.append(pokemons_Plante("Empiflor"))
pokemons_combat.append(pokemons_Plante("Rosélia"))
pokemons_combat.append(pokemons_Plante("Joliflor"))
pokemons_combat.append(pokemons_Plante("Rafflesia"))
pokemons_combat.append(Pokemons_Normal("Rattata"))
pokemons_combat.append(Pokemons_Normal("Rattatac"))

class Combat:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def commencer_Combat(self):
        while self.pokemon1.vie > 0 and self.pokemon2.vie > 0:
            self.pokemon1.attaquer(self.pokemon2)
            if self.pokemon2.vie <= 0:
                print(f"{self.pokemon2.nom} a perdu le combat")
                print(f"Fin du combat, {self.pokemon1.nom} gagne")
                break     
            self.pokemon2.attaquer(self.pokemon1)
            if self.pokemon1.vie <= 0:
                print(f"{self.pokemon1.nom} a perdu le combat")
                print(f"Fin du combat, {self.pokemon2.nom} gagne")
                break

    # Créer les Pokémon de départ
    salamèche = pokemons_Feu("Salamèche")
    bulbizarre =pokemons_Plante("Bulbizarre")
    carapuce = pokemons_Eau("Carapuce")

    # Demander au joueur de choisir son Pokémon de départ
    print("Choisissez votre Pokémon de départ:")
    print("1. Salamèche")
    print("2. Bulbizarre")
    print("3. Carapuce")
    choix = int(input("Entrez le numéro de votre choix: "))

    # Assigner le Pokémon choisi par le joueur
    if choix == 1:
        pokemon_joueur = salamèche
    elif choix == 2:
        pokemon_joueur = bulbizarre
    else:
        pokemon_joueur = carapuce

class Pokedex:
    def __init__(self):
        self.pokemons = []

    def ajouter_pokemon(self, pokemon):
        # Vérifier si le Pokémon est déjà dans le Pokédex
        for p in self.pokemons:
            if p.nom == pokemon.nom:
                # Le Pokémon est déjà dans le Pokédex, ne pas l'ajouter à nouveau
                return
        # Le Pokémon n'est pas dans le Pokédex, l'ajouter à la liste

def sauvegarder(self):
        # Créer une liste de dictionnaires contenant les données des Pokémon
        data = []
        for pokemon in self.pokemons:
            data.append({
                "nom": pokemon.nom,
                "type": pokemon.type,
                "vie": pokemon.vie,
                "niveau": pokemon.niveau,
                "attaque": pokemon.attaque,
                "defense": pokemon.defense
            })
        # Ouvrir le fichier JSON en mode écriture
        with open("pokedex.json", "w") as f:
            # Écrire les données dans le fichier JSON
            json.dump(data, f)

        pokemon_adversaire = random.choice(pokemons_combat)
        combat = Combat(pokemon_joueur, pokemon_adversaire)
        combat.commencer_combat()