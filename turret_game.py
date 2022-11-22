new_list = []
colours = ['red','blue','green','yellow']
ranks = ['one','two','three','four','five','six','seven','eight','nine']
values = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
powers = ['healing drone','tesla discharge','shield','acid spray','air drop','grenade blast','assault drone','armoured convoy','shady deals','bomb','energy assimilator','spare battery','supercharger','defensive systems','reflective system','EMP blast','ballistic shield','flame barrels','armour piercing rounds','extended magazine','instant fix','double damage','bullet spray','bullet barrage','turret disabler','corrosive gas','electro cannon','flamethrower','mechanic fix','spare parts']
superpowers = ['special air drop','air support','tank','elite deal','nuclear blast','heavy duty battery','upgrade kit','grenade launcher','extra turret','bazooka','FUBAR','anti-air systems','railgun','gravitron','cluster missiles']

class Player():
    
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.deck = []#For power ups only!
        self.energy = 5
        self.shield = False
        self.burn = 0
        self.stun = False
        self.corrode = 0
        self.vulnerable = 0
        self.drone = False
        self.armour = 0
        self.defense = 0
        self.x2_dmg = False
        self.armour_pierce = False
        self.extended_mag = 0
        self.regen = False
        self.mirror = False
        self.bps = False
        self.tank = 0
        self.air_support = False
        self.increased_dmg = 0
        self.g_launcher = False
        self.turret = 0
    
    def __str__(self):
        return self.name + ' has ' + str(self.health) + ' points of health, and ' + str(self.energy) + ' points of energy.'
    
    
    def deck_display(self):
        print(f'{self.name} has the following power-up cards:')
        q = 0
        for element in self.deck:
            q += 1
            print('\t' + str(q) + ': ' + str(element))
    
    
    def turn_card(self, card):
        self.card = card
        print(f'{self.name} has drawn a turn {card}.')
        if len(player_list) <= card.value:
            diff = abs(card.value - len(player_list))
        else:
            diff = card.value
        while diff >= len(player_list):
            diff -= len(player_list)
                    
        attack_deck.deck.append(card)
        target = player_list[diff]
    
        return target
                
    
    def dmg_card(self, card):
        attack_deck.deck.append(card)
        print(f'{self.name} has drawn a damage {card}.')
        return card.value
    
    
    def dmg_received(self, damage):
        self.damage = damage
        if player.g_launcher:
            self.burn += 1
        if self.vulnerable > 0:
            self.damage += 2
            print(f'{self.name} is vulnerable. Additional damage taken! {str(self.vulnerable)} turns left.')

        if player.armour_pierce:
            self.bps = False
            
        if self.shield and self.damage > 0:
            print('Player is protected from all incoming damage by the shield!')
            print('The shield has been destroyed!')
            self.shield = False
            
        elif self.shield and self.damage <= 0:
            pass
        
        elif self.armour > 0:
            self.armour -= self.damage
            print('The armoured convoy soaks up incoming damage.')
            if self.armour <= 0:
                self.armour = 0
                print('The armoured convoy has been destroyed!')
            else:
                print(f'The armoured convoy has {str(self.armour)} points of armour left.')
        
        elif self.tank > 0:
            self.tank -= self.damage
            print('The tank soaks up incoming damage.')
            if self.tank <= 0:
                self.tank = 0
                print('The tank has been destroyed.')
            else:
                print(f'The tank has {str(self.tank)} points of armour left.')
        
        elif self.bps:
            print('Ballistic shield protects from all incoming damage!')
        
        else:
            self.damage -= self.defense
            if self.damage < 0:
                self.damage = 0
            self.health -= self.damage
            print(f'{str(self.damage)} damage has been dealt to {self.name}.')
            
    def damage_processing(self, dmg):
        self.dmg = dmg
        if self.x2_dmg:
            self.dmg += self.dmg
        if self.corrode > 0:
            self.dmg -= 3
        if self.armour_pierce:
            target.shield = False
            self.dmg += 2
        if self.drone:
            self.dmg += 3
        if target.mirror:
            player.dmg_received(2)
        if self.tank > 0:
            self.dmg += 5
        if self.air_support:
            self.dmg += 5
        self.dmg += self.increased_dmg
        
        return self.dmg

while True:
    player_number = input('How many players are there playing this game? Ans: ')
    try:
        player_num = int(player_number)
    except:
        print('Please input a proper integer value!')
        continue
    break
    
