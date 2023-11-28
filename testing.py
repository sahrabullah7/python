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
    