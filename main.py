class PrimeFactor:
    def of(self, number):
        factors = []
        divisor = 2
        while number > 1:
            while not number % divisor:
                factors.append(divisor)
                number //= divisor
            divisor += 1
        return factors
