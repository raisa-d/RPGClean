import random as r

def diceRoll(numOfSides):
  roll = r.randint(1, numOfSides)
  return roll

def disadvantageWNarration():
    print("\nDue to exhaustion, you have a disadvantage.")
    disadvantageRoll()

def disadvantageRoll():
    roll1 = diceRoll(20)
    roll2 = diceRoll(20)
    final_roll = min(roll1, roll2)
    return final_roll

def skillCheck(user, DC, skillName, narration=False):
    # roll with a disadvantage on skill checks if exhaustion level 1
    if user.exhaustionLevel == 1:
        if narration == True:
            roll = disadvantageWNarration()
        else:
            roll = disadvantageRoll()
    
    # if not exhausted, roll d20 normally
    else:
        roll = diceRoll(20)
    
    # add ability modifier to roll depending which skill name
    if skillName == 'str':
        skillCheck = roll + user.strMod
    elif skillName == 'dex':
        skillCheck = roll + user.dexMod
    elif skillName == 'int':
        skillCheck = roll + user.intMod
    elif skillName == 'wis':
        skillCheck = roll + user.wisMod
    elif skillName == 'char':
        skillCheck = roll + user.charMod
    
    # compare skillCheck to damage class
    if skillCheck > DC:
        return True # pass check
    else:
        return False # fail check