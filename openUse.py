import tkinter as tk
from main import start
from save_acc import *


def main():
    # Создайте окно
    window = tk.Tk()

    # Установите заголовок окна
    window.title("Мое приложение")
    window.geometry('300x500')

    # Создайте выпадающий список
    account = read_file('acc.txt')
    var_acc = tk.StringVar(window)
    var_acc.set(account[0])
    dropdown = tk.OptionMenu(window, var_acc, *account)
    dropdown.pack()

    case = read_file('case.txt')
    var_case = tk.StringVar(window)
    var_case.set(case[0])
    dropdown2 = tk.OptionMenu(window, var_case, *case)
    dropdown2.pack()

    # Создайте кнопку
    button = tk.Button(window, text="Кейс собран", command=lambda: start(var_acc.get(), var_case.get()))
    button.pack()

    button2 = tk.Button(window, text="Добавить аккаунт", command=lambda: add_acc(input_field.get(), 'acc.txt'))
    button2.pack()

    input_field = tk.Entry(window)
    input_field.pack()

    button3 = tk.Button(window, text="Добавить кейс", command=lambda: add_acc(input_field2.get(), 'case.txt'))
    button3.pack()

    input_field2 = tk.Entry(window)
    input_field2.pack()

    # Запустите главный цикл окна
    window.mainloop()


if __name__ == '__main__':
    main()
