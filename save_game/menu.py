from code import terminal, util
from classes import player
from save_game import save

menu_text = """

  _____  ______       _______ _    _ _  _____   
 |  __ \|  ____|   /\|__   __| |  | ( )/ ____|  
 | |  | | |__     /  \  | |  | |__| |/| (___    
 | |  | |  __|   / /\ \ | |  |  __  |  \___ \   
 | |__| | |____ / ____ \| |  | |  | |  ____) |  
 |_____/|______/_/  _ \_\_|_ |_|__|_|_|_____/ _ 
 |  __ \| |  | | \ | |/ ____|  ____/ __ \| \ | |
 | |  | | |  | |  \| | |  __| |__ | |  | |  \| |
 | |  | | |  | | . ` | | |_ |  __|| |  | | . ` |
 | |__| | |__| | |\  | |__| | |___| |__| | |\  |
 |_____/ \____/|_| \_|\_____|______\____/|_| \_|

    Created by The Avocadish Onions

"""
# ^^^ ????

options = """
 [1] Restore Save
 [2] Start New
 [3] Tutorial
 [4] Exit
"""

limited_options = """
 [1] Play
 [2] Tutorial
 [3] Exit
"""

def menu():
	"""Display The Menu"""
	terminal.clear()
	print(menu_text+options)

	choice = util.get_input("-> ", valid=['1', '2', '3', '4'])

	if choice == '1':
		game_data = save.get_game_data()

	elif choice == '2':
		game_data = False # start new

	elif choice == '3':
		return tutorial()

	elif choice == '4':
		exit()

	return game_data


def limited_menu():
    """Display the Limited Menu"""
    terminal.clear()
    print(menu_text+limited_options)

    choice = util.get_input("-> ", valid=['1', '2', '3'])

    if choice == '1':
        return
    elif choice == '2':
        return tutorial(bob="bill")
    elif choice == '3':
        exit()

    return game_data



def tutorial(bob="bob"):
    """Display Tutorial and call Menu Again"""

    with open('tutorial.txt', 'r') as file:
        parts = file.read().split('PART')

    for part in parts:
        terminal.clear()
        terminal.slow_print(part, 0.001)
        util.cont()

    if bob == 'bob':
        # as all things should be
        return menu()

    elif bob == 'bill':
        # herm...
        return limited_menu()