import unittest

def reverse_string(st):
    s=''
    for i in st:
        s=i+s
    return s
def is_palindrome(st1):
    d=''
    for i in st1:
        if i.isalnum():
            d=d+i.lower()
    if d == d[::-1]:
        return True
    return False

class Testing(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertNotEqual(reverse_string("sam"), "samay")

    def test_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("Hello World"))

if __name__ == "__main__":
    unittest.main()



