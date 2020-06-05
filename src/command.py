from random import choice


class Command:
    list = dict()

    @classmethod
    def add(cls, pattern, fn):
        cls.list[pattern] = fn

    @classmethod
    def parse(cls, command, *args):
        for pattern, fn in cls.list.items():
            if ')' in pattern:
                start, end = pattern.split(')')
                if command in [start, start + end]:
                    return fn(*args)
            elif '|' in pattern:
                if command in pattern.split('|'):
                    return fn(*args)
            elif command == pattern:
                return fn(*args)

        print(choice(('What?', "I don't understand.", 'Nani?!', 'Try again.')))


# directional movements
Command.add('l)ook', lambda p: print(p.current_room))
Command.add('n)orth', lambda p: p.move('north'))
Command.add('s)outh', lambda p: p.move('south'))
Command.add('e)ast', lambda p: p.move('east'))
Command.add('w)est', lambda p: p.move('west'))
Command.add('i)n', lambda p: p.move('in'))
Command.add('o)ut', lambda p: p.move('out'))


def insert_punctuation(text):
    return text[-1] in [".", "!", "?"] and text or text + "."


# player actions
Command.add('g)et', lambda p, item: p.get(item))
Command.add('dr)op', lambda p, item: p.drop(item))
Command.add('inv)entory', lambda p: p.list_inventory())
Command.add('say', lambda p, msg: print(f'You say, "{insert_punctuation(msg).capitalize()}"'))
