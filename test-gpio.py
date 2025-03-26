import RPi.GPIO as GPIO
import time

# Configurer le mode de numérotation des GPIO
GPIO.setmode(GPIO.BCM)

# Configurer le GPIO 17 comme sortie (utilise un autre GPIO si nécessaire)
GPIO.setup(17, GPIO.OUT)

# Allumer la LED pendant 1 seconde
GPIO.output(17, GPIO.HIGH)
time.sleep(1)

# Éteindre la LED
GPIO.output(17, GPIO.LOW)

# Nettoyer les configurations GPIO
GPIO.cleanup()
