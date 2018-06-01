import curses
import os
import sys

import controlflow
from frontend import Window

class App(object):

    def __init__(self):
        self.window = curses.wrapper(lambda stdscr: Window(stdscr))
        self.signals = controlflow.Signals(self)
        self.run()

    def run(self):
        # file name required
        if len(sys.argv) < 2:
            self.signals.exit.crash('No file specified')

        # set up colors
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # show splash screen
        self.__splash(self.window._textbox, *(self.window._textbox.getmaxyx()))
        self.window._textbox.getkey()
        self.window._textbox.clear()

        # load the contents of the file
        contents = self.__readfile(sys.argv[1])
        line_marign = len(str(len(contents))) + 2
        for index, line in enumerate(contents):
            self.window._textbox.addstr(index, 1, str(index+1))
            self.window._textbox.addstr(index, line_marign, line)

        # show screen and require user input
        self.window._textbox.refresh()
        self.window._textbox.getkey()

    def __readfile(self, path=''):
        """ read the contents of a file as a list of lines """
        if os.path.isfile(path):
            return open(path).read().splitlines()
        else:
            return list()

    def __splash(self, screen, height, width):
        offset_y = int((height-20)/2)
        offset_x = int((width-60)/2)
        with open('flag') as fp:
            for y, line in enumerate(fp):
                for x, char in enumerate(line):
                    if char == '\n': screen.addstr(y + offset_y, x + offset_x, '\n')
                    elif char == '@': screen.addstr(y + offset_y, x + offset_x, ' ', curses.color_pair(1))
                    elif char == '%': screen.addstr(y + offset_y, x + offset_x, '#', curses.color_pair(2))
                    elif char == ' ': screen.addstr(y + offset_y, x + offset_x, '%', curses.color_pair(3))

if __name__ == "__main__":
    # require python3
    if (sys.version_info > (3, 0)):
        App()
    else:
        # please get python3 and let python2 rest in peace
        sys.exit((
            "I'd just like to interject for a moment. What you're referring to as Python2, is\n"
            "in fact, Python3, or as I've recently taken to calling it, Python3 plus Python2.\n"
            "Python2 is no longer a python version unto itself, but rather another free component\n"
            "of a fully functioning Python3 system made useful by the Python3 corelibs, shell\n"
            "utilities and vital system components comprising a full version as defined by POSIX.\n\n"
            "This application is specifically made to be incompatible with python2."
        ))
