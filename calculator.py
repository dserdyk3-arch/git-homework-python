"""Расширенный калькулятор с дополнительными функциями"""

def power(base, exponent):
    """Возведение в степень"""
    return base ** exponent

def factorial(n):
    """Вычисление факториала"""
    if n < 0:
        return "Ошибка: факториал отрицательного числа!"
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def square_root(n):
    """Квадратный корень"""
    if n < 0:
        return "Ошибка: корень из отрицательного числа!"
    return n ** 0.5

if __name__ == "__main__":
    print("Расширенный калькулятор")
    print(f"2^10 = {power(2, 10)}")
    print(f"5! = {factorial(5)}")
    print(f"√16 = {square_root(16)}")