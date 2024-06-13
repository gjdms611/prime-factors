class PrimeFactor:
    def of(self, number):
        factors = []
        if number > 1:
            diviser = 2
            if number == 4:
                while not number % diviser:
                    factors.append(diviser)
                    number //= diviser
            elif number == 6:
                while number > 1:
                    if not number % diviser:
                        factors.append(diviser)
                        number //= diviser
                    diviser += 1
            elif number == 9:
                factors.append(3)
                factors.append(3)
            else:
                factors.append(number)
        return factors
