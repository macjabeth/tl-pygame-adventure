from room import Room, rooms
from player import Player
from command import Command

#
# Intro
#

print('-' * 80)
name = input('What is your name, adventurer? ')
print(f'\nWelcome to Pythonia, {name}. May the odds be ever in your favour...')
print('-' * 80)

#
# Main
#

player = Player(name, rooms['outside'])

print(player.current_room)

while True:
    command, *args = input('> ').split(' ')

    if command in ('q', 'quit'):
        break
    elif not Command.parse(command, player, *args):
        continue

    print(player.current_room)
