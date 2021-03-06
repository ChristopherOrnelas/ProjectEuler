"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

def lista():
    multiplo = []
    for c in range(0, 1000):
        if c % 3 == 0 or c % 5 == 0: multiplo.append(c)
    return sum(multiplo)


print(lista())