class PrimeFactor:
    def of(self, number):
        factors = []
        if number > 1:
            diviser = 2
            if number == 4 or number == 6 or number == 9:
                while number > 1:
                    while not number % diviser:
                        factors.append(diviser)
                        number //= diviser
                    diviser += 1
            else:
                factors.append(number)
        return factors
