#Ariana Ramos
#Period 1

import random

def rockpaperscissors():
    loop = True
    rock = False
    scissors = False
    paper = False
    npc_rock = False
    npc_scissors = False
    npc_paper = False
    wins = 0
    losses = 0

    print("Welcome to 'Rock Paper Scissors,' choose a move to proceed!")
    while loop == True: #Makes the game replayable
        print("Rock(1), Paper(2), or Scissors(3).")

        playermove = int(input("Select a move.")) #Sets the chosen move as true based on user input
        if playermove == 1:
               rock = True
        if playermove == 2:
               paper = True
        if playermove == 3:
               scissors = True

        npcmove = random.randint(1, 3) #Sets the chosen move as true based on random number
        if npcmove == 1:
               npc_rock =  True
        if npcmove == 2:
               npc_paper = True
        if npcmove == 3:
               npc_scissors = True

        #Determines whether the user won or lost
        if rock == True and npc_scissors == True:
               wins = wins + 1
               print("You won!")
        if paper == True and npc_rock == True:
               wins = wins + 1
               print("You won!")
        if scissors == True and npc_paper == True:
               wins = wins + 1
               print("You won!")
        elif rock == True and npc_rock == True:
               print("There was a draw!")
        elif paper == True and npc_paper == True:
               print("There was a draw!")
        elif scissors == True and npc_scissors == True:
               print("There was a draw!")
        elif rock == True and npc_paper == True:
               losses = losses + 1
               print("You lost. . .")
        elif paper == True and npc_scissors == True:
               losses = losses + 1
               print("You lost. . .")
        elif scissors == True and npc_rock == True:
               losses = losses + 1
               print("You lost. . .")

        #Sets the final scores
        print("These are the total scores:")
        print("Wins:" + str(wins))
        print("Losses:" + str(losses))

        #Resets all variables for potential replay
        rock = False
        scissors = False
        paper = False
        npc_rock = False
        npc_paper = False
        npc_scissors = False

        #Allows the user to play again
        print("Select 1 if you wish to exit.")
        loopexit = int(input("Exit or no?"))
        if loopexit == 1:
            loop = False


rockpaperscissors()
