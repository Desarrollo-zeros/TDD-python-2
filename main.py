def is_prime(number: int):
    if number < 2:
        return False
    for i in range(2, int(number / 2) + 1):
        if (number % i) == 0:
            return False
    return True


def fibonacci(position: int):
    if position < 2:
        return 1
    a = 1
    b = 1
    for i in range(3, position + 1):
        c = a + b
        a = b
        b = c
    return b
