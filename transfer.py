from dotenv.main import load_dotenv
import paho.mqtt.client as mqtt
import time
from pymongo import MongoClient
import json
from dotenv import dotenv_values
import os

# Load environment variables from .env file
load_dotenv()

# Callback method for printing the log dialog 
def on_log(client, userdata, level, buf):
    print('Log: ' + buf)

# Callback method for printing connection status
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print('Connected OK')
    else:
        print('Bad connection, returned code: ' + rc)

# Callback method defining what to do with received messages from broker, in this case printing the received message and sending it to MongoDB
def on_message(client, userdata, msg):
    m_decode = str(msg.payload.decode('utf-8'))
    msg = m_decode.strip('[]')
    jsonDict = json.loads(msg)
    collection.insert_one(jsonDict)
    print('Message received: ', jsonDict)

# Connect to the MongoDB using the connection string
connection = MongoClient(os.getenv('KEY'))

# Creating/switching to the database and collection
db = connection.KruserData
collection = db.GPS
    
# IP of computer where the broker is installed, either the internal or external IP
broker = os.getenv('IP')

# Create a client
client = mqtt.Client('boat1')

# Call the callback methods to give signal   
#client.on_connect=on_connect
#client.on_log=on_log
client.on_message=on_message

print('Connecting to broker: ' + broker)

# Connect the client to the broker
client.connect(broker)

# Make client subscribe to a specified topic
client.subscribe('devices/boats/boat1/gps')

print('Starting infinite loop -> press "CTRL + C" to exit')
# Create an infinite loop so the program receives data forever unless manually exited
client.loop_forever()

#client.disconnect()