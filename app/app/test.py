"""Sample test for testing the test framework is working. """

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        res = calc.subtract(5, 11)
        self.assertEqual(res, 6)
