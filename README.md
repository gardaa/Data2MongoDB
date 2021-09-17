# Getting started

Firstly, you have to add environment variables to the `.env` file. There is an `.env.example` file included in the repository as an example showing how it is done. This is done to hide sensitive information. You can get this information (the connection string) by creating a user in MongoDB Atlas and follow the steps regarding "how to connect to MongoDB Atlas with Python". 

# How it's built

This is a Python script made for the case of sending telemetry data to a MongoDB Atlas account with the use of MQTT protocol and therefore a MQTT broker. The script is designed to continue sending data in an infinite loop, unless told otherwise (exited). The script connects to the MQTT broker (by subscribing to the broker's specified topic) and the MongoDB account, and defines to insert every incoming payload to MongoDB as JSON data.

# How to RUN

Enter `python3 transfer.py` in the terminal to run the script. The MongoDB will be updated automatically depending on how long you have decided the intervals to be.
