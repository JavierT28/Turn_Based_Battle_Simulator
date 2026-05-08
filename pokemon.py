class Pokemon:
    def __init__(self, name, p_type, hp, attack, defense, speed, moves):
        self.name = name
        self.type = p_type
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves  # list of Move objects

    def is_fainted(self):
        return self.hp <= 0

    def take_damage(self, dmg):
        self.hp = max(0, self.hp - dmg)

    def choose_move(self):
        # For now: auto-select first move
        return self.moves[0]
