import curses

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)


while True:
    event = screen.getch()
    if event == ord("q"):
        break
    elif event == curses.KEY_UP:
        screen.addstr("The User Pressed UP\n")
    elif event == curses.KEY_DOWN:
        screen.addstr("The User Pressed DOWN\n")
    elif event == curses.KEY_LEFT:
        screen.addstr("The User Pressed LEFT\n")
    elif event == curses.KEY_RIGHT:
        screen.addstr("The User Pressed RIGHT\n")
    elif event == ord("u"):
        screen.addstr("The User Pressed U\n")

curses.endwin()
