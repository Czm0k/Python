import csv
import names


# Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
# Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.

# Создать пустой empty.csv файл.
def create_empty_file(name):
    f = open(name, 'w')
    f.close()
    print(f)

# Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
def create_file_with_0_to_150(name):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        for i in range(0, 151):
            writer.writerow([i])


# Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
def create_names(name):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        for i in range(0, 100):
            writer.writerow([names.get_full_name()])


# Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
def create_emails(name):
     with open(name, 'w') as f:
        writer = csv.writer(f)
        for i in range(0, 100):
            writer.writerow([names.get_full_name().replace(' ', '_')+'@gmail.com'])

# Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
def create_nne(name):
    with open(name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['number', 'name', 'email'])
        writer.writeheader()
        for i in range(0, 100):
            rand_name = names.get_full_name()
            writer.writerow({"number": i, "name": rand_name, "email": rand_name.replace(' ', '_')+'@gmail.com'})


create_empty_file('empty.csv')
create_file_with_0_to_150('digits.csv')
create_names('names.csv')
create_emails('emails.csv')
create_nne('nne.csv')