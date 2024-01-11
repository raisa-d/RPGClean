from util import clear, bold, cyan, end

# introductory scene that orients player in game
def introScene(): 
    clear()
    print("When the nuclear apocalypse destroyed Earth, groups\nof lucky individuals made it onto 13 space stations\nand shot themselves into space to ensure the survival\nof the human race. 12 space stations joined together\nand were renamed the Ark.")
    print("\nOn the Ark, every crime is punishable by death unless\nyou are under 18 years old, in which case, you get\nimprisoned in the Sky Box.")
    print("\n97 years post-apocalypse, and 100 years before the\nEarth will be survivable again, you\nare a prisoner on the Ark.\n")
    input(f"[{bold}{cyan}Enter{end}] to choose the crime that got landed you in the Ark prison\n")