"""The sum of the squares of the first ten natural numbers is, 1**2+2**2+....10***2 = 385

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


def square_of_the_sums(numbers):
    s = sum(i for i in range(1, numbers+1))
    ss = sum(i**2 for i in range(1, numbers+1))
    return s**2 - ss



print(square_of_the_sums(100))