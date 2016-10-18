import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
import time
import curses
import math

command_id = 0

REVERSE = {"m1" : "1", "m2" : "2", "m_up" : "0", "time" : "80", "command_id" : "5"}
FORWARD = {"m1" : "2", "m2" : "1", "m_up" : "0", "time" : "80", "command_id" : "5"}
UP = {"m1" : "0", "m2" : "0", "m_up" : "15", "time" : "40", "command_id" : "5"}
LEFT = {"m1" : "0", "m2" : "1", "m_up" : "5", "time" : "15", "command_id" : "5"}
RIGHT = {"m1" : "2", "m2" : "0", "m_up" : "5", "time" : "15", "command_id" : "5"}
latest_values = []

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("team4_read")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    payload = json.loads(msg.payload)
    #if BEACON2 == payload["baddr"]:
    #print "beacon: {4}, rssi: {0}, x: {1}, y: {2}, z: {3}".format(payload["rssi"], payload["x"], payload["y"], payload["z"], payload["baddr"])
    #if "E1:92:13:FC:20:7D" == payload["baddr"]:
    #print average_of_latest_values(payload["baddr"], int(payload["rssi"]))

    try:
        if "57:D7:D5:72:8D:F1" in payload["baddr"]:
            print "near: {0} meters".format(calculate_distance(average_of_latest_values(payload["baddr"], int(payload["rssi"]))))
        if "6F" in payload["baddr"]:
            print "far away: {0} meters".format(calculate_distance(average_of_latest_values(payload["baddr"], int(payload["rssi"]))))
    except Exception as e:
        print (e)
    command_id = payload["command_id"]



def average_of_latest_values(baddr, rssi):
    #print latest_values
    if not latest_values:
        latest_values.append({"baddr" : baddr, "rssi_values" : [int(rssi)]})
        return int(rssi)
    for index, item in enumerate(latest_values):

        if item["baddr"] == baddr:
            latest_values.remove(item)
            if len(item["rssi_values"]) >= 5:
                item["rssi_values"].pop(0)
            item["rssi_values"].append(rssi)
            latest_values.insert(index, item)
            return int((sum(item["rssi_values"]) / float(len(item["rssi_values"]))))
    latest_values.append({"baddr": baddr, "rssi_values": [int(rssi)]})
    return int(rssi)


def calculate_distance(rssi):
    txPower = -59 # hard coded power value.Usually ranges between - 59 to - 65

    if (rssi == 0):
        return -1.0

    ratio = rssi * 1.0 / txPower

    if (ratio < 1.0):
        return pow(ratio, 10);
    else:
        distance = (0.89976) * pow(ratio, 7.7095) + 0.111
        return distance

def on_log(mqttc, userdata, level, string):
    pass
    #print(string)


def move(command_dict):
    message_id = None
    command_dict = _update_command_id(command_dict)
    while not message_id and command_dict["command_id"] != command_id:
        res, message_id = client.publish("team4_write", json.dumps(command_dict))
        print "RES: {0}\n".format(res)
        print "MID: {0}\n".format(message_id)


def on_publish(client, userdata, mid):
    print "on publish;, userdata: {0}, mid: {1}\n".format(userdata, mid)


def _update_command_id(command_dict):
    #TODO: method needed to get latest command_id dynamically from the queue:
    command_dict["command_id"] = str(int(command_id) + 1)
    return command_dict

if __name__ == '__main__':
    client = mqtt.Client(protocol=mqtt.MQTTv31)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    #debug prints
    client.on_log = on_log

    client.connect("54.93.150.126", 1883, 60)

    client.loop_start()

    while True:
        event = screen.getch()
        if event == ord("q"):
            client.disconnect()
            break
        elif event == curses.KEY_UP:
            print "The User Pressed UP\n"
            move(FORWARD)
        elif event == curses.KEY_DOWN:
            print "The User Pressed DOWN\n"
            move(REVERSE)
        elif event == curses.KEY_LEFT:
            print "The User Pressed LEFT\n"
            move(LEFT)
        elif event == curses.KEY_RIGHT:
            print "The User Pressed RIGHT\n"
            move(RIGHT)
        elif event == ord("u"):
            print "The User Pressed U\n"
            move(UP)

    curses.endwin()
