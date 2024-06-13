class PrimeFactor:
    def of(self, number):
        factors = []
        diviser = 2
        while number > 1:
            while not number % diviser:
                factors.append(diviser)
                number //= diviser
            diviser += 1
        return factors
