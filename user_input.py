import curses

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

while True:
   event = screen.getch()
   if event == ord("q"): break
   elif event == curses.KEY_UP:
      screen.clear()
      screen.addstr("The User Pressed UP")
   elif event == curses.KEY_DOWN:
      screen.clear()
      screen.addstr("The User Pressed DOWN")


curses.endwin()


