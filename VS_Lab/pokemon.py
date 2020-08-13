class Pokemon:
    def __init__(self, name, level, element_type):
        self.name = name
        self.level = level
        self.set_element_type(element_type)
        self.set_maximum_health()
        self.current_health = self.maximum_health
        self.knocked_out = False

    def __repr__(self):
        return "{name}".format(name=self.name)

    def set_maximum_health(self):
        health_multiplier = 10
        self.maximum_health = self.level * health_multiplier

    def get_current_state(self):
        if self.knocked_out == False:
            print("{name} is level {level} is awake and has {current_health} health points".format(
                name=self.name, level=self.level, current_health=self.current_health))

        elif self.knocked_out == True:
            print("{name} is level {level} and is knocked out".format(
                name=self.name, level=self.level))

    def knocked_out_method(self):
        self.knocked_out = True
        print("{name} has lost all health points and has fainted".format(
            name=self.name))

    def revive(self):
        if self.knocked_out == True:
            self.set_maximum_health()
            self.current_health = self.maximum_health
            self.knocked_out = False
            print("{name} has been revived".format(name=self.name))

        elif self.knocked_out == False:
            print("{name} is still awake".format(name=self.name))

    def lose_health(self, hit_points):
        self.current_health -= hit_points

        if self.current_health <= 0:
            self.current_health = 0
            self.knocked_out_method()

        else:
            print("{name} lost {hit_points} health points and now has {current_health} left".format(
                name=self.name, hit_points=hit_points, current_health=self.current_health))

    def gain_health(self, points_gained):
        self.current_health += points_gained

        if (self.current_health > self.maximum_health):
            self.current_health = self.maximum_health

        print("{name} has gained {points_gained} health points and now is up to {current_health} health points".format(
            name=self.name, points_gained=points_gained, current_health=self.current_health))

    def set_element_type(self, element_type):
        element_list = [{"name_type": "Fire", "strong_against": "Grass", "weak_against": "Water"},
                        {"name_type": "Water", "strong_against": "Fire",
                            "weak_against": "Grass"},
                        {"name_type": "Grass", "strong_against": "Water", "weak_against": "Fire"}]

        for element in element_list:
            if element["name_type"] == element_type:
                self.element_type = element

    def attack(self, enemy_pokemon):
        damage = self.level * 2.0
        adjust_damage = 2
        level_increase = 1

        print("{name} has attacked {enemy_name}".format(
            name=self.name, enemy_name=enemy_pokemon.name))

        if (self.element_type["name_type"] == enemy_pokemon.element_type["name_type"]):
            enemy_pokemon.lose_health(damage)

        elif self.element_type["name_type"] in enemy_pokemon.element_type["weak_against"]:
            enemy_pokemon.lose_health(damage*adjust_damage)

        elif self.element_type["name_type"] in enemy_pokemon.element_type["strong_against"]:
            enemy_pokemon.lose_health(damage/adjust_damage)

        if enemy_pokemon.knocked_out == True:
            self.level += level_increase
            print("{name} level has increased to {level}".format(
                name=self.name, level=self.level))


class Trainer:
    def announce_active_pokemon(self):
        print("{name_trainer} has choosen {name_pokemon}".format(
            name_trainer=self.name, name_pokemon=self.pokemon_list[self.active_pokemon].name))

    def __init__(self, name, potions, pokemon_list):
        self.name = name
        self.potions = potions
        self.pokemon_list = pokemon_list
        self.active_pokemon = 0
        self.announce_active_pokemon()

    def use_potion(self):
        health_gained = 2.0
        if self.potions <= 0:
            print("You are out of potions")
        else:
            print("You have use a potion")
            self.potions -= 1
            self.pokemon_list[self.active_pokemon].gain_health(health_gained)

    def check_active_pokemon(self):
        if (self.pokemon_list[self.active_pokemon].knocked_out) == True:
            self.active_pokemon += 1 % (len(self.pokemon_list))
            self.announce_active_pokemon()

    def switch_active_pokemon(self, active_pokemon):
        if active_pokemon < len(self.pokemon_list):
            if (self.pokemon_list[active_pokemon].knocked_out) == False:
                self.active_pokemon = active_pokemon
                self.announce_active_pokemon()
            else:
                print("{name_trainer} cannot choose {name_pokemon} because is fainted".format(
                    name_trainer=self.name, name_pokemon=self.pokemon_list[active_pokemon].name))
        else:
            print("It's not one of your pokemons")

    def attack(self, enemy_trainer):
        self.pokemon_list[self.active_pokemon].attack(
            enemy_trainer.pokemon_list[enemy_trainer.active_pokemon])
        enemy_trainer.check_active_pokemon()


charmander = Pokemon("Charmander", 1, "Fire")
bulbasaur = Pokemon("Bulbasaur", 1, "Grass")
squirtle = Pokemon("Squirtle", 1, "Water")
ash_pokemon_list = [charmander, bulbasaur, squirtle]


cyndaquil = Pokemon("Cyndaquil", 1, "Fire")
chikorita = Pokemon("Chikorita", 1, "Grass")
totodile = Pokemon("Totodile", 1, "Water")
brock_pokemon_list = [cyndaquil, chikorita, totodile]

ash = Trainer("Ash", 5, ash_pokemon_list)
brock = Trainer("Brock", 5, brock_pokemon_list)

print("")
# ash.announce_active_pokemon()
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
ash.attack(brock)
brock.switch_active_pokemon(0)
