#Testing the commit

english_to_morse ={
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}
check = "Yes"
while check == "Yes":
  morse_code = []
  text = input("Type the word to be translated to Morse code: ")

  def translation (text):
    for char in text.upper():
      morse_code.append(english_to_morse[char])

    return ' '.join(morse_code)

  morse_code_output = translation(text)
  print("Morse code:", morse_code_output)
  check = input("Do you want to translate another word? (Yes/No) ")

