class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = list()

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            return True

        print('What do you hope to find that way?')

    def get(self, item):
        if len(self.current_room.items) == 0:
            print(f'You see no "{item}" here.')
            return

        for room_item in self.current_room.items:
            if room_item.name == item:
                self.add_item(room_item)
                print(f'You pick up {room_item.short_desc}.')
                self.current_room.remove_item(room_item)
                return

    def drop(self, item):
        if len(self.inventory) == 0:
            print(f'You are not carrying anything.')
            return

        for inv_item in self.inventory:
            if inv_item.name == item:
                self.current_room.add_item(inv_item)
                print(f'You drop {inv_item.short_desc}.')
                self.remove_item(inv_item)
                return

    def list_inventory(self):
        if len(self.inventory) == 0:
            print('You are not carrying anything.')
            return

        short_items = map(lambda i: i.short_desc, self.inventory)

        print(f'You hold following items: {", ".join(short_items)}.', )
