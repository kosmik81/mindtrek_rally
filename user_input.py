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
        print "up"
        #screen.addstr("The User Pressed UP\n")
    elif event == curses.KEY_DOWN:
        print "d"
        #screen.addstr("The User Pressed DOWN\n")
    elif event == curses.KEY_LEFT:
        print "l"
        #screen.addstr("The User Pressed LEFT\n")
    elif event == curses.KEY_RIGHT:
        print "r"
        #screen.addstr("The User Pressed RIGHT\n")
    elif event == ord("u"):
        print "u"
        #screen.addstr("The User Pressed U\n")

curses.endwin()
