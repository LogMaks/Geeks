#создадим скрипт калькулятора из используемых функций и модулей

#блок импорта модулей
import mycalc
import myrandom

def my_main():
    """"Эта главная функция, которая создает 2 случайных числа\
        и применяет к ним функции сложения и вычитания"""
    x = myrandom.random_1d()
    y = myrandom.random_2d()
    print('Случайные числа:', x, y)
    print('Сумма:', mycalc.add(x,y))
    print('Разность:', mycalc.substract(x,y))

    """print("x = {}, y = {}".format(x, y))
    print("sum is {}".format(sum))
    print("diff is {}".format(diff))"""

""" This is executed only if the special variable\
    '__name__' is set as main"""
if __name__ == "__main__":
    my_main()