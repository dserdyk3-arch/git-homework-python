def add(a, b):
    """Функция сложения двух чисел"""
    return a + b

def subtract(a, b):
    """Функция вычитания двух чисел"""
    return a - b

def multiply(a, b):
    """Функция умножения двух чисел"""
    return a * b

def divide(a, b):
    """Функция деления двух чисел"""
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

# Пример использования
if __name__ == "__main__":
    print("Простой калькулятор")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"5 / 3 = {divide(5, 3)}")
Шаг 3: Обновите README.md
Обновите содержимое README.md:

Markdown

# Git Homework Repository

Это репозиторий для выполнения домашнего задания по системе контроля версий Git.

## Описание проекта

Простой калькулятор на Python с базовыми арифметическими операциями.

## Функционал

- Сложение двух чисел
- Вычитание двух чисел
- Умножение двух чисел
- Деление двух чисел с проверкой на деление на ноль

## Использование

```python
from calculator import add, subtract, multiply, divide

result = add(5, 3)  # 8
result = subtract(10, 4)  # 6
