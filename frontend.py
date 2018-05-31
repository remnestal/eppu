import curses

class Window(object):
    """ Class for managing the terminal window
        screens:
            __stdscr    - main terminal screen, private access
            _textbox    - sub-screen for the text display
            _cmdline    - sub-screen for the command line interface
    """

    _cmdline_height = 1

    def __init__(self, stdscr):
        self._init_stdscr(stdscr)
        self._init_textbox()
        self._init_cmdline()

    def _init_stdscr(self, stdscr):
        """ initializes the main screen """
        self.__stdscr = stdscr
        self.__stdscr.clear()
        self.height, self.width = self.__stdscr.getmaxyx()

    def _init_textbox(self):
        """ initializes the text-box screen """
        assert(self.__stdscr)
        self._textbox = self.__stdscr.subwin(self.height - self._cmdline_height, self.width, 0, 0)
        self._textbox.border()
        self._textbox.addstr('textbox')

    def _init_cmdline(self):
        """ initializes the command-line screen """
        assert(self.__stdscr)
        self._cmdline = self.__stdscr.subwin(self._cmdline_height, self.width, self.height - 1, 0)
        self._cmdline.addstr('cmdline')
