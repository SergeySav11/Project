list = [5,4,6]
'''
Словарь-структура данных доступ к информации у которой * по ключу
Множество-структура данных для хранения уникальных значений
'''
dict()
d = {'dict': 1, 'dictionary': 2}
print(d['dict'])
set()
a= set([3,1,7,7])
{}
print(a)
names = set()
name = input()
visitors = dict()
while name != '0':
    names.add(name)
    if visitors.get(name) != None:
        visitors[name] +=1
    else:
        visitors[name] = 1
    name = input()
print(names)
print(visitors)