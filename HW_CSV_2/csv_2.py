import csv
import names
import random
import datetime

# Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310

def create_digits(name, dig_list):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(dig_list)


# Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами

def create_names(name, names_list):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(names_list)


# Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то@gmail.com

def create_emails(name, emails_list):
    with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(emails_list)


# Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.

def create_nne(name, nne_dict):
    with open(name, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["number", "name", "email"])
        writer.writeheader()
        writer.writerows(nne_dict)

def update_nne(file_name):
    with open(file_name, 'r', newline='') as f:
        ff = []
        reader = csv.DictReader(f, fieldnames=["number", "name", "email"])
        for j in reader:
            ff.append(j)


# Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
# a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)
# b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)
# с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)
# в) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно)
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[*ff[0].keys(), "date"])
        writer.writeheader()
        offset = 1
        for k in range(offset, len(ff)):
            date = datetime.datetime.now()
            if k < 50 + offset:
                ff[k]["date"] = date.replace(year=random.randint(1980, 1990))
            elif k < 150 + offset:
                ff[k]["date"] = date.replace(year=random.randint(1991, 2000))
            elif k < 300 + offset:
                ff[k]["date"] = date.replace(year=random.randint(2001, 2010))
            else:
                ff[k]["date"] = date.replace(year=random.randint(2011, 2021))
            writer.writerow(ff[k])

# Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
# a) Соберите имена из файла nne_2.csv.
# b) недостающие 550 строк имён сгенерируйте.
# с) Имена расположите в алфавитном порядке.
# d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
# e) Остальные даты генерировать рандомно.
# f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

def create_combo(nne_file_name, combo_file_name, names_list):
    with open(nne_file_name, 'r', newline='') as f:
        ff = []
        reader = csv.DictReader(f, fieldnames=["number", "name", "email", "date"])
        for j in reader:
            ff.append([j["name"], j["date"]])
        ff = ff + names_list
        sorted_data = sorted(ff[1:])

    with open(combo_file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "date", "phone", "gender", "salary"])
        writer.writeheader()
        gender_list = ["Male", "Female"]
        new_raw = {}
        phone_gen = lambda dig_str: "+" + dig_str[11:][::-1] + "(" + dig_str[8:11][::-1] + ")"\
                                    + "-" + dig_str[4:8][::-1] + '-' + dig_str[0:4][::-1]

        for k in range(1000):
            if len(sorted_data[k]) == 1:
                new_raw["name"] = sorted_data[k][0]
                new_raw["date"] = datetime.datetime.now()
                new_raw["email"] = new_raw["name"].replace(" ", "_") + "@yahoo.com"
                new_raw["phone"] = phone_gen(str(random.randint(111110000000, 99999999999999))[::-1])
                new_raw["gender"] = gender_list[random.randint(0, 1)]
                new_raw["salary"] = random.randint(1000, 99999)
            else:
                new_raw["name"] = sorted_data[k][0]
                new_raw["date"] = sorted_data[k][1]
                new_raw["email"] = new_raw["name"].replace(" ", "_") + "@yahoo.com"
                new_raw["phone"] = phone_gen(str(random.randint(111110000000, 99999999999999))[::-1])
                new_raw["gender"] = gender_list[random.randint(0, 1)]
                new_raw["salary"] = random.randint(1000, 99999)
            writer.writerow(new_raw)


digits_list = []
name_list = []
email_list = []
dict_list = []
for i in range(0, 1000):
    digits_list.append([i])
    rand_name = names.get_full_name()
    email = rand_name.replace(" ", "_") + "@yahoo.com"
    name_list.append([email])
    dict_list.append({"number": i, "name": rand_name, "email": email})

create_digits("digits_2.csv", digits_list[10:351])
create_names("names_2.csv", name_list[:400])
create_emails("emails_2.csv", email_list[:400])
create_nne("nne_2.csv", dict_list[0:450])
update_nne("nne_2.csv")
create_combo("nne_2.csv", "combo.csv", name_list[450:])
