#Pokemon Evolution Game

#Init

#Global Variables
import random
pokemon_level = 0
pokemon_name = "Pichu"
won_battles = 0
lost_battles = 0
repreat = True

#Functions

#creates the visual for the pokemon
def draw_pichu():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣷⠀⣀⣤⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⡖⠀⠀⠀
⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⢛⣿⢿⣿⡟⠋⠀⠀⠀⠀
⣿⣿⣿⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠠⣾⣿⡿⠋⠀⠈⠀⢸⣿⡇⠀⠀⠀⠀⠀
⢻⣿⣿⣟⠻⣿⣿⣷⣦⣀⠀⠀⠀⠀⠀⠻⠉⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀
⢸⣿⣟⠿⠀⠀⠉⠛⢿⣿⡇⠀⠀⠀⠀⠈⡀⠀⠀⠀⠀⠀⣿⣿⠇⠀⠀⠀⠀⠀
⠀⣿⣿⡄⠀⠀⠀⠀⠀⠈⡇⢀⠠⠀⠀⠀⠁⠀⠀⡀⠀⠠⠟⠛⠀⠀⠀⠀⠀⠀
⠀⠸⣿⣷⡀⠀⠀⠀⠀⠀⠔⠁⠀⠀⠀⢀⢀⡀⠀⠈⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣴⣿⠀⠔⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠻⠿⠇⠒⠈⡄⠀⠀⠀⠀⠀⠀⠈⡉⠁⠀⠀⠀⠁⠀⠀⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡠⠴⠄⠀⢀⠔⠀⠀⠀⠄⠌⠀⠀⡁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢁⣀⡀⠀⡀⠙⠄⠀⢀⠀⣠⣾⠄⣤⠊⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⡑⠁⠂⠀⣈⣥⣾⡿⢿⠀⠀⢄⠀⢀⣠⣤⣤⣴⣦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠈⠀⠋⠿⠀⠀⠀⠄⠀⠌⣴⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠃⠀⠀⠀⠀⠀⠉⠀⠏⠀⠀⠈⠉⠙⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠈⠂⠄⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠄⢀⣀⡰⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
      """)
def draw_raichu():
    print("""
⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛⬛⬛🟨🟨⬜⬜⬜⬜⬜⬛🟨⬛⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛🟨🟨🟨⬛⬜⬜⬜⬜⬛🟨⬛⬜
⬜⬜⬛🟧🟧🟧🟧🟧⬛⬛⬛🟨🟨⬛⬛⬛⬜⬜⬜⬜⬛🟨⬛⬜
⬜⬛🟧🟧🟧🟧🟧🟧🟧⬛⬛🟨⬛⬜⬜⬛⬜⬜⬜⬜⬛🟨🟨⬛
⬛⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬛⬜⬜⬜⬜⬜⬛🟨🟨⬛
⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬜⬜⬜⬜⬛⬛⬛🟨🟨🟨⬛
⬛🟧🟧🟧🟧⬜⬛🟧🟧🟧🟧🟧⬛⬛⬜⬜⬛⬛🟨🟨🟨⬛⬛⬛
⬜⬛🟧🟧🟧⬛⬛🟨🟨🟧🟧🟧🟧⬛⬜⬜⬛⬛⬛🟨🟨⬛⬜⬜
⬜⬜⬛🟥🟧🟧🟧🟨🟨🟧🟧🟧🟧⬛⬛⬜⬛⬜⬜⬛🟨⬛⬜⬜
⬜⬛⬛🟥🟥🟥🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜⬛⬛⬜⬛⬜⬜⬜
⬜⬜⬛⬛⬜⬜🟧🟧🟧🟧🟧🟧⬛🟥⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜🟧⬛🟧🟥⬛🟥⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬛⬛🟥🟥⬛⬜⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬜⬜🟥🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛🟥⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛🟥🟥⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
      """)
def draw_pikachu():
    print("""
⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁
⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀
⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴
⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿
⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿
⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿
⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿
⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿
⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹
      """)

#used in the main function to level up the pokemon
def train():
    global pokemon_level
    print("You have chosen to train " + pokemon_name + " today!")
    pokemon_level = pokemon_level + 1
    print("Training went well!")
    evolution()

#used in the main function to user the pokemon in gym battles
def gym_battle():
    global pokemon_level
    global won_battles
    global lost_battles
    print("A gym battle! " + pokemon_name + " looks excited!")
    if pokemon_level < 5:
        outcome = random.randint(1,2)
        if outcome == 1:
            print("You won the Gym Battle! " + pokemon_name + " has gotten stronger!")
            pokemon_level = pokemon_level + 2
            won_battles = won_battles + 1
            evolution()
        if outcome == 2:
            print("You lost... " + pokemon_name + " has not gotten stronger. Maybe if you level up, winning will be easier.")
            lost_battles = lost_battles + 1
    if pokemon_level > 4 and pokemon_level < 9:
        outcome = random.randint(1,10)
        if outcome < 8:
            print("You won the Gym Battle! " + pokemon_name + " has gotten stronger!")
            pokemon_level = pokemon_level + 2
            won_battles = won_battles + 1
            evolution()
        else:
            print("You lost... " + pokemon_name + " has not gotten stronger. Maybe if you level up, winning will be easier.")
            lost_battles = lost_battles + 1
    if pokemon_level > 8:
        outcome = random.randint(1,10)
        if outcome < 10:
            print("You won the Gym Battle! " + pokemon_name + " has gotten stronger!")
            pokemon_level = pokemon_level + 2
            won_battles = won_battles + 1
            evolution()
        else:
            print("You lost... " + pokemon_name + " has not gotten stronger. Maybe if you level up, winning will be easier.")
            lost_battles = lost_battles + 1

#used in the main function to display pokemon details
def display_info():
    global pokemon_level
    global lost_battles
    global won_battles
    print("You have a " + pokemon_name + ". They are level " + str(pokemon_level))
    print("Wins: " + str(won_battles))
    print("Losses: " + str(lost_battles))
    if pokemon_name == "Pichu":
        draw_pichu()
    if pokemon_name == "Pikachu":
        draw_pikachu()
    if pokemon_name == "Raichu":
        draw_raichu()

#used in various functions where pokemon can level up to determine whether it can evolve or not
def evolution():
    global pokemon_level
    global pokemon_name
    if pokemon_level == 4:
        print("Your " + pokemon_name + " is evolving!")
        pokemon_name = "Pikachu"
        print("Now, they're a " + pokemon_name + ".")
        draw_pikachu()
    elif pokemon_level == 8:
        print("Your " + pokemon_name + " is evolving!")
        pokemon_name = "Raichu"
        print("Now, they're a " + pokemon_name + ".")
        draw_raichu()

#main game
def pokemon_evolution():
    print("Welcome to Pokemon Evolution! Train your pokemon, fight battles, and watch your companion evolve!")
    global repreat
    while repreat == True:
        print("""
    Select an activity:
    1. Train
    2. Gym Battle
    3. Rest / Display Pokemon Info
    4. Exit
        """)
        selection = int(input("What will you do today?"))
        if selection == 1:
            train()
        elif selection == 2:
            gym_battle()
        elif selection == 3:
            display_info()
        elif selection == 4:
            print("Bye Bye!")
            repreat = False
        elif selection > 4 or selection < 1:
            print("Whoops! That's not an option!")


#Main
pokemon_evolution()
