import curses

class Keyboard(object):
    """ Simple keyboard handler """
    __key_literals = ['q', 'w', 'e', 'f', 'j', 'i', 'o', 'p']
    __panic_button = ' '

    def __init__(self, stdscr):
        self.stdscr = stdscr

    def next_ascii():
        pass

    def _next_sequence(self):
        """ Get the next key sequence entered by the user """
        key_sequence = [False] * len(self.__key_literals)
        while True:
            try:
                key = self.stdscr.getkey()
                if key == self.__panic_button:
                    # submit sequence when the panic button is pressed
                    return key_sequence
                else:
                    index = self.__key_literals.index(key)
                    key_sequence[index] = not key_sequence[index];
            except:
                pass
