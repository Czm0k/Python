# 2) В виде функций - код разбит на функции. Отдельные функции можно вынести в другие .py файлы и
# вызывать их в main.py предвварительно импортируя в main.py.

def dict_data(**kwargs):
    global c
    c = {**kwargs}


def change():
    while True:
        a = input("Выберите валюту из ['usd','eur','chf','gbp','cny']: ")
        for k, v in c.items():
            if k == a:
                b = input("Введите сумму: ")
                if b.strip() == "":
                    print("Вы ввели пустое поле. Введите число.")
                else:
                    try:
                        if int(b) > 0:
                            print("Вы ввели " + b + " usd и валюту " + a)
                            result = int(b) * v
                            print("Конвертировання сумма в", a, "=", int(result))
                        elif int(b) < 0:
                            print("Введите положительное число.")
                        elif int(b) == 0:
                            print("Введите число > 0.")
                    except ValueError:
                        print("Вы ввели не число. Введите число.")

def fun_task_4():
    dict_data(usd=1, eur=0.88, chf=0.91, gbp=0.75, cny=6.36)
    change()