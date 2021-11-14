#Основные кодировки текстовых файлов:utf-8,windows-1251
file = open('text.txt','r',encoding='utf-8')
#Считывание файлов посимвольно
print(file.read(2))
print(file.read(1))
#После работы с файлом обязательно его закрываем
file.close()
file = open('text.txt','r',encoding='utf-8')
#Построчное считывание файлов
print(file.readline())
print(file.readline())
file.close()
file = open('text.txt','r',encoding='utf-8')
print(file.readlines())
file.close()
#Открываем файл на дозапись
file = open('text.txt','a',encoding='utf-8')
file.write('\nНовая строка')
file.close()
with open('text.txt','a',encoding='utf-8') as outfile:
    outfile.write('\nЭта строка добавлена через with as')
