import time
from w1thermsensor import W1ThermSensor, Unit
from pymongo import MongoClient
from dotenv import load_dotenv
from random import randrange
from os import getenv
import RPi.GPIO as GPIO
import Adafruit_DHT

green_led = 20
red_led = 16
yellow_led = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(yellow_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)


def set_light(temperature):
    if temperature < THRESHOLD_TEMP_OK:
        light_on(green_led)
        light_off(yellow_led)
        light_off(red_led)
    elif temperature < THRESHOLD_TEMP_BAD:
        light_off(green_led)
        light_on(yellow_led)
        light_off(red_led)
    else:
        light_off(green_led)
        light_on(yellow_led)
        light_on(red_led)


def light_on(pin):
    GPIO.output(pin, GPIO.HIGH)


def light_off(pin):
    GPIO.output(pin, GPIO.LOW)


load_dotenv()

MONGO_URI = getenv('MONGODB_URI')
print(MONGO_URI)
client = MongoClient(MONGO_URI)

# connect with bierbot collection
db = client.bierbot
w1_sensor = W1ThermSensor()

while True:
    humidity, temp = Adafruit_DHT.read(11,21)
    measurement = {
        "knoten": "thron1",
        "temperature1": temp,
        "temperature2": w1_sensor.get_temperature(),
        "timestamp": time.strftime("%H:%M:%S"),
        "humidity": humidity,
        "weight": randrange(400, 500),
        "gps": "52.5,13.5",
        "battery": randrange(0, 100)
    }
    client.bierbot.measures.insert_one(measurement)
    set_light(temp)
    time.sleep(10)
