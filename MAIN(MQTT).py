print("MQTT with Adafruit IO")
print("Sensors and Actuators")

import time
import sys
from Adafruit_IO import MQTTClient
import requests
import sensor
from AIoT_Action_Feelings_Change import Detect_Feelings
import Security

AIO_USERNAME = "PhamBaoLongGroupAI"
AIO_KEY = "aio_GLpQ71e9BHVW7RTMgs1Va1Cs5SLa"

global_equation = "x1/x2"
Security.Sign_up()
Security.Log_in()
print("Welcome user, please enter your option to use the device")
print("")
print("Manual mode or Auto mode")
Request_of_user = str(input("Enter your request: ", ))


#Implement the requests from user
def init_global_equation():
    global global_equation
    headers = {}
    aio_url = "https://io.adafruit.com/api/v2/PhamBaoLongGroupAI/feeds/equation"
    x = requests.get(url=aio_url, headers=headers, verify=False)
    data = x.json()
    global_equation = data["last_value"]
    print("The latest equation: ", global_equation)


def modify_value(x1, x2):  # Eval_function
    result = eval(global_equation)
    print(result)
    return result


def connected(client):
    print("Server connected ...")
    client.subscribe("button-for-light")
    client.subscribe("button-for-fan")
    client.subscribe("equation")


# subscribe
def subscribe(client, userdata, mid, granted_qos):
    print("Subscribed!!!")


def disconnected(client):
    print("Disconnected from the server!!!")
    sys.exit(1)


# Control light and fan
def message(client, feed_id, payload):
    print("Received: " + payload)
    if feed_id == 'button-for-fan':
        if payload == "1":
            print("Turn on the fan...")
            sensor.sendCommand("2")
            return

        elif payload == "0":
            print('Turn off the fan...')
            sensor.sendCommand("3")
            return
    if feed_id == 'button-for-light':
        if payload == "1":
            print("Turn on the light...")
            sensor.sendCommand("4")
            return

        elif payload == "0":
            print('Turn off the light...')
            sensor.sendCommand("5")
            return
    if (feed_id == "equation"):
        global_equation = payload
        print(global_equation)

    print("Testing commands")


client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe

client.connect()
client.loop_background()
init_global_equation()
# Implement Request of user
if Request_of_user == "Manual mode":
    while True:
        pass
elif Request_of_user == "Auto mode":

    #Request for Ideal temp and humid
    print("Please enter your ideal temperature and humidity")
    ideal_temp = float(input("Enter your ideal temperature: "))
    ideal_humid = float(input("Enter your ideal humidity:  %"))

    # Request for temp and Humid
    while True:
        # Request for temperature
        sensor.requestData("0")
        if sensor.processData.splitData[1] == "T":
            Temp = float(sensor.processData.splitData[2])
            client.publish("Temp", sensor.processData.splitData[2])
        time.sleep(2)

        # Request for Humidity
        sensor.requestData("1")
        if sensor.processData.splitData[1] == "H":
            Humid = (float(sensor.processData.splitData[2]))
            client.publish("Humid", sensor.processData.splitData[2])
        time.sleep(2)

        # Request for Feelings:
        Detect_Feelings.image_detector()
        time.sleep(3)
        client.publish("Feeling", str(Detect_Feelings.image_detector.Class_name1))

        # Action when the Feelings, temp, and humid change
        if Temp > ideal_temp and Humid > ideal_humid:
            if Detect_Feelings.image_detector.Class_name1 == 'Irritate\n' or Detect_Feelings.image_detector.Class_name1 == 'Sweat\n':
                sensor.sendCommand("5")  # Turn off light
                sensor.sendCommand("2")  # Turn on fan
        elif Temp < ideal_temp and Humid < ideal_humid:
            if Detect_Feelings.image_detector.Class_name1 == 'Shiver\n' or Detect_Feelings.image_detector.Class_name1 == 'Sneeze\n':
                sensor.sendCommand("3")  # Turn off fan
                sensor.sendCommand("4")  # Turn on light
        pass
