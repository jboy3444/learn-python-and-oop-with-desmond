
"""
Add comments here...
pokemon level
pokemon stats
pokemon nature
gender
type
type advantage
stat growth
battles
battle themes
music: battles, area, other
trainer
trainer customization
battle rules
held item effects
move animation
pokemon animation
game animation
habitat design
experience gain system
experience gain manipulation
pokemon registration system
wild pokemon generator
wifi connection
multiplayer capabilitites
move effect calculation
move effect type advantage
status change
evolotion state change
special efects]
catch ratio critacal hit ratio








List the attirbutes of a pokemon

# Inheritance
is_a():
    # Define what a pokemon is...

# Abstraction
# has_a():
    # Things a pokemon has...

"""


class Pokemon():
    level = 1

    def __init__(self, name, type, move_list):
        self.name = name
        self.type = type
        self.move_list = move_list

    def pokedex_entry(self):
        print(
            f"This is a level {this.level}, {this.name}, it is a {this.type} type")

    def get_move_list(self):
        print(move_list)

    def set_move_list(self, move):
        if (len(move_list) == 4):
            print(
                "{this.name}, cannot learn more than four moves, do you wish to delete one?")
        this.move_list.append(move)


charmander = Pokemon("Charmander", "Fire", ["scratch"])
charmander.pokedex_entry()
