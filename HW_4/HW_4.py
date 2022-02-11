# WHILE

# Создать переменную count со значением 0
count = 0
# Создать переменную range_count со значением 10
range_count = 10
# Создать переменную for_count со значением 0
for_count = 0
# Создать переменную run  со значением True
run = True

# # Сделать цикл while который будет работать пока run
# while run:
#     print("Hello Cycle")

# # Сделать цикл while который будет работать пока run
# while run:
#     print("Step =", count)
#     count += 1

# # Сделать цикл while который будет работать пока count < range_count
# while count < range_count:
#     print("Step =", count)
#     count += 1

# # Сделать цикл while который будет работать пока count < range_count
# while count < range_count:
#     print("Step =", count)
#     count += 1
#     if count == 3:
#         print("Step =", count, 'if body')
#
# # Сделать цикл while который будет работать пока run
# while run:
#     print("Step =", count)
#     count += 1
#     if count == range_count:
#         print("STOP", count)
#         break

# =================================================================================

# FOR
#
# # Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
# for item in range(for_count, range_count):
#     print("Step =", item)
#
# # Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
# for item in range(0, 30):
#     print("Step =", item)
#     if item == 5:
#         print('item =', item)
#     if item == 10:
#         print('item =', item)
#     if item < 4:
#         print('item <', item)
#     if item >= 27:
#         print('item >=', item)
#
# # Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
# for item in range(0, range_count + 1):
#     print('Step =', item)
#     if item == 7:
#         inner_count = 0
#         print('--Inner_count =', inner_count)
#         for inner_item in range(0, item):
#             print('-------- Inner_Step =', inner_item)
#             if inner_item == 5:
#                 inner_count = inner_item
# print('--inner_count =', inner_count)
#
# Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
for item in range(0, 20):
    print('Step =', item)
    if item > 7 and item < 12:
        print('if_item =', item)
        continue
print('End_iteration =', item)