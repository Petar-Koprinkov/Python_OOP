from typing import List


def get_primes(numbers: List):
    for number in numbers:
        if number <= 1:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number


print(list(get_primes([7, 9])))