import curses
import sys
import os

def main(stdscr):

    # file name required
    if len(sys.argv) < 2:
        sys.exit('No file specified.')

    # Clear screen at startup
    stdscr.clear()

    # set up colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    #  configure runtime vars
    scr_height, scr_width = stdscr.getmaxyx()

    # show splash screen
    __splash(stdscr, scr_height, scr_width)
    stdscr.getkey()
    stdscr.clear()

    # load the contents of the file
    contents = __readfile(sys.argv[1])
    line_marign = len(str(len(contents))) + 2
    for index, line in enumerate(contents):
        stdscr.addstr(index, 1, str(index+1))
        stdscr.addstr(index, line_marign, line)

    # show screen and require user input
    stdscr.refresh()
    stdscr.getkey()

def __readfile(path=''):
    """ read the contents of a file as a list of lines """
    if os.path.isfile(path):
        return open(path).read().splitlines()
    else:
        return list()

def __splash(stdscr, height, width):
    offset_y = int((height-20)/2)
    offset_x = int((width-60)/2)
    with open('flag') as fp:
        for y, line in enumerate(fp):
            for x, char in enumerate(line):
                if char == '\n': stdscr.addstr(y + offset_y, x + offset_x, '\n')
                elif char == '@': stdscr.addstr(y + offset_y, x + offset_x, ' ', curses.color_pair(1))
                elif char == '%': stdscr.addstr(y + offset_y, x + offset_x, '#', curses.color_pair(2))
                elif char == ' ': stdscr.addstr(y + offset_y, x + offset_x, '%', curses.color_pair(3))

if __name__ == "__main__":
    curses.wrapper(main)