player_list = []
names = []

for val in range(player_num):
    name = input('Player, what is your name? Ans: ')
    while name in names:
        print('Name taken! Choose another name!')
        name = input('What is your name? Ans: ')
    names.append(name)
    player = Player(name)
    player_list.append(player)
    
class AttackCard():
    def __init__(self, rank, colour):
        self.rank = rank
        self.colour = colour
        self.value = values[rank]
        
    def __str__(self):
        return 'card of ' + self.rank

class PowerUpCard():
    def __init__(self, power, colour):
        self.power = power
        self.colour = colour
        self.super = False
    def __str__(self):
        return 'power card of ' + self.power

class SuperpoweredCard():
    def __init__(self, superpower, colour):
        self.superpower = superpower
        self.colour = colour
        self.super = True
    def __str__(self):
        return 'SUPER power card of ' + self.superpower

class AttackDeck():
    def __init__(self):
        self.deck = []
        for colour in colours:
            for rank in ranks:
                card = AttackCard(rank, colour)
                self.deck.append(card)
        
        for colour in colours:
            for rank in ranks:
                card = AttackCard(rank, colour)
                self.deck.append(card)
                
    def shuffle(self):
        import random
        random.shuffle(self.deck)
        
    def draw_one(self):
        return self.deck.pop(0)

class PowerDeck():
    def __init__(self):
        self.deck = []  
        for i in range(4):
            for colour in colours:
                for power in powers:
                    booster = PowerUpCard(power, colour)
                    self.deck.append(booster)
        
        for colour in colours:
            for superpower in superpowers:
                booster = SuperpoweredCard(superpower,colour)
                self.deck.append(booster)
                
    def shuffle(self):
        import random
        random.shuffle(self.deck)
        
    def draw_one(self):
        return self.deck.pop(0)

def player_input():
    
    input(f'{player.name} draws a card...')

attack_deck = AttackDeck()
power_deck = PowerDeck()

def roll_the_die():
    input(f'{player.name} is rolling the die...')
    import random
    x = random.randint(1,6)
    return x

def replace(card):
    power_deck.deck.append(card)
    card_num = player.deck.index(card)
    player.deck.pop(card_num)

def card_index_input():
    while True:
        try:
            user_input = input('Please choose a power-up. Type in the number of the power, or skip. Ans: ')
            if user_input.lower() == 'skip':
                user_input = 101
            input_int = int(user_input) - 1
            return input_int
        except:
            print('Input a proper number!')
            continue
        break

def check_energy(value):
    player.energy -= value
    if player.energy < 0:
        player.energy += value
        print('\n'*5 + 'Not enough energy!')
        print(player)
        player.deck_display()
        return False
    else:
        return True

def power_confirm():
    while True:
        i = input('Continue? yes / no Ans: ')
        if i.lower() == 'no':
            print('\n'*5)
            print(player)
            player.deck_display()
            return False
            break
        elif i.lower() == 'yes':
            return True
            break
        print('Input yes or no!')

