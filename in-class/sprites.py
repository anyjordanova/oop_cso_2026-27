class Enemy:
    enemy_type = "electric"
    health = 5
    x_pos = 10
    y_pos = 10

    def __init__(self, enemy_type, health, x_pos=0, y_pos=0):
        self.enemy_type = enemy_type
        self.health = health
        self.x_pos = x_pos
        self.y_pos = y_pos


    def display(self):
        print(f"type: {self.enemy_type}")
        print(f"health: {self.health}")
        print(f"x_pos: {self.x_pos}")
        print(f"y_pos: {self.y_pos}")


if __name__ == "__main__":
    first_enemy = Enemy("lightning", 100, 90, -100)

    print(f"enemy type: {first_enemy.enemy_type}")
    first_enemy.enemy_type = "fire"
    print(f"enemy type: {first_enemy.enemy_type}")

    first_enemy.display()

    second_enemy = Enemy("grass", 10, 4, 1)
    second_enemy.display()

    # required and optional parameters
    print("only required:")
    only_required = Enemy("fire", 5)
    only_required.display()

    print("no y pos:")
    no_y_pos = Enemy("water", 500, 88)
    no_y_pos.display()