import time as t
from util import clear, bold, end, enter, red, white, green, orange
from cutscene import arriveAtDropship, launchDropship
from skillCheck import skillCheck

##### Go To Earth Events #####
def goToEarth(user):
    travelToDropship(user)
    arriveAtDropship()
    launchDropship()
    dropshipMalfunction(user)
    seeEarth()

def guardInteraction():
    clear()
    print('Guards suddenly rush into your cell and bark at you, "Let\'s go!"\nThey take you by your arm and drag you down the Ark corridors.')
    print('\nYou look around and see that the other prisoners are being\nherded in the same direction, looking terrified.\n')
    print('Do you...\na) try to ask the guard where they are taking you\nb) stay quiet')

def travelToDropship(user):
    while True:
        guardInteraction()
        speakUp = input('\n> ').strip().lower()
        
        ### change reactions to speaking up? make user be able to interact back instead of it being a sort of static response
        if speakUp == 'a':
            print(f'{bold}The guard shoots you a menacing expression and grunts at you.')

            if user.crimeNum == 0: # vital supplies
                print(f'\nYou make eye contact with the prisoner to your left and try to\nnonverbally communicate "What the **** is going on?"\n\nThe prisoner gives you some side-eye.{end}')
                enter()
                break

            elif user.crimeNum == 1: # rebellion leader
                ### this NPC was arrested for treason? define who these prisoners are
                print(f'\nYou exchange a glance with another prisoner, who mouths to you\nin a panic: "They\'re sending us...down.{end}"') 
                enter()
                break

            elif user.crimeNum == 2: # cannabis thief
                print(f'\nYou realize you\'re still a little bit baked from smoking\nthe last of the stash you had hidden in the air ducts in your cell.\n\nYou begin to realize you have no clue what\'s going on.{end}') ### 
                enter()
                break

            elif user.crimeNum == 3: # 2nd child
                print(f'\nAnother prisoner tries to get your attention\nand has a panicked look on their face.{end}') ###
                enter()
                break

            elif user.crimeNum == 4: # falsely accused
                print(f'\nYou look to your right and see a prisoner nearby\nstruggling to get out of a guard\'s grasp{end}')
                enter()
                break
        
        elif speakUp == 'b':
            ### you observe your surroundings and see worried faces, clues as to what could be happening
            print(f'The prisoner next to you is yelling "Where are you taking us?!" at one of the Guard members,\nwho maintains a cold and aggressive expression.{end}')
            enter()
            break
        
        # input error handling
        else:
            print(f"{red}{bold}Invalid command.{green}\nValid commands:\n{white}['a', 'b']{end}")
            enter()
            clear()
            continue

### continue coding rest of this function
def dropshipMalfunction(user):
    clear()
    print(f"\n{bold}Suddenly, the descent turns into a {red}chaotic freefall.{white} The dropship\nshakes aggressively and you all try to grip anything stable. The\nengine becomes very loud, intesifying the feeling of {orange}imminent\ndanger{white} and helplessness.{end}")
    t.sleep(1)

    while True:
        print("\nDo you...\na) attempt to fix the issue or\nb) brace for impact?")
        fixOrBrace = input("> ").strip().lower()

        if fixOrBrace in ['a', 'fix', 'f', 'fix the issue', 'attempt to fix the issue'] or fixOrBrace[0] == 'a':
            clear()

            print(f"\n{user.name} will use an investigation skill check to assess the malfunction")

            ### add skill check here
            invCheck = skillCheck(user, 8, 'int', narration=True)

            if invCheck:
                print("\nYou have successfully identified a damaged component in the dropship's propulsion system.")
                enter()
            else:
                print("\nYou were unsuccessful and did not figure out the source of the malfunction.\n")
                braceForImpact(user)
                enter()
                break
        
        elif fixOrBrace in ['b', 'brace', 'brace for impact'] or fixOrBrace[0] == 'b':
            braceForImpact(user)
        
        ### create error handling for incorrect input
        else:
            pass

### write
def seeEarth():
    print('you are seeing earth')

### write
def braceForImpact(user):
    print('you are bracing for impact')