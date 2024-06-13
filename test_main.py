from unittest import TestCase

from main import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor(self):
        prime_factor = PrimeFactor()
        self.assertEqual(prime_factor.of(2), [2])
        self.assertEqual(prime_factor.of(3), [3])
        self.assertEqual(prime_factor.of(2), [2])
        self.assertEqual(prime_factor.of(2), [2])
        self.assertEqual(prime_factor.of(2), [2])
        self.assertEqual(prime_factor.of(2), [2])
