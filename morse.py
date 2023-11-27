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