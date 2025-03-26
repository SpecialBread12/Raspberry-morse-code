import RPi.GPIO as GPIO
import time

# Configuration du mode des GPIO
GPIO.setmode(GPIO.BCM)

# GPIO utilisé pour la commande du transistor
GPIO_LED = 17

# Configurer le GPIO comme sortie
GPIO.setup(GPIO_LED, GPIO.OUT)

# Éteindre la LED (mettre la base du transistor à HIGH)
GPIO.output(GPIO_LED, GPIO.HIGH)
time.sleep(1)

# Allumer la LED (mettre la base du transistor à LOW)
GPIO.output(GPIO_LED, GPIO.LOW)
time.sleep(1)

# Nettoyer la configuration des GPIO
GPIO.cleanup()
