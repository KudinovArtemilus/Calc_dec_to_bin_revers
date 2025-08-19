def dec_to_bin(n: int) -> str:
    """Перевод из десятичного в двоичное"""
    return bin(n)[2:]


def bin_to_dec(b: str) -> int:
    """Перевод из двоичного в десятичное"""
    return int(b, 2)


def calculator():
    while True:
        print("\n---- Калькулятор----")
        print("1. Десятичное -> Двоичное")
        print("2. Двоичное -> Десятичное")
        print("3. Выход")

        choice = input("Выберите действия (1/2/3): ")

        if choice == '1':
            try:
                num = int(input("Введите десятичное число: "))
                print(f"Двоичное {dec_to_bin(num)}")
            except ValueError:
                print("Ошибка: нужно ввести десятичное число")
        elif choice == '2':
            try:
                bnum = input("Введите двоичное число: ")
                print(f"Десятичное: {bin_to_dec(bnum)}")
            except ValueError:
                print("Ошибка: нужно ввести двоичное число")
        elif choice == '3':
            print("Выход из программы...")
            break
        else:
            print("Некорректный выбор!")


calculator()
