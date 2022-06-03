#import RPi.GPIO as GPIO
import time
from flask import Flask, render_template,request
app=Flask(__name__)
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(2,GPIO.OUT)


@app.route('/')
def home():
    
    #GPIO.output(2,GPIO.HIGH)
    return render_template('prueba.html')
    #return '<a href="/led1" class="button"> led1</a>'

@app.route('/led1')
def led1():
    #time.sleep(1)
    #GPIO.output(2,GPIO.LOW)
    return render_template('led.html')
    #return '<a href="/" class="button"> volver</a>'

if __name__ == '__main__':
    app.run(host="0.0.0.0" ,debug=True)

