#!/usr/bin/env python3

def main():
    try:
        a = int(input("Введите A: "))
        b = int(input("Введите B: "))
        x = int(input("Введите X: "))
        if x <= 4:
            y = ((a * a) / (x * x)) + 6 * x
        else:
            y = (b * b) * ((4 + x) * (4 + x))
        print(f"y = {y:.2f}")
    except ValueError:
        print("Неверные входные данные!")
    except ArithmeticError:
        print("Нет решения!")


if __name__ == "__main__":
    main()
    input("Нажмите любую клавишу чтобы выйти...")
