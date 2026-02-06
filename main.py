def factorial(num: int) -> int:
    if num == 1:
        return num
    else:
        fact = factorial(num - 1)
        fact *= num
        return fact


print(factorial(5))
