#!/usr/bin/python3
import psutil
import os.path
import json
import zipfile

# Задание №1
disk_info = psutil.disk_partitions()
print("Информация о дисках")
for i in range(len(disk_info)):
    print(disk_info[i])

# Задание №2
print("Создать файл? (0/1)")
choose = int(input())
if choose:
    print("Введите название для нового файла: ")
    file_name = input()
    if os.path.exists(file_name):
        print("Данный файл уже существует, хотите перезаписать его? (0/1) ")
        choose2 = int(input())
        if choose2:
            file = open(file_name, 'w')
            print("Введите строку для записи: ")
            file_string = input()
            file.write(file_string + '\n')
            file.close()
    else:
        file = open(file_name, 'w')
        print("Введите строку для записи: ")
        file_string = input()
        file.write(file_string + '\n')
        file.close()
    with open(file_name) as f:
        lines = f.readlines()
        print(*lines)
    f.close()
    os.remove(file_name)
else:
    print('........')

# Задание 3
inf = { "student":
        { "name" : "Kate", 
        "courses": ["math", "programming"],
        "marks": [5, 4, 3, 5, 4, 2]
        },
        "teacher":
        { "name": "John",
        "students": ["Mike", "Kate", "Ian"]
        }
    }
inftojson = json.dumps(inf)
file = open('info.json', 'w')
file.write(inftojson + '\n')
file.close()
with open('info.json', 'r') as fjs:
    data = json.load(fjs)
print(data)
os.remove('info.json')

# Задание 4
with open("filexml.xml", 'a') as fxm:
    print("Введите строку для записи в файл:" )
    ss = input()
    fxm.write(ss + '\n')
fxm.close()
with open("filexml.xml", 'r') as fxm:
    lines = fxm.readlines()
    print(*lines)
os.remove("filexml.xml")

# Задание 5
zf = zipfile.ZipFile("myzip.zip", "w")
print("Введите название файла для ввода в архив")
file_name = input()
with zipfile.ZipFile("myzip.zip", 'w') as mz:
    mz.write(file_name)
with zipfile.ZipFile("myzip.zip", 'r') as mz:
    mz.extractall("./")
print('Информация о файле %s \n' %(file_name), os.stat(file_name))
os.remove("%s" %(file_name))
os.remove("myzip.zip")
