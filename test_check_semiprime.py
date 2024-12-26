import unittest
from check_semiprime import isSemiprime, find_semiprimes

class TestSemiprime(unittest.TestCase):
    def test_small_semiprimes(self):
        """Test known small semiprime numbers"""
        known_semiprimes = [4, 6, 9, 10, 14, 15, 21, 22, 25, 26]
        for num in known_semiprimes:
            self.assertTrue(isSemiprime(num), f"{num} should be semiprime")
    
    def test_non_semiprimes(self):
        """Test numbers that are not semiprimes"""
        non_semiprimes = [1, 2, 3, 8, 12, 16, 27, 30]
        for num in non_semiprimes:
            self.assertFalse(isSemiprime(num), f"{num} should not be semiprime")
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertFalse(isSemiprime(1))  # 1 is not semiprime
        self.assertFalse(isSemiprime(2))  # Prime numbers are not semiprime
        
    def test_negative_numbers(self):
        """Test negative numbers"""
        with self.assertRaises(ValueError):
            isSemiprime(-4)
    
    def test_find_semiprimes_range(self):
        """Test finding semiprimes in a range"""
        expected = [4, 6, 9, 10]
        self.assertEqual(find_semiprimes(1, 10), expected)

if __name__ == '__main__':
    unittest.main()