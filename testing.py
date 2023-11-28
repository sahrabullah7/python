from morse import MORSECODE,Morse_function,English_function,choosing_input

# Import the 'unittest' module, which provides a testing framework
import unittest

# Define a test class thats from 'unittest.TestCase'
class TestMorseCodeConversion(unittest.TestCase):

    # Define a test method for converting English to Morse code
    def test_english_to_morse(self):
        # Define the expected Morse code result for the input 'HELLO TKH USERS'
        expected_result = '.... . .-.. .-.. --- / - -.- .... / ..- ... . .-. ...'
        
        # Call the 'Morse_function' function to convert 'HELLO TKH USERS' to Morse code
        actual_result = Morse_function('HELLO TKH USERS', MORSECODE)
        
        # Assert that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")
    
    # Define a test method for converting Morse code to English
    def test_morse_to_english(self):
        # Define the expected English result for the input Morse code
        expected_result = 'HELLO TKH USERS' 
        
        # Call the 'English_function' function to convert the Morse code to English
        actual_result = English_function('.... . .-.. .-.. --- / - -.- .... / ..- ... . .-. ...', MORSECODE)
        
        # check that the actual result matches the expected result; otherwise, raise an AssertionError with a custom error message
        self.assertEqual(actual_result, expected_result, f"Expected: {expected_result}\nActual: {actual_result}")

    # Test that an error is raised for invalid English input
    def test_invalid_english_to_morse(self):

        with self.assertRaises(ValueError):  

            Morse_function('H3ll0', MORSECODE)  #call a wrong function   #the code will pause if the unknown letter is in the middle or the beginning and it wont continue the rest of the word or sentence

    # Test that an error is raised for invalid morse code input
    def test_invalid_morse_to_english(self):

        with self.assertRaises(ValueError):  

            English_function('..../.-/-..---', MORSECODE)   #call a wrong function

    # Test conversion from Morse code with space
    def test_morse_code_with_space(self): #check the less spaces in the sentence
        
        expected_result = 'HELLO TKH USERS'  # Expected English text for '.... . .-.. --- --- / - -.- .... / ..- ... . .-. ...'
        actual_result = English_function('.... . .-.. --- ---  - -.- ....  ..- ... . .-. ...', MORSECODE)
        print(f"Expected: {expected_result}\nActual: {actual_result}")


if __name__ == '__main__':
    unittest.main()