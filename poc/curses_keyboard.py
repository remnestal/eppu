import curses

def main(stdscr):
    """ Proof of concept: keyboard-input via curses

    This implementation is based on the getKey() functionality of the curses
    package. This package is currently also heavily used in the rest of the app.

    Based on: https://stackoverflow.com/a/32386410/1434940
    """
    stdscr.nodelay(True)
    stdscr.clear()

    literals = ['q', 'w', 'e', 'f', 'j', 'i', 'o', 'p']
    keypress = [False] * len(literals)

    while True:
        try:
            # print which keys are pressed
            feedback = ['x' if k else '_' for k in keypress];
            stdscr.addstr(2, 1, feedback[0])
            stdscr.addstr(2, 3, feedback[1])
            stdscr.addstr(2, 5, feedback[2])
            stdscr.addstr(3, 7, feedback[3])
            stdscr.addstr(3, 13, feedback[4])
            stdscr.addstr(2, 15, feedback[5])
            stdscr.addstr(2, 17, feedback[6])
            stdscr.addstr(2, 19, feedback[7])

            stdscr.addstr(0, 0, 'Press x to panic')

            key = stdscr.getkey()
            if key == 'x': # panic key
                break
            if key == ' ': # commit to key sequence
                keypress = [False] * len(literals)
            else:
                index = literals.index(key)
                keypress[index] = not keypress[index];

            stdscr.clear()

        except:
            pass

curses.wrapper(main)
