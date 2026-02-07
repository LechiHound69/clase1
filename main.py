def factorial(num: int) -> int:
    """
    Factorial

    Una función para calcular el factorial de un número entero ingresado
    :type num: int
    :return: El factorial calculado del número num ingresado
    :rtype: int
    """
    if num == 1:
        return num
    else:
        fact = factorial(num - 1)
        fact *= num
        return fact


print(factorial(5))
print("cfff")
