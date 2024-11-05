import json

def main():
    game = getDefaultGame()
    keepGoing = True

    while keepGoing:
        userChoice = getMenuChoice()

        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            print("load default game")
            game = getDefaultGame()
        elif userChoice == "2":
            game = loadGame()
        elif userChoice == "3":
            saveGame(game)
        elif userChoice == "4":
            editNode(game)
        elif userChoice == "5":
            playGame(game)
        else:
            print("that is not an option.")
            
def getMenuChoice():
    print("\n        0) exit")
    print("        1) load default game")
    print("        2) load a game file")
    print("        3) enter 3 to save")
    print("        4) edit or add a node")
    print("        5) play the current game")
    return input("what will you do? ")

def playGame(game_data):
    current_node = 'start'
    while True:
        playNode(game_data, current_node)
        if current_node not in game_data:
            print("that node cannot be done")
            return
        
        description, menu_a, node_a, menu_b, node_b = game_data[current_node]
        choice = input("your choice: ")
        
        if choice == "1":
            current_node = node_a
        elif choice == "2":
            current_node = node_b
        else:
            print("invalid option.")
            return

def playNode(game_data, current_node):
    if current_node in game_data:
        description, menu_a, node_a, menu_b, node_b = game_data[current_node]
        print(description)
        print(f"1) {menu_a}")
        print(f"2) {menu_b}")

def getDefaultGame():
    return {
        "start": [
            "Do you want to win or lose?",
            "I want to win",
            "win",
            "I'd rather lose",
            "lose"
        ],
        "win": [
            "You win!",
            "Start over",
            "start",
            "Quit",
            "quit"
        ],
        "lose": [
            "You lose!",
            "Start over",
            "start",
            "Quit",
            "quit"
        ]
    }

def editNode(game_data):
    print("current nodes: ")
    for node in game_data.keys():
        print(f" {node}")
        
    node_name = input("choose node to edit or enter new node name: ")
    if node_name not in game_data:
        game_data[node_name] = ["", "", "", "", ""]

    game_data[node_name][0] = editField("Description", game_data[node_name][0])
    game_data[node_name][1] = editField("Menu A", game_data[node_name][1])
    game_data[node_name][2] = editField("Node A", game_data[node_name][2])
    game_data[node_name][3] = editField("Menu B", game_data[node_name][3])
    game_data[node_name][4] = editField("Node B", game_data[node_name][4])

    print(f"\nUpdated node {node_name}:")
    print(f"{'Description:':15}{game_data[node_name][0]}")
    print(f"{'Menu A:':15}{game_data[node_name][1]}")
    print(f"{'Node A:':15}{game_data[node_name][2]}")
    print(f"{'Menu B:':15}{game_data[node_name][3]}")
    print(f"{'Node B:':15}{game_data[node_name][4]}\n")

def editField(field_name, current_value):
    new_value = input(f"{field_name} ({current_value}): ")
    return new_value if new_value != "" else current_value

def saveGame(game_data):
    filename = "current_game.json"
    with open(filename, 'w') as file:
        json.dump(game_data, file)
    print(f"game save to {filename}.")
    
def loadGame():
    filename = input("enter filename to load: ")
    file = open(filename, 'r')
    game_data = json.load(file)
    file.close()
    return game_data
    
main()