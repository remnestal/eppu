import curses

class Window(object):
    """ Class for managing the terminal window
        screens:
            __stdscr    - main terminal screen, private access
            _textbox    - sub-screen for the text display
            _cmdline    - sub-screen for the command line interface
    """

    def __init__(self, stdscr):
        self.__init_stdscr(stdscr)
        self.__init_textbox()
        self.__init_cmdline()

    def __init_stdscr(self, stdscr):
        """ initializes the main screen """
        self.__stdscr = stdscr
        self.__stdscr.clear()
        self.height, self.width = self.__stdscr.getmaxyx()

    def __init_textbox(self):
        """ initializes the text-box screen """
        assert(self.__stdscr)
        self._textbox = self.__stdscr.subwin(self.height - 1, self.width, 0, 0)
        self._textbox.border()
        self._textbox.addstr('textbox')

    def __init_cmdline(self):
        """ initializes the command-line screen """
        assert(self.__stdscr)
        self._cmdline = self.__stdscr.subwin(1, self.width, self.height - 1, 0)
        self._cmdline.addstr('cmdline')
