import RPi.GPIO as GPIO
import time

# Configuration du mode des GPIO
GPIO.setmode(GPIO.BCM)

# GPIO utilisé pour la commande du transistor
GPIO_LED = 17
GPIO_CUT = 27

# Configurer le GPIO comme sortie
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_CUT, GPIO.OUT)
# Éteindre la LED (mettre la base du transistor à HIGH)
GPIO.output(GPIO_LED, GPIO.HIGH)
print('start')
time.sleep(1)

# Allumer la LED (mettre la base du transistor à LOW)
GPIO.output(GPIO_CUT, GPIO.HIGH)
print('off')
time.sleep(1)

GPIO.output(GPIO_LED, GPIO.LOW)
GPIO.output(GPIO_CUT, GPIO.LOW)
print('done')
time.sleep(1)

# Nettoyer la configuration des GPIO
GPIO.cleanup()
