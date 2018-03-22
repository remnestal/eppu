import curses

class Keyboard(object):
    """ Simple keyboard handler """
    __key_literals = ['q', 'w', 'e', 'f', 'j', 'i', 'o', 'p']
    __panic_button = ' '

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def next_ascii():
        pass

    def __next_sequence(self):
        """ Get the next key sequence """
        key_sequence = [False] * len(literals)
        while True:
            try:
                key = stdscr.getkey()
                if key == __panic_button:
                    return key_sequence
                else:
                    index = literals.index(key)
                    key_sequence[index] = not key_sequence[index];
            except:
                pass
