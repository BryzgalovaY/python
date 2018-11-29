__author__ = 'Брызгалова Юлия Викторовна'

import os
import sys
import shutil

print("Домашнее задание №5")

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print()
print()
print("Easy. Задача-1")

dir_name = ['dir_1', 'dir_2', 'dir_3', 'dir_4', 'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9']

for i in dir_name:
    os.mkdir(i)
input("Директории созданы, нажмите ENTER чтобы их удалить.")
for i in dir_name:
    os.rmdir(i)	
print("Файлы успешно удалены.")


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print()
print()
print("Easy. Задача-2")

print(os.listdir())




# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print()
print()
print("Easy. Задача-3")

shutil.copy2(str(sys.argv[0]), r'копия файла.py')
print("Файл успешно скопирован.")