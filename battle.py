class Battle:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def calculate_damage(self, attacker, defender, move):
        base = move.power + attacker.attack - defender.defense
        return max(1, base)

    def execute_move(self, attacker, defender, move):
        dmg = self.calculate_damage(attacker, defender, move)
        defender.take_damage(dmg)
        print(f"{attacker.name} used {move.name}! {defender.name} took {dmg} damage.")

    def take_turn(self):
        p1 = self.team1.get_active()
        p2 = self.team2.get_active()

        if not p1 or not p2:
            return

        m1 = p1.choose_move()
        m2 = p2.choose_move()

        # Speed check
        if p1.speed >= p2.speed:
            self.execute_move(p1, p2, m1)
            if not p2.is_fainted():
                self.execute_move(p2, p1, m2)
        else:
            self.execute_move(p2, p1, m2)
            if not p1.is_fainted():
                self.execute_move(p1, p2, m1)

    def run(self):
        while self.team1.has_pokemon_left() and self.team2.has_pokemon_left():
            self.take_turn()

        if self.team1.has_pokemon_left():
            print("Team 1 wins!")
        else:
            print("Team 2 wins!")
