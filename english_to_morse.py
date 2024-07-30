# Morse code dictionaries
english_to_morse = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

morse_to_english = {
    '.-': 'A',    '-...': 'B',  '-.-.': 'C',  '-..': 'D',   '.': 'E',    
    '..-.': 'F',  '--.': 'G',   '....': 'H',  '..': 'I',    '.---': 'J', 
    '-.-': 'K',   '.-..': 'L',  '--': 'M',    '-.': 'N',    '---': 'O',  
    '.--.': 'P',  '--.-': 'Q',  '.-.': 'R',   '...': 'S',   '-': 'T',    
    '..-': 'U',   '...-': 'V',  '.--': 'W',   '-..-': 'X',  '-.--': 'Y', 
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', 
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '/': ' '  # Assuming '/' is used to represent spaces between words
}

# Function to translate English to Morse code
def english_to_morse_translation(text):
    decoded_message = []
    for char in text.upper():
        if char in english_to_morse:
            decoded_message.append(english_to_morse[char])
        else:
            decoded_message.append('?')  # Placeholder for unrecognized characters
    return ' '.join(decoded_message)

# Function to translate Morse code to English
def morse_to_english_translation(morse_code):
    words = morse_code.split(' / ')  # Split Morse code by '/' to separate words
    decoded_message = []
    for word in words:
        decoded_word = []
        for symbol in word.split():  # Split each word by space to get symbols
            if symbol in morse_to_english:
                decoded_word.append(morse_to_english[symbol])
            else:
                decoded_word.append('?')  # Placeholder for unrecognized Morse codes
        decoded_message.append(''.join(decoded_word))
    return ' '.join(decoded_message)

# Main loop for user input
check = "Yes"
while check == "Yes":
    input_type = input("What would you like to translate? 1- EN>M or 2-M>EN ")

    if input_type == "1":
        text = input("Type the word to be translated to Morse code: ")
        morse_code_output = english_to_morse_translation(text)
        print("Morse code:", morse_code_output)
    elif input_type == "2":
        text = input("Type the Morse code to be translated to English: ")
        morse_code_output = morse_to_english_translation(text)
        print("English text:", morse_code_output)
    else:
        print("Invalid input type. Please enter 1 or 2.")

    check = input("Do you want to translate another word? (Yes/No) ").capitalize()
