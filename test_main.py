from unittest import TestCase

from main import PrimeFactor


class TestPrimeFactor(TestCase):
    def test_prime_factor_of_1(self):
        prime_factor = PrimeFactor()
        self.assertEqual(prime_factor.of(1), [])

    def test_prime_factor_of_2(self):
        prime_factor = PrimeFactor()
        self.assertEqual(prime_factor.of(2), [2])
