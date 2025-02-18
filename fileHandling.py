# задаем имя файла и текст, который допишем
filename = 'sample_text.txt'
additional_text = "\nЭта строчка добавлена в файл."

# открываем файл в режиме добавления и пишем в него новый текст
with open(filename, 'a') as file:
    file.write(additional_text)
print(f"Дополнительный текст добавлен в {filename}")

# читаем и выводим обновленное содержимое файла
with open(filename, 'r') as file:
    updated_content = file.read()

print("Читаем, что теперь в файле:")
print(updated_content)

# работаем с csv файлом
import csv

# задаем имя csv-файла и данные
csv_filename = 'people.csv'
data = [
    ["Имя", "Возраст", "Город"],
    ["Алиса", "30", "Нью-Йорк"],
    ["Боб", "25", "Лос-Анджелес"],
    ["Чарли", "35", "Чикаго"]
]

# записываем данные в csv
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f"Данные сохранены в {csv_filename}")

# читаем данные обратно из csv и печатаем их
print("Читаем данные из csv:")
with open(csv_filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# снова работаем с текстовым файлом
filename = 'sample_text.txt'
content = """Привет, мир!
Это тестовый файл.
Тут несколько строк текста, чтобы проверить работу с файлами."""

# записываем контент в файл
with open(filename, 'w') as file:
    file.write(content)
print(f"Контент записан в {filename}")

# читаем контент обратно
with open(filename, 'r') as file:
    read_content = file.read()

print("Читаем содержимое файла:")
print(read_content)
