# Создать переменную типа String
st = "Hello"
# Создать переменную типа Integer
i = 5
# Создать переменную типа Float
f = 3.5
# Создать переменную типа Bytes
by = b"name"
# Создать переменную типа List
l = [1, 2, 3]
# Создать переменную типа Tuple
t = tuple('hello')
# Создать переменную типа Set
s = {'h','e','l','l','o'}
# Создать переменную типа Frozen set
fr = frozenset('hello')
# Создать переменную типа Dict
d = {'name': 'Nick', 'age': 22, 'location': 'Minsk'}

# Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("string", st, type(st))
print("i =", i, type(i))
print("f =", f, type(f))
print("bytes", by, type(by))
print("LIST ", l, type(l))
print("tuple ", t, type(t))
print("set", s, type(s))
print("frozen", fr, type(fr))
print("dict", d, type(d))

# Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
first = "hello"
second = "world"
k = first + second
print(k)

# Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
# print(st, i) - будет слитно
print(st, i, sep=' ')

# Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
st = "Hello "
i = 5
print(st + str(i))
# print(st + ' ' + str(i))
