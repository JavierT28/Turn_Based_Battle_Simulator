from move import Move
from pokemon import Pokemon
from team import Team
from battle import Battle

# Sample moves
tackle = Move("Tackle", 40, "Normal")
ember = Move("Ember", 40, "Fire")

# Sample Pokémon
charmander = Pokemon("Charmander", "Fire", 39, 52, 43, 65, [ember])
bulbasaur = Pokemon("Bulbasaur", "Grass", 45, 49, 49, 45, [tackle])

# Teams
team1 = Team([charmander])
team2 = Team([bulbasaur])

# Run battle
battle = Battle(team1, team2)
battle.run()
