from flask import Flask, render_template, jsonify
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

# Set up GPIO pins for the relays
RELAY_1_PIN = 17
RELAY_2_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_1_PIN, GPIO.OUT)
GPIO.setup(RELAY_2_PIN, GPIO.OUT)

# Function to toggle relay state
def toggle_relay(pin, state):
    GPIO.output(pin, state)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle_relay/<int:relay>/<int:state>')
def toggle(relay, state):
    if relay == 1:
        toggle_relay(RELAY_1_PIN, state)
    elif relay == 2:
        toggle_relay(RELAY_2_PIN, state)
    return jsonify(success=True)

@app.route('/get_status')
def get_status():
    relay1_status = GPIO.input(RELAY_1_PIN)
    relay2_status = GPIO.input(RELAY_2_PIN)
    return jsonify(relay1=relay1_status, relay2=relay2_status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
