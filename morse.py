MORSECODE = {   # dictionary
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}

def Morse_function(string, MORSECODE): #def: what is morsecode    #MORSECODE: for knowing where to change from eng to morse   #this function converts from english to morse code
    string = string.upper()  #upper: to make every letter passing upper case
    result = []
    for letter in string: #for loop:to pass for every letter 
        if letter in MORSECODE: #if: to search line by line
            result.append(MORSECODE[letter])  # search the dictionary for each letter to translate it
        elif letter == " ":
            result.append("/") #incase there is a space in the sentence print (/)
        else: # not to stop the code so if there is a letter not found a massage will be printed (raising error)
            raise ValueError (f"The '{letter}' key doesn't exist in the dictionary")  # Raise an error if the letter is not in the dictionary   #valueerror:A function receives an argument that is right type but a bad value
    return ' '.join(result)  #form spaces between letters not to confuse the user

def English_function(string, MORSECODE): #this function converts from morse code to english
    morse_words = string.split('/')  # get a massage and split it into seperate words by /
    result = ""  #store the results
    for morse_word in morse_words: #to get single word in the sentence
        morse_letters = morse_word.strip().split()  #to split the word into letters  #strip: remove extra spaces
        for letter in morse_letters: #to pass on every letter in the word
            if letter in MORSECODE.values(): #check if the given letter exists as a value in the dictionary
                result += [key for key, value in MORSECODE.items() if value == letter][0]  #search the dictionary for each letter to translate it
            else:
                raise ValueError(f"The '{letter}' key doesn't exist in the dictionary")  # Raise an error if the Morse code is not in the dictionary    #valueerror:A function receives an argument that is right type but a bad value
        result += " "  # Add space between words after passing on every letter
    return result.strip()  # Remove extra spaces

def choosing_input(): #to make the user chose which translation he wants
    
    choice = input("Press 'e' for English to Morse code or 'm' for Morse code to English: ").lower() #the choice   #lower:not to raise an error if the user wrote the choice in capital letter

    # Check the user's choice
    if choice == "e":
        string = input("Enter english text: ")
        print(Morse_function(string, MORSECODE))  # Call the function to convert English to Morse code
    elif choice == "m":
        string = input("Enter Morse code text (use '.' for dot and '-' for dash, space between letters and '/' between words): ")
        print(English_function(string, MORSECODE))  # Call the function to convert Morse code to English
    else:
        print("Choose a correct letter.")  # Print an error message for an incorrect choice

choosing_input()