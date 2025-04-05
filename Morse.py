import RPi.GPIO as GPIO
import time

# --------------------------
# Configuration GPIO
# --------------------------

LED_PIN = 26  # La LED pour le morse
SEGMENTS = {
    'a': 22,
    'b': 23,
    'c': 16,
    'd': 25,
    'e': 24,
    'f': 27,
    'g': 17
}

# --------------------------
# Lettres → segments à allumer
# --------------------------
LETTER_SEGMENTS = {
    'A': ['a', 'b', 'c', 'e', 'f', 'g'],
    'B': ['c', 'd', 'e', 'f', 'g'],
    'C': ['a', 'd', 'e', 'f'],
    'D': ['b', 'c', 'd', 'e', 'g'],
    'E': ['a', 'd', 'e', 'f', 'g'],
    'F': ['a', 'e', 'f', 'g'],
    # Ajoute plus de lettres au besoin
}

# --------------------------
# Table de conversion Morse
# --------------------------
MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '1': '.----',  '2': '..---',  '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....',
    '7': '--...',  '8': '---..',  '9': '----.',
    '0': '-----'
}

# --------------------------
# Setup GPIO
# --------------------------
def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    for pin in SEGMENTS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

# --------------------------
# Fonctions de contrôle
# --------------------------
def clear_display():
    for pin in SEGMENTS.values():
        GPIO.output(pin, GPIO.LOW)

def display_letter(letter):
    clear_display()
    upper = letter.upper()
    if upper in LETTER_SEGMENTS:
        for seg in LETTER_SEGMENTS[upper]:
            GPIO.output(SEGMENTS[seg], GPIO.HIGH)

def dot():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.2)

def dash():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.6)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.2)

def transmit_morse(message):
    for char in message:
        upper = char.upper()
        if upper == ' ':
            time.sleep(0.6)  # Pause entre les mots
            continue

        display_letter(upper)
        morse = MORSE_CODE.get(upper, '')
        print(f"{upper} : {morse}")
        
        for symbol in morse:
            if symbol == '.':
                dot()
            elif symbol == '-':
                dash()
        clear_display()
        time.sleep(0.6)  # Pause entre les lettres

# --------------------------
# Exécution
# --------------------------
if __name__ == '__main__':
    try:
        setup()
        message = input("Entrez un message à transmettre en morse : ")
        transmit_morse(message)

    except KeyboardInterrupt:
        print("\nInterruption par l'utilisateur.")

    finally:
        clear_display()
        GPIO.cleanup()
