import RPi.GPIO as IO
import time
import pyttsx3
engine = pyttsx3.init()
IO.setwarnings(False)          # do not show any warnings

IO.setmode (IO.BCM)            # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)

TRIG = 16
ECHO = 18

IO.setup(TRIG,IO.OUT)
IO.setup(ECHO,IO.IN)


IO.output(TRIG, False)



def distance():
       IO.output(TRIG, True)
       time.sleep(0.00001)
       IO.output(TRIG, False)

       while IO.input(ECHO)==0:
          pulse_start = time.time()

       while IO.input(ECHO)==1:
          pulse_end = time.time()

       pulse_duration = pulse_end - pulse_start

       distance = pulse_duration * 17150

       distance = round(distance+1.15, 2)
  
       print ("distance:",distance,"cm")
       time.sleep(2)

while True:
            dist=distance()
            if(dist<50):
                engine.say('Object detected on the front')
                engine.runAndWait()
                engine.say("At the distance of")
                engine.runAndWait()
                engine.say(dist)
                engine.runAndWait()
                engine.say("Centimeters")
                engine.runAndWait()
GPIO.cleanup()
