import unittest
from io import StringIO
import sys

class TestSumEvenNumbers(unittest.TestCase):

    def test_sum(self):
        # Redirect sys.stdout to capture the program output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Import and call the main function from the SumEvenNumbers module
        from SumOfEvenNumbers import main
        main()

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Expected output
        expected_output = 2550

        # Convert captured output to an integer and check if it matches the expected result
        self.assertEqual(expected_output, int(captured_output.getvalue().strip()))

if __name__ == '__main__':
    unittest.main()
