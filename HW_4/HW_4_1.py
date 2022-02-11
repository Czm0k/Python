# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

# USD
usd_item = 'usd'
usd_usd_rate = 1

# EUR
eur_item = 'eur'
usd_eur_rate = 0.86

target_currency = int(input("Введите количество денег: "))

if target_currency:
    currency_result = target_currency / usd_eur_rate
    print("Вы ввели", target_currency, eur_item)
    print("Конвертировання сумма в", usd_item, "=", int(currency_result))
else:
    print('Введите число > 0')
