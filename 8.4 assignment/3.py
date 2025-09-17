import unittest

def is_sentence_palindrome(sentence):
    cleaned = ''.join(c.lower() for c in sentence if c.isalnum())
    return cleaned == cleaned[::-1]

class TestIsSentencePalindrome(unittest.TestCase):
    def test_true_palindromes(self):
        self.assertTrue(is_sentence_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_sentence_palindrome("Madam In Eden, I'm Adam"))
        self.assertTrue(is_sentence_palindrome("Able was I ere I saw Elba"))
        self.assertTrue(is_sentence_palindrome("No lemon, no melon"))
        self.assertTrue(is_sentence_palindrome("Was it a car or a cat I saw"))
    def test_false_palindromes(self):
        self.assertFalse(is_sentence_palindrome("Hello world"))
        self.assertFalse(is_sentence_palindrome("Python is fun"))
        self.assertFalse(is_sentence_palindrome("This is not a palindrome"))
    def test_empty_and_single(self):
        self.assertTrue(is_sentence_palindrome(""))
        self.assertTrue(is_sentence_palindrome("a"))
        self.assertTrue(is_sentence_palindrome(" "))

if __name__ == "__main__":
    unittest.main(exit=False)
    sentence = input("Enter a sentence to check palindrome: ")
    if is_sentence_palindrome(sentence):
        print("Palindrome!")
    else:
        print("Not a palindrome.")
