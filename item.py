from util import bold, end, green

# create item class
class Item:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price

# create weapon class
class Weapon(Item):
    def __init__(self, name, desc, price, finesse, melee, range, numOfSides):
        super().__init__(name, desc, price)
        self.finesse = finesse
        self.melee = melee
        self.range = range
        self.numOfSides = numOfSides

# create potion class
class Potion(Item):
    pass

# create tek class
class Tek(Item):
    def __init__(self, name, desc, price, effects):
        super().__init__(name, desc, price)
        self.effects = effects

# create food class
class Food(Item):
    def __init__(self, name, desc, price):
        super().__init__(name, desc, price)

# create drink class
class Drink(Item):
    def __init__(self, name, desc, price, numOfSips):
        super().__init__(name, desc, price)
        self.numOfSips = numOfSips # total number of sips drink can provide
        self.remainingSips = numOfSips # number of remaining sips in drink

# weapon objects
glaive = Weapon('glaive', 'This glaive boasts a gleaming obsidian blade with intricate,\nethereal runes etched along its length, set upon a polished, ebony-hued\nshaft adorned with menacing, dragon-shaped pommel.', 20, False, True, False, 10)
rapier = Weapon('rapier', 'This rapier is an elegantly slender and silvered blade,\nits handle intricately adorned with sapphire-encrusted crossguards\nand a hilt of black leather wrapped in silver thread.', 25,False, True, False, 8)
dagger = Weapon('dagger', 'The dagger gleams with a wickedly curved obsidian blade,\na hilt wrapped in midnight-blue leather, and\na pommel adorned with a menacing onyx gemstone.', 4,True, False, False, 4)
crossbow = Weapon('crossbow', 'This crossbow features a sleek, polished mahogany stock adorned\nwith intricate ivory inlays, a glistening steel barrel, and an\nexquisitely carved ebony trigger guard, giving it\nan air of both beauty and deadly precision.', 25,False, False, True, 8)
butterflySword = Weapon('butterfly sword', 'The butterfly sword boasts a pair of elegantly slender blades\nwith intricately carved jade hilts, their unique S-shaped guards\ndesigned for fluid, acrobatic combat Tekniques.', 10,True, False, False, 6)
reaperStick = Weapon('reaper stick', 'WRITE DESCRIPTION', 10,False, True, False, 8)
reaperCleaver = Weapon('reaper cleaver', 'The Reaper Cleaver is a massive, double-edged greataxe\nwith a rusted and jagged blade, imbued with a menacing aura,\nsuggesting the cruelty of its wielder.', 30,False, True, False, 8)
multipurposeKnife = Weapon('multipurpose knife', 'A compact tool featuring a sharp blade,\nserrated edge, firestarter, bone saw, and an LED flashlight', 50,False, True, False, 6)
throwingKnives = Weapon('throwing knives', 'Set of 5 sleek, lightweight knives balanced for precision,\nmaking them deadly when thrown accurately or used up close.', 10,True, False, False, 4)
shiv = Weapon('shiv', 'A small, sharp blade attached to a handle\nmade from scrap metal', 0,False, True, False, 6)
wrench = Weapon('mechanical wrench blade', 'Combines a a sturdy metal wrench with a retractable, razor-sharp blade\nOriginally designed for enginering repairs, the blade can be extended\nfor use as a melee weapon.', 0,False, True, False, 8)
shortbow = Weapon('shortbow', 'The shortbow\'s silent operation and lightweight design\nmake it an excellent choice for individuals relying on stealth\nand precision in their encounters', 25,False, False, True, 6)
weaponsAll = [glaive, rapier, dagger, crossbow, butterflySword, reaperStick, reaperCleaver, multipurposeKnife, throwingKnives, shiv, wrench, shortbow]
weaponsForSale = [glaive, rapier, dagger, crossbow, butterflySword, reaperStick, reaperCleaver, multipurposeKnife, throwingKnives, shortbow]

# tek objects
wristband = Tek('wristband', 'These wristbands came with the original Ark prisoners to the ground.\nThey were used to measure their vital signs and to\ncommunicate with those still on the Ark.', 50, 'This helpful wristband will give you radiation alerts and night-vision.')

# consumable objects
rations = Food("1 days rations", "WRITE DESC", 5)
smallWaterskin = Drink("small waterskin", "WRITE DESC", 2, numOfSips=3)
largeWaterskin = Drink("large waterskin", "WRITE DESC", 4, numOfSips=5)
consumables_all = [rations, smallWaterskin, largeWaterskin]