#фрагмент кода файла myrandom.py
import random #импорт модуля random для генерации случайных чисел

def random_1d():
    """Эта функция возвращает случайное число от 0 до 9"""
    return random.randint(0,9)

def random_2d():
    """Эта функция возвращает случайное число от 10 до 99"""
    return random.randint(10,99)