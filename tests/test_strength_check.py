import unittest
from analyzer.strength_check import analyze_password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_weak_password(self):
        result = analyze_password_strength("abc")
        self.assertEqual(result["klassificering"], "Svagt")
        self.assertIn("Använd minst 12 tecken.", result["förbättringar"])

    def test_medium_password(self):
        result = analyze_password_strength("abc123ABC")
        self.assertEqual(result["klassificering"], "Medel")

    def test_strong_password(self):
        result = analyze_password_strength("Abc123!@#xyz")
        self.assertEqual(result["klassificering"], "Starkt")

    def test_missing_uppercase(self):
        result = analyze_password_strength("abc123!@#xyz")
        self.assertIn("Lägg till stora bokstäver.", result["förbättringar"])

    def test_missing_digits(self):
        result = analyze_password_strength("Abc!defXYZ")
        self.assertIn("Lägg till siffror.", result["förbättringar"])

if __name__ == "__main__":
    unittest.main()
