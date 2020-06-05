from item import Item
from termcolor import colored
from textwrap import wrap


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = dict()
        self.items = list()

    def add_exit(self, direction, room):
        self.exits.setdefault(direction, room)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def __str__(self):
        exits = list(self.exits.keys())

        if len(exits) > 1:
            exits = f"There are exits {', '.join(exits[:-1]) + ' and ' + exits[-1]}."
        else:
            exits = f"You see a single exit {exits[0]}."

        descriptions = [self.description, ' '.join(map(lambda i: i.room_desc, self.items))]

        return '\n'.join((
            colored(self.name, 'yellow'),
            colored('\n'.join(wrap(' '.join(descriptions), width=100)), 'magenta'),
            exits
        ))


rooms = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons."),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. In the corner, however, you see a small crack in the wall that beckons your attention."""),
    'smallcrack': Room("Inside the Treasure Chamber", """A hidden chamber within a chamer!""")
}

# room connections
rooms['outside'].add_exit('north', rooms['foyer'])
rooms['foyer'].add_exit('south', rooms['outside'])
rooms['foyer'].add_exit('north', rooms['overlook'])
rooms['foyer'].add_exit('east', rooms['narrow'])
rooms['overlook'].add_exit('south', rooms['foyer'])
rooms['narrow'].add_exit('west', rooms['foyer'])
rooms['narrow'].add_exit('north', rooms['treasure'])
rooms['treasure'].add_exit('south', rooms['narrow'])
rooms['treasure'].add_exit('in', rooms['smallcrack'])
rooms['smallcrack'].add_exit('out', rooms['treasure'])

# room items
rooms['treasure'].add_item(Item(
    name='foliage',
    short_desc='some foliage',
    room_desc='Some beautifully carved foliage adorns the walls here.',
    examine_desc='As you take a closer look, you can make out a faint glimmer of gold within the foliage.'
))

rooms['smallcrack'].add_item(Item(
    name='key',
    short_desc='a silver key',
    room_desc='A silver key lies abandoned in the corner here.',
    examine_desc='This key looks like it would fit into a lock...'
))
