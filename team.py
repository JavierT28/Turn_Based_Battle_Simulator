class Team:
    def __init__(self, pokemons):
        self.pokemons = pokemons

    def get_active(self):
        for p in self.pokemons:
            if not p.is_fainted():
                return p
        return None

    def has_pokemon_left(self):
        return any(not p.is_fainted() for p in self.pokemons)
