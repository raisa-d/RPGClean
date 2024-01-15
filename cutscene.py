from util import clear, bold, cyan, end, red, enter
import time as t

# introductory scene that orients player in game
def introScene(): 
    clear()
    print("When the nuclear apocalypse destroyed Earth, groups\nof lucky individuals made it onto 13 space stations\nand shot themselves into space to ensure the survival\nof the human race. 12 space stations joined together\nand were renamed the Ark.")
    print("\nOn the Ark, every crime is punishable by death unless\nyou are under 18 years old, in which case, you get\nimprisoned in the Sky Box.")
    print("\n97 years post-apocalypse, and 100 years before the\nEarth will be survivable again, you\nare a prisoner on the Ark.\n")
    input(f"[{bold}{cyan}Enter{end}] to choose the crime that got landed you in the Ark prison\n")

def arriveAtDropship():
    clear()
    print('You approach the Boarding Bay. When you get there, you see\nprisoners being pushed into a dropship, strapped into\na seat, and tagged with a wristband.')
    print('\nSuddenly, you are being shoved into a seat and a wristband is\nclamped onto your wrist. It pinches a little bit.')
    print("\nOnce everyone is seated, a video of the Chancellor begins playing. He says:")
    print(f"\n{bold}{red}\"You are being sent to the ground to see if mankind can\nsurvive there. As you are criminals, we felt you were expendable.\n\nWe are dropping you on Mount Weather, where there is a bunker\nthat can supply 300 people for two years. Find those supplies\nas your life may depend on it.\n\nIf you do survive on Earth, your crimes will be forgiven.\"{end}")
    print("\nThe dropship doors close.")
    enter()

def launchDropship():
    clear()
    print('LAUNCHING DROPSHIP IN')
    t.sleep(0.5)
    print('3...')
    t.sleep(1)
    print("2...")
    t.sleep(1)
    print("1...")
    t.sleep(1)
    print("\nYou launch into space.")
    t.sleep(1)
    print("\nYour body fills with exhilaration and fear as you hurtle through\nEarth's atmosphere. The anticipation of stepping outside and\nonto the ground makes your heart pound violently.")
    enter()