import random

class entity:
    def __init__(self, name, hp, armor, dodge, mana, attack, potions):    # Entity's name, health, armor, dodge chance, mana, attack and potions numbers
        self.name = name
        self.hp = hp
        self.current_hp = hp
        self.armor = armor
        self.dodge = dodge
        self.mana = mana
        self.attack = attack
        self.potions = potions
    
    def take_damage(self):
        if self.armor >= opponent.attack:
            print(f'{self.name} blocked an attack!')
        else:
            self.current_hp =- (opponent.attack - self.armor)
    
    def deal_damage(self):
        if opponent.armor >= self.attack:
            print(f'{self.name} blocked an attack!')
        else:
            opponent.current_hp =- (self.attack - opponent.armor)

class skill:
    def __init__(self, name, damage, mana_usage, description):
        self.name = name
        self.damage = damage
        self.mana_usage = mana_usage
        self.description = description

def clear():
    print(f'\n' * 20)





player_alive = True

username = input('Enter your username: ')

hero = entity(username, 100, 5, 10, 50, 15, 3)



#                       GAME START



enemies = ['Goblin', 'Strong Goblin', 'Skeleton', 'Skeleton Archer', 'Skeleton With A Shield', 'Evil Wizard']

level = 0

while player_alive:
    level =+ 1

    if level != 10:
        floor_enemy = enemies[random.randint(0, 4)]
    else:
        floor_enemy = 'Evil Wizard'

    if floor_enemy == 'Goblin':
        goblin = entity(floor_enemy, 30, 2, 15, 0, 0, 0)
        current_enemy = goblin
    elif floor_enemy == 'Strong Goblin':
        strong_goblin = entity(floor_enemy, 80, 8, 5, 0, 0, 0)
        current_enemy = strong_goblin
    elif floor_enemy == 'Skeleton':
        skeleton = entity(floor_enemy, 40, 3, 5, 0, 0, 0)
        current_enemy = skeleton
    elif floor_enemy == 'Skeleton Archer':
        skeleton_archer = entity(floor_enemy, 25, 1, 20, 0, 0, 0)
        current_enemy = skeleton_archer
    elif floor_enemy == 'Skeleton With A Shield':
        skeleton_with_shield = entity(floor_enemy, 45, 12, 0, 0, 0, 0)
        current_enemy = skeleton_with_shield
    elif floor_enemy == 'Evil Wizard':
        evil_wizard = entity('Evil Wizard', 65, 2, 10, 100, 0, 0)
        current_enemy = evil_wizard


    print()
    print(f'Level {level}')
    print()
    print(f'Your enemy at this floor is {current_enemy.name}!')

    enemy_alive = True

    while enemy_alive:
        
        print()
        print(f'Your HP {hero.current_hp * '■' + (hero.hp - hero.current_hp) * '-'}')
        print(f'Enemy HP {current_enemy.current_hp * '■' + (current_enemy.hp - current_enemy.current_hp) * '-'}')
        print()

        player_turn = True
        enemy_turn = False

        while player_turn:
            opponent = current_enemy
        
            print(f'It\'s your turn! What will you do? ')
            print()
            print('1. Attack')
            print('2. Skills')
            print('3. Block')
            print('4. Heal.')

            print()
            action = int(input())
            clear()
#            if action == 1:
#                print 
#
#        while enemy_turn:
#            opponent = hero
    