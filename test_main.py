import sys
from io import StringIO
import unittest
from main import hello

class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        hello()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), 'hi')

if __name__ == '__main__':
    unittest.main()