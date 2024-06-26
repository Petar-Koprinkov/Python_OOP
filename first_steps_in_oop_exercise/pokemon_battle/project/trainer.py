from typing import List
from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name: str):
        self.name = name
        self.pokemons: List = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        for p_obj in self.pokemons:
            if p_obj.name == pokemon_name:
                self.pokemons.remove(p_obj)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for p_obj in self.pokemons:
            result.append(f"- {p_obj.pokemon_details()}")

        return "\n".join(result)


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
