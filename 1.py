import re
import unittest

class TestIsValidEmail(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("first.last@domain.co"))
        self.assertTrue(is_valid_email("a_b-c.d@sub.domain.org"))

    def test_invalid_email(self):
        self.assertFalse(is_valid_email("userexample.com"))  # missing @
        self.assertFalse(is_valid_email("user@.com"))        # missing domain name
        self.assertFalse(is_valid_email("@example.com"))     # missing username
        self.assertFalse(is_valid_email("user@domain"))      # missing TLD
        self.assertFalse(is_valid_email("user@domain,com"))  # invalid character
        self.assertFalse(is_valid_email("user@domain..com")) # double dot

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    unittest.main(exit=False)
    email = input("Enter an email to validate: ")
    if is_valid_email(email):
        print("Valid email.")
    else:
        print("Invalid email.")
