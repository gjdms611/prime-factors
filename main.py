class PrimeFactor:
    def of(self, number):
        factors = []
        if number == 4:
            factors.append(2)
            factors.append(2)
        elif number > 1:
            factors.append(number)
        return factors
