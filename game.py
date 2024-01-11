import pickle
import time as t
from util import clear, draw, bold, end, cyan, enter, red, green, orange, yellow
from cutscene import introScene
from crime import crimeList
from character import Player
from item import smallWaterskin, multipurposeKnife, wristband, rations, throwingKnives, shiv, dagger, wrench

# booleans for whether game is running/game is being played
gameRunning = True
playingGame = False

# Game class
class Game():
    def init__(self):
        self.player = None

    # function to start the game and initialize the player
    def startGame(self):
        # when player begins game, mainMenu is true
        mainMenu = True
        while mainMenu:
            ### need to store instance of player in self.player somehow, this does not work v 
            self.menu(self.player)
    
    def menu(self, user):
        # print game menu
        clear()
        draw()
        print('1. New Game\n2. Load Game\n3. Quit game')
        draw()
        print('Please enter the number that corresponds with the option\nyou are choosing or the first letter of said option.')

        # store user input, remove whitespace, make lowercase
        menuChoice = input('> ').strip().lower()

        # if user chooses new game
        if menuChoice in ['1', 'n', 'new', 'new game']:
            self.newGame()
        
        # if user chooses load game
        elif menuChoice in ['l', 'load', 'load game']:
            pass
            
        # if user chooses to exit
        elif menuChoice in ['x', 'exit', 'l']:
            saveGame(user, 'load.json')
            print('Goodbye!')
            quit()
    
    def newGame(self):
        # play introduction scene
        introScene()

        # user chooses their crime/class
        self.createPlayer()

    @staticmethod
    def assignPlayer(name, index):
        # vital supplies thief
        if index == 0:
            # instantiate player object
            player = Player(name, 11, 11, 10, 14, 2, 15, 2, 16, 3, 13, 1, 11, 0, 9, -1, 2, 0, 12, 0, multipurposeKnife, wristband, {})

            # add starting equipment to inventory
            player.addToInv(multipurposeKnife, 1)
            player.addToInv(wristband, 1)
            player.addToInv(rations, 2)
            player.addToInv(smallWaterskin, 1)

            return player
        
        # rebellion leader
        elif index == 1:
            player = Player(name, 12, 12, 10, 16, 3, 14, 2, 15, 2, 9, -1, 11, 0, 13, 1, 2, 0, 12, 1, throwingKnives, wristband, {})
            player.addToInv(throwingKnives, 1)
            player.addToInv(wristband, 1)
            player.addToInv(rations, 2)
            player.addToInv(smallWaterskin, 1)

            return player

        # cannabis thief
        elif index == 2:
            player = Player(name, 10, 10, 10, 13, 1, 14, 2, 15, 2, 11, 0, 16, 3, 9, -1, 2, 0, 12, 2, shiv, wristband, {})
            player.addToInv(shiv, 1)
            player.addToInv(wristband, 1)
            player.addToInv(rations, 2)
            player.addToInv(smallWaterskin, 1)

            return player

        # second child
        elif index == 3:
            player = Player(name, 12, 12, 10, 16, 3, 15, 2, 14, 2, 11, 0, 9, -1, 13, 1, 2, 0, 12, 3, dagger, wristband, {})
            player.addToInv(dagger, 1)
            player.addToInv(wristband, 1)
            player.addToInv(rations, 2)
            player.addToInv(smallWaterskin, 1)

            return player

        # falsely accused
        elif index == 4:
            player = Player(name, 10, 10, 10, 16, 3, 15, 2, 14, 2, 9, -1, 13, 1, 11, 0, 2, 0, 13, 4, wrench, wristband, {})
            player.addToInv(wrench, 1)
            player.addToInv(wristband, 1)
            player.addToInv(rations, 2)
            player.addToInv(smallWaterskin, 1)    

            return player

        ### change this to be error handling
        else:
            print('that didn\'t work hm')
            enter()

        return player

    # have user choose their crime/class
    def createPlayer(self):
        while True:
            clear()
            # prompt user to choose crime
            print(f'{bold}What was your crime? Your crime choice will dictate\nwhat weapon you begin with as well as your ability scores.\n(type in the number that corresponds with each crime to see details)\n{end}')

            # print list of crimes
            printCrimeList()

            # store user's crime choice input as an integer
            crime = input('\n> ').strip().lower()

            # if the crime is a digit and between 1 and the length of the crime list
            if crime.isdigit() and 1 <= int(crime) <= len(crimeList):
                
                # convert user's choice into index
                crimeIndex = int(crime) - 1
                crimeChoice = crimeList[str(crimeIndex)]

                # print the title of the crime user chose
                print(f'{bold}{crimeChoice["title"]}{end}')
                
                # print crime menu options, have player choose their crime, and return their character's name
                ### not working as intended when try to hit back from crime menu
                charName = crimeMenu(crimeChoice)

                # based on crime they chose, instantiate the player object
                player = self.assignPlayer(charName, crimeIndex)

                print(player.name)
                enter()

            # invalid input
            else:
                print(f'{red}{bold}Invalid command.\n{green}Please enter the number that corresponds\nwith the crime your character has committed{end}')

def printCrimeList():
    draw()
    counter = 1
    for i in crimeList:
        print(f'{bold}{cyan}{counter}. {crimeList[i]["desc"]}\n{end}')
        counter += 1 
    draw()

def crimeMenu(crimeChoice):
    clear()
    printCrimeList()
    print(f'\n{bold}Back | {red}Skills | {orange}Items | {yellow}Implications | {green}Choose This Crime |{end}')

    # loop for choosing from crime menu
    while True:
        crimeInfo = input('\n> ').strip().lower()
        
        # if choose to see skills associated with crime
        if crimeInfo in ['s', 'skills', 'skill']:
            print(f'\n{bold}{crimeChoice["skills"]}{end}')
        
        elif crimeInfo in ['items', 'item']:
            print(f'\n{bold}{crimeChoice["items"]}{end}')

        elif crimeInfo in ['implications', 'imp', 'i']:
            print(f'\n{bold}{crimeChoice["implications"]}{end}')

        elif crimeInfo in ['b', 'back', 'x', 'exit', 'l', 'leave']:
            break

        # choose that crime   
        elif crimeInfo[0] == 'c':
            charName = input('\nWhat is your character\'s name?\n> ').strip().title()

            # force them to choose a character name
            while charName == '':
                charName = input('Please enter a name\n\n> ').strip().title()
            
            return charName
        
        # invalid input
        else:
            print(f"{red}{bold}Invalid command.\n{green}Valid commands:{end}\n['b', 'back', 'x', 'exit', 'l', 'leave'\n'skills', 'skill', 's'\n'items', 'item'\n'implications', 'imp', 'i'\n'choose', 'c']")
            enter()
            break

def saveGame(user, filename):
    try:
        with open(filename, "wb") as file:
            pickle.dump(user, file)
        print(f'{green}>> game saved <<{end}')
        t.sleep(0.5)
    except Exception as e:
        print(f"{red}Error saving game: {str(e)}{end}")

def loadGame(filename):
    try:
        with open(filename, "rb") as file:
            loaded_player = pickle.load(file)
        print(f'{green}>>loaded successfully<<{end}')
        return loaded_player
    except FileNotFoundError:
        print(">>no saved game found<<")
        return None
    except Exception as e:
        print(f"{red}Error loading game: {str(e)}")