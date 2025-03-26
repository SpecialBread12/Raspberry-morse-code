import RPi.GPIO as GPIO
import time

# Configuration du GPIO
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Dictionnaire Morse
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.'
}

# Durées en secondes
DOT_DURATION = 0.2
DASH_DURATION = DOT_DURATION * 3
SPACE_DURATION = DOT_DURATION * 7
LETTER_GAP = DOT_DURATION * 3
SYMBOL_GAP = DOT_DURATION

def blink_led(duration):
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(SYMBOL_GAP)

def text_to_morse(text):
    for char in text.upper():
        if char == ' ':
            time.sleep(SPACE_DURATION)
        elif char in MORSE_CODE:
            for symbol in MORSE_CODE[char]:
                if symbol == '.':
                    blink_led(DOT_DURATION)
                elif symbol == '-':
                    blink_led(DASH_DURATION)
            time.sleep(LETTER_GAP)

try:
    text = input("Entrez le texte à transmettre en Morse : ")
    text_to_morse(text)
finally:
    GPIO.cleanup()