def power_up():
    while True:
        chosen_index = card_index_input()
        if  chosen_index == 100:
            print('Power-up skipped.')
            break
            
        if chosen_index not in range(len(player.deck)):
            print('Please input a number within the range of your deck.')
            continue
        
        card = player.deck[chosen_index]
        if not card.super:
            var = card.power

            if var == 'shield':
                print('Shield negates damage taken by next attack.')
                print('Uses 1 energy.')

                check = power_confirm()
                if not check:
                    continue

                check_2 = check_energy(1)
                if not check_2:
                    continue

                player.shield = True
                
            elif var == 'acid spray':
                print('Deals 6 damage to all enemies, and applies corrosion.')
                print('Corrosion lasts for 3 turns. Reduces turret damage by 3, and deals 3 damage each turn.')
                print('Uses 4 energy.')

                check = power_confirm()
                if not check:
                    continue

                check_2 = check_energy(4)
                if not check_2:
                    continue
                
                dmg = player.damage_processing(6)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                    person.corrode += 3

            elif var == 'extended magazine':
                print('Extended magazine allows for one additional turn for the player.')
                print('Uses 2 energy.')

                check = power_confirm()
                if not check:
                    continue

                check_2 = check_energy(2)
                if not check_2:
                    continue

                player.extended_mag += 1
                
            elif var == 'armour piercing rounds':
                print("Armour piercing rounds eliminates target's shields, and deals an additional 2 damage.")
                print('Uses 2 energy.')

                check = power_confirm()
                if not check:
                    continue

                check_2 = check_energy(2)
                if not check_2:
                    continue

                player.armour_pierce = True

            elif var == 'bullet spray':
                print('Deals 5 damage to all enemies. Subject to buffs.')
                print('Uses 1 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(1)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(5)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                
            elif var == 'double damage':
                print('Doubles the base damage dealt by the player for the entire turn.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                    
                player.x2_dmg = True

            elif var == 'bullet barrage':
                print('Deals 5 damage to target, and 5 damage to all enemies.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(5)
                target.dmg_received(dmg)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)

            elif var == 'turret disabler':
                print('Disables target enemy turret for the next turn.')
                print('Uses 1 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(1)
                if not check_2:
                    continue
                    
                target.stun = True

            elif var == 'corrosive gas':
                print('Corrosive gas corrodes enemy turrets.')
                print('Uses 2 energy.')
                print("Corrosion lasts for 3 turns. Reduces affected turret's damage by 3, and deals 3 damage each turn.")
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                for person in player_list:
                    if person == player:
                        continue
                    person.corrode += 3

            elif var == 'electro cannon':
                print('Deals 10 damage to target and removes 5 energy from target.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(10)
                target.dmg_received(dmg)
                target.energy -= 5
                while target.energy < 0:
                    target.energy += 1 

            elif var == 'flamethrower':
                print('Deals 7 damage to and burns the target.')
                print('Burning lasts for 4 turns, and deals 3 damage each turn.')
                print('Uses 1 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(1)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(7)
                target.dmg_received(dmg)
                target.burn += 4

            elif var == 'mechanic fix':
                print('Mechanic fix restores 15 health, and clears all negative status effects.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                player.health += 15
                player.burn = 0
                player.corrode = 0
                player.vulnerable = 0
            
            elif var == 'spare parts':
                print('Spare parts restores 10 health.')
                print('Does not require energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                player.health += 10

            elif var == 'air drop':
                print('Calls in for supplies, randomly ranging from power-up draws, health restoration, shield activation or energy restoration.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                    
                input('Opening air drop...')
                from random import randint
                integer = randint(1,8)
                
                if integer == 1 or integer == 5:
                    print('Batteries found!')
                    energy = randint(4,8)
                    player.energy += energy
                    print(f'{player.name} has restored {str(energy)} energy from the air drop supplies!')
                    
                elif integer == 2 or integer == 6:
                    print('Turret parts obtained!')
                    health = randint(10,20)
                    player.health += health
                    print(f'{player.name} has restored {str(health)} health from the air drop supplies!')
                    
                elif integer == 3 or integer == 7:
                    print('Shield found!')
                    player.shield = True
                    
                else:
                    print('Power-ups found!')
                    card_num = randint(2,5)
                    for number in range(card_num):
                        player.deck.append(power_deck.draw_one())
                        
                    print(f'{str(card_num)} cards found from the air drop supplies!')

            elif var == 'grenade blast':
                print('Deals 7 damage to all enemies. Applies burn.')
                print('Burn lasts for 4 turns, and deals 3 damage each turn.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                  
                dmg = player.damage_processing(7)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                    person.burn += 4
                
            elif var == 'assault drone':
                print('Assault drone deals 3 damage to target every time the player attacks.')
                print('Uses 5 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(5)
                if not check_2:
                    continue
                    
                player.drone = True
                
            elif var == 'armoured convoy':
                print('Summons an armoured vehicle to provide cover and support fire.')
                print('Deals 3 damage to all enemies at the start of every turn.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                player.armour += 10
                
            elif var == 'shady deals':
                print('Player loses 10 health, but gains 5 energy and 2 power-ups at random.')
                print('Does not use energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                player.health -= 10
                player.energy += 5
                for i in range(2):
                    player.deck.append(power_deck.draw_one())
                
            elif var == 'bomb':
                print('Deals 7 damage to all enemies. Applies vulnerable.')
                print('Vulnerable lasts for 3 turns, and increases damage taken by 2.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(7)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                    person.vulnerable += 3
                
            elif var == 'energy assimilator':
                print('Absorbs 5 energy from target player.')
                print('Does not use any energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                target.energy -= 5
                player.energy += 5
                if target.energy < 0:
                    target.energy = 0
                
            elif var == 'healing drone':
                print('Activates a drone that heals by 5 points at the start of every turn.')
                print('Uses 4 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(4)
                if not check_2:
                    continue
                
                player.regen = True
                
            elif var == 'tesla discharge':
                print('Tesla discharge removes 7 energy from all enemies.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                for person in player_list:
                    if person == player:
                        continue
                    person.energy -= 7
                    if person.energy < 0:
                        person.energy = 0
            
            elif var == 'instant fix':
                print('Restores  6 health and 3 energy, and clears all negative effects.')
                print('Uses no energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                player.health += 6
                player.energy += 3
                while player.burn > 0:
                    player.burn -= 1
                while player.corrode > 0:
                    player.corrode -= 1
                while player.vulnerable > 0:
                    player.vulnerable -= 1
            
            elif var == 'spare battery':
                print('Spare battery replenishes 5 energy.')
                print('Does not use any energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                player.energy += 5
            
            elif var == 'supercharger':
                print('Replenishes 15 energy, but applies burn to the player.')
                print('Burn lasts for 3 turns, and deals 3 damage each turn.')
                print('Does not use energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                player.energy += 15
                player.burn += 3
            
            elif var == 'defensive systems':
                print('Reduces damage taken by 1. Effects are stackable.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                player.defense += 1
            
            elif var == 'reflective system':
                print('Returns 2 damage back at the opponent every time damage is received.')
                print('Lasts until the next turn.')
                print('Uses 1 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(1)
                if not check_2:
                    continue
                    
                player.mirror = True
            
            elif var == 'EMP blast':
                print('Disables all enemy defensive systems, apart from support units (Drones, armoured convoy etc.).')
                print('Enemies also cannot attack for the next turn.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                
                for person in player_list:
                    if person == player:
                        continue
                    while person.defense > 0:
                        person.defense -= 1
                    person.shield = False
                    person.stun = True
                    person.bps = False
            
            elif var == 'ballistic shield':
                print('Provides a protective shield that protects from all incoming damage, except from tortures.')
                print('Lasts until the next turn.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                    
                player.bps = True
            
            elif var == 'flame barrels':
                print('Deals 10 damage to and burns all turrets.')
                print('Burning lasts for 4 turns, and deals 3 damage each turn.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(10)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                    person.burn += 4
            
        else:
            var = card.superpower
            #For superpowered cards.
            if var == 'tank':
                print('Tank provides an armour of 20 points to the player, and deals an additional 5 damage to damaged enemies.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                player.tank += 20
            
            elif var == 'special air drop':
                print('The special air drop provides 5 random power-ups, and restores 20 health and 10 energy.')
                print('Uses 5 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(5)
                if not check_2:
                    continue
                    
                player.health += 20
                player.energy += 10
                
                for num in range(5):
                    player.deck.append(power_deck.draw_one())
            
            elif var == 'air support':
                print('Air support both heals the player and damages targeted enemies.')
                print('At the start of the turn, drops packages containing spare parts that restore 3 health.')
                print('Deals an additional 5 damage to damaged enemies.')
                print('Uses 6 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(6)
                if not check_2:
                    continue
                    
                player.air_support = True
            
            elif var == 'elite deal':
                print('Elite deal restores 5 energy, and allows the player to draw 5 power-ups at random.')
                print('Uses no energy.')
                
                check = power_confirm()
                if not check:
                    continue

                player.energy += 5
                for num in range(5):
                    player.deck.append(power_deck.draw_one())
            
            elif var == 'nuclear blast':
                print('Deals 25 damage to all enemies, and applies burn.')
                print('Burn lasts for 4 turns, and deals 3 damage each turn.')
                print('Uses 20 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(20)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(25)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                    person.burn += 4
            
            elif var == 'heavy duty battery':
                print('Gives the user 20 energy.')
                print('Uses no energy.')
                
                check = power_confirm()
                if not check:
                    continue
                
                player.energy += 20
            
            elif var == 'upgrade kit':
                print('Increases the defense of the turret by 2, and permanently increases the damage dealt by 2.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                    
                player.defense += 2
                player.increased_dmg += 2
            
            elif var == 'grenade launcher':
                print('Increases permanently the damage dealt by 2 and inflicts burn for every attack.')
                print('Burn lasts for 1 turn, and deals 3 damage each turn.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                    
                player.increased_dmg += 2
                player.g_launcher = True
            
            elif var == 'extra turret':
                print('Provides the player with another turret, with 25 health.')
                print("When the player's turret is destroyed, the new turret will be in use.")
                print('Uses 5 energy.')
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(5)
                if not check_2:
                    continue
                    
                player.turret += 1
            
            elif var == 'bazooka':
                print('Deals 15 damage to target, and applies burn to all enemies.')
                print('Burn lasts for 5 turns, and deals 3 damage each turn.')
                print('Uses 6 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(6)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(15)
                target.dmg_received(dmg)
                for person in player_list:
                    if person == player:
                        continue
                    person.burn += 5
            
            elif var == 'FUBAR':
                print('Deals 35 damage to target enemy. Enemy is as good as gone.')
                print('Uses 10 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(10)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(35)
                target.dmg_received(dmg)
            
            elif var == 'anti-air systems':
                print('Anti-air systems disable all enemy drones.')
                print('Uses 2 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(2)
                if not check_2:
                    continue
                    
                for person in player_list:
                    if person == player:
                        continue
                    person.drone = False
                    person.regen = False
                    person.air_support = False
            
            elif var == 'railgun':
                print('Deals 10 damage to target, and 10 damage to all enemies. Disables all enemy turrets.')
                print('Uses 8 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(8)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(10)
                target.dmg_received(dmg)
                for person in player_list:
                    if person == player:
                        continue
                    person.dmg_received(dmg)
                    person.stun = True
            
            elif var == 'gravitron':
                print('Unleashes a gravity-distorting attack, dealing 15 damage to target.')
                print('Removes 3 random power-ups from target.')
                print('Uses 5 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(5)
                if not check_2:
                    continue
                    
                dmg = player.damage_processing(15)
                target.dmg_received(dmg)
                
                for i in range(3):
                    try:
                        power_deck.deck.append(target.deck.pop(0))
                    except:
                        break
            
            elif var == 'cluster missiles':
                print('Bypassing all defenses, it removes 20 health from target. Not subject to buffs.')
                print('Uses 3 energy.')
                
                check = power_confirm()
                if not check:
                    continue
                    
                check_2 = check_energy(3)
                if not check_2:
                    continue
                
                target.health -= 20
            
        replace(card)
        break

def revive(active_turret):
    if active_turret.health <= 0:
        if active_turret.turret > 0:
            active_turret.turret -= 1
            print('Extra turret used.')
            active_turret.health = 25
            active_turret.energy = 5
            active_turret.burn = 0
            active_turret.corrode = 0
            active_turret.vulnerable = 0
            active_turret.defense = 0
            active_turret.increased_dmg = 0
            active_turret.shield = False
            active_turret.stun = False
            active_turret.x2_dmg = False
            active_turret.armour_pierce = False
            active_turret.mirror = False
            active_turret.bps = False
            active_turret.g_launcher = False

def check_tortures():
    if player.burn > 0:
        player.burn -= 1
        player.dmg_received(3)
        print(f'Burning: Deals 3 damage. {str(player.burn)} turns left.')
    if player.corrode > 0:
        player.corrode -= 1
        player.dmg_received(3)
        print(f'Corrosion: Deals 3 damage. {str(player.corrode)} turns left.')
    if player.regen:
        player.health += 5
        print('Healed by 5 points by healing drone.')
    if player.air_support:
        player.health += 3
        print('Healed by 3 points by air support.')

#GAME LOGIC
game_on = True
while game_on:
    player_list.extend(new_list)
    new_list = []
    from random import shuffle
    shuffle(player_list)
    input('Randomising playing sequence...')
    print('The sequence of players will be as follows:')
    for player in player_list:
        print('\t' + player.name)
    input('Continue?')

    print('Welcome to the game!')    

    attack_deck.shuffle()
    power_deck.shuffle()

    print("Each player will start with three cards.")

    for player in player_list:
        for i in range(3):
            player.deck.append(power_deck.draw_one())
        
    for player in player_list:
        while True:
            ask = input(f'{player.name}, do you want to show your cards? yes / no Ans: ')
            if ask.lower() != 'yes' and ask.lower() != 'no':
                print('Please input yes or no!\n')
                continue
            if ask.lower() == 'yes':
                player.deck_display()
                print('\n')
                input('Continue?')
                break
            else:
                print('\n')
                break

    while len(player_list) > 1:
        for player in player_list:
            attack_deck.shuffle()
            power_deck.shuffle()
            while True:
                print('\n'*5)
                input(f"{player.name}'s turn...")
                if player.mirror:
                    print('Reflective system expires.')
                player.mirror = False

                if player.bps:
                    print('Ballistic shield expires.')
                player.bps = False
                
                #Handling of tortures.
                check_tortures()
                revive(player)
                if player.health <= 0:
                    print(f"{player.name}'s turret has been destroyed, and is disqualified from the game!")
                    loser = player_list.index(player)
                    loser_player = player_list.pop(loser)
                    new_list.append(loser_player)
                    break
                    
                #Handling of the armoured convoy's support fire.
                if player.armour > 0:
                    print('Armoured convoy fires at all enemy turrets.')
                    for person in player_list:
                        if person == player:
                            continue
                        person.dmg_received(3)
                        revive(person)
                        if person.health <= 0:
                            loser = player_list.index(person)
                            loser_player = player_list.pop(loser)
                            new_list.append(loser_player)
                if player.health <= 0:
                    break
                            
                #Handling of stun.
                if player.stun:
                    player.stun = False
                    print(f"{player.name}'s turret has been disabled.")
                    break
                    
                #Handling of targeting system.
                while True:
                    turn_card = attack_deck.draw_one()
                    target = player.turn_card(turn_card)
                    if target == player:
                        input('Self-harm is not encouraged in this game. Drawing another card...')
                        continue
                    break
                input(f'{target.name} has been targeted...')
                
                #Handling of power-up draws. (3 times)
                die_num = roll_the_die()
                print(f'{player.name} has rolled a die value of {str(die_num)}.')
                if die_num == 1:
                    print('Gain 1 energy and 1 power-up card.')
                    player.energy += 1
                    player.deck.append(power_deck.draw_one())
                if die_num == 2:
                    print('Gain 2 power-up cards.')
                    for num in range(2):
                        player.deck.append(power_deck.draw_one())
                if die_num == 3:
                    print('Gain 3 energy.')
                    player.energy += 3
                if die_num == 4:
                    print('Gain 2 energy and 2 power-up cards.')
                    player.energy += 2
                    for num in range(2):
                        player.deck.append(power_deck.draw_one())
                if die_num == 5:
                    print('Gain 2 energy and 3 power-up cards.')
                    player.energy += 2
                    for num in range(3):
                        player.deck.append(power_deck.draw_one())
                if die_num == 6:
                    print('Gain 3 energy and 3 power-up cards.')
                    player.energy += 3
                    for num in range(3):
                        player.deck.append(power_deck.draw_one())
                print('\n'*5)
                print(f'{player.name} can now use 3 power-ups.')
                for num in range(3):
                    print(player)
                    player.deck_display()
                    power_up()
                    brk_lp = False
                    if player.health <= 0:
                        brk_lp = True
                    for person in player_list:
                        revive(person)
                        if person.health <= 0:
                            print(f"{person.name}'s turret has been destroyed. {person.name} is out of the game!")
                            loser = player_list.index(person)
                            loser_player = player_list.pop(loser)
                            new_list.append(loser_player)
                            if len(player_list) < 2:
                                break
                        if brk_lp:
                            break

                if target.health <= 0:
                    break
                #Damage dealt to targeted player.
                strike_card = attack_deck.draw_one()
                raw_dmg = player.dmg_card(strike_card)
                dmg = player.damage_processing(raw_dmg)
                target.dmg_received(dmg)
                
                revive(target)
                if target.health <= 0:
                    loser = player_list.index(target)
                    l = player_list.pop(loser)
                    new_list.append(l)
                    print(f"{target.name}'s turret has been destroyed. {target.name} is out of the game!")
                    break
                    
                #Continue the loop.
                player.armour_pierce = False
                player.x2_dmg = False
                input('Continue?')
                if player.extended_mag > 0:
                    player.extended_mag -= 1
                    continue
                    
                break
                
    if len(player_list) == 1:
        winner = player_list[0]
        print('\n'*5)
        print(f'{winner.name} is the winner for this round!')
    else:
        print('Nobody has survived this round. Good luck next time!')

    while True:
        c = input('Do you want to play another round? yes / no Ans: ')
        if c.lower() != 'yes' and c.lower() != 'no':
            print('Input yes or no!')
            continue
        break
    if c.lower() == 'no':
        break

input('GAME OVER')
