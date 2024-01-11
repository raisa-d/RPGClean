class Character():
    def __init__(self, name, HP, maxHP, AC, strMod, dexMod, equippedWeapon=None):
        self.name = name
        self.HP = HP
        self.maxHP = maxHP
        self.AC = AC
        self.strMod = strMod
        self.dexMod = dexMod
        self.equippedWeapon = equippedWeapon

class Player(Character):
    def __init__(self, name, HP, maxHP, gp, strAbility, strMod, dexAbility, dexMod, constAbility, constMod, intAbility, intMod, wisAbility, wisMod, charAbility, charMod, profBonus, xp, AC, crimeNum, equippedWeapon=None, equippedTek=None, inv=None):
        super().__init__(name, HP, maxHP, AC, strMod, dexMod, equippedWeapon)
        self.gp = gp

        # D&D ability scores/modifiers
        self.strAbility = strAbility
        self.dexAbility = dexAbility
        self.constAbility = constAbility
        self.constMod = constMod
        self.intAbility = intAbility
        self.intMod = intMod
        self.wisAbility = wisAbility
        self.wisMod = wisMod
        self.charAbility = charAbility
        self.charMod = charMod
        self.profBonus = profBonus
        
        self.crimeNum = crimeNum
        self.xp = xp
        self.equippedTek = equippedTek
        
        # doing this so we don't have a mutable list set as the default
        if inv is None:
            self.inv = {}
        else:
            self.inv = inv

        # track exhaustion level
        self.exhaustion_level = 0 
        # handles dodging state for Battle
        self.is_dodging = False
    
    def addToInv(self, item, quantity):
        # if already have this item in inventory, add to quantity
        if item in self.inv: 
            self.inv[item] += quantity
        # if don't already have this item create new entry in inventory
        else:
            self.inv[item] = quantity