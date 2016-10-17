# mindtrek_rally

Basic commands with mosquitto client:

subscribe
mosquitto_sub -h 54.93.150.126 -t team4_read

move left
mosquitto_pub -h 54.93.150.126 -t team4_write -m '{"m1" : "2", "m2" : "0", "m_up" : "50", "time" : "30", "command_id" : "1"}'

move right
mosquitto_pub -h 54.93.150.126 -t team4_write -m '{"m1" : "0", "m2" : "1", "m_up" : "50", "time" : "30", "command_id" : "1"}'

forward
mosquitto_pub -h 54.93.150.126 -t team4_write -m '{"m1" : "1", "m2" : "2", "m_up" : "20", "time" : "200", "command_id" : "1"}'

Installing needed libraries

Curses library in Windows:
Download and install unofficial curses library: http://www.lfd.uci.edu/~gohlke/pythonlibs/#curses
Whl file can be installed with command 'pip install <filename>.whl'

