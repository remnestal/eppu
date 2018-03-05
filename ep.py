import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # colors
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    height, width = stdscr.getmaxyx()
    flag(stdscr, height, width)

    stdscr.refresh()
    stdscr.getkey()

def flag(stdscr, height, width):
    offset_y = int((height-24)/2)
    offset_x = int((width-80)/2)
    with open('flag') as fp:
        for y, line in enumerate(fp):
            for x, char in enumerate(line):
                if char == '\n': stdscr.addstr(y + offset_y, x + offset_x, '\n')
                elif char == '@': stdscr.addstr(y + offset_y, x + offset_x, ' ', curses.color_pair(1))
                elif char == '%': stdscr.addstr(y + offset_y, x + offset_x, '#', curses.color_pair(2))
                elif char == ' ': stdscr.addstr(y + offset_y, x + offset_x, '%', curses.color_pair(3))

if __name__ == "__main__":
    curses.wrapper(main)
