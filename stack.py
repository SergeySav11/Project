'''
Стэк-структура данных для хранения порядка
Принцип стэка - последний зашел первый вышел
Оперцании над стэком:удаление последнего элемента(pop),добавление последнего элемента в конец(push)
'''
class Stack:

    #Пекречисляем свойства класса
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def push(self,a):
        self.stack.append(a)
class Calculator:
    def __init__(self):
        pass

    def plus(self,a,b):
        return a + b

    def minus(self,a,b):
        return a - b

    def second_stepen(self,a):
        return a * a

o = Calculator()
a,b = list(map(int,input().split()))
sum = o.plus(a,b)
sum_2 = o.minus(a,b)
sum_3 = o.second_stepen(a)
print(f'{a} + {b} = {sum}')
print(f'{a} - {b} = {sum_2}')
print(f'{a} ^ 2 = {sum_3}')