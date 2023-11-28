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