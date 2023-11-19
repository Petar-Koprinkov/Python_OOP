def squares(n):
    for number in range(1, n + 1):
        yield number * number
        number += 1


print(list(squares(5)))
