from pymongo import MongoClient
import time
from random import randrange
from os import getenv

client = MongoClient('mongodb://bierbot:bierbot@localhost:27017/')

# connect with bierbot collection
db = client.bierbot

mockdoc = {
    "knoten": "thron1",
    "temperature": "20",
    "timestamp": "15:00:00",
    "humidity": "50",
    "weight": "400",
    "gps": "52.5,13.5",
    "battery": "100"
}

client.bierbot.measures.insert_one(mockdoc)

while True:
    mockdock = {
        "knoten": "thron1",
        "temperature": randrange(20, 30),
        "timestamp": time.strftime("%H:%M:%S"),
        "humidity": randrange(50, 60),
        "weight": randrange(400, 500),
        "gps": "52.5,13.5",
        "battery": randrange(0, 100)
    }
    client.bierbot.measures.insert_one(mockdock)
    time.sleep(10)
