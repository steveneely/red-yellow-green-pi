from gpiozero import Button
from time import sleep
import requests
import json

API_ENDPOINT = "http://mockbin.org/bin/060682cb-a8c5-4ae8-a272-e06f17ce6a3c/view"

red_button = Button(2)
yellow_button = Button(3)
green_button = Button(14)

while True:
    if red_button.is_pressed:
        print("Red button is pressed")
    elif yellow_button.is_pressed:
        print("Yellow button is pressed")
    elif green_button.is_pressed:
        print("Green button is pressed")
    else:
        print("No buttons pressed")
    sleep(1)

def send_http_request(color):
    print("Sending " + color)
    data = json.dumps({'color':color}) 

    r = requests.post(url = API_ENDPOINT, json = data) 
    print("Status code returned: " + r.status_code)