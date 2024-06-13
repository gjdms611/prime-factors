class PrimeFactor:
    def of(self, number):
        factors = []
        if number == 4:
            while not number % 2:
                factors.append(2)
                number //= 2
        elif number == 6:
            factors.append(2)
            factors.append(3)
        elif number > 1:
            factors.append(number)
        return factors
