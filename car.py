import random,json,colorama,copy
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
class Car:
    def __init__(self):
        with open('map.json',encoding='windows-1251') as infile:
            self.map = json.load(infile)
        self.power = False
        self.doors = False
        self.time = False
                           #ночь день
        self.choosen_city = None
        self.color = WHITE
        self.lights = False
        self.home = [0,0]
    def power_on(self):
        if self.doors == True:
            if self.power == False:
                self.power = True
                print('Машина заведина')
            else:
                print('Машина уже заведина')
        else:
            print('откройте двери чтобы завести машину')
    def  power_off(self):
        if self.power == True:
            self.power = False
            print('машина заглушена')
        else:
            print('машина уже заглушина')
    def open_doors(self):
        if self.doors == False:
            self.doors = True
            print('двери открыты')
        else:
            print('двери уже открыты')
    def close_doors(self):
        if self.lights == False:
            if self.power == False:
                if self.doors == True:
                    self.doors = False
                    print('двери закрыты')
                else:
                    print('двери уже закрыты')
            else:
                print('заглушите двигатель чтобы закрыть машину')
        else:
            print('выключите фары чтобы закрыть машину')


    def set_day(self):
        if self.time == False:
            self.time = True
            print('установлен день')
        else:
            print('время суток-день')
    def set_night(self):
        if self.time == True:
            self.time = False
            print('установлена ночь')
        else:
            print('время суток-ночь')
    def set_color(self,color):
        if self.color != color:
            self.color = color
            print(f'машина перкрашена в {color}')
        else:
            print(f'машина уже {color}')
    def lights_on(self):
        if self.power == True:
            if self.lights == False:
                self.lights = True
                print('фары включены')
            else:
                print('фары уже включены')
        else:
            print('заведите двигатель чтобы включить фары')

    def lights_off(self):
        if self.lights == True:
            self.lights = False
            print('фары выключены')
        else:
            print('фары уже выключены')
    def read_cities(self):
         return list(self.map.keys())
    def choice_city(self,name_city):
        if self.map.get(name_city) == None:
            print('такого города не существует')
            return None
        print(f'загрузка города {name_city} выполнена')
        self.choosen_city = copy.deepcopy(self.map[name_city])
        for i in range(len(self.choosen_city[0])):
            if self.choosen_city[0][i] == 1:
                self.choosen_city[0][i] = '*'
                break
        self.home = [0,i]
        return self.choosen_city

    '''
    При двежении вправо номер строки не изменяется,изменяется только номер столбца self.home[1] 
    Мы проверяем заведен ли двигатель или на улице ночь и включены ли фары.
    Мы проверяем позицию на когторую хотим встать
    self.home[0] - позиция по x,т.е. номер строки где стоит машина до движения
    self.home[1] - позиция по y,т.е. номер столбца где стоит машина до движения
    self.home[1] + steps - позиция столбца в которую мы хотим переместится
    '''

    def right(self,steps):
        if self.power == True:
             if self.time == True or (self.time == False and self.lights == True):
                    if self.choosen_city[self.home[0]][self.home[1] + steps] == 1:
                     #если сумма всех элементов от позиции где стоит машина до позиции куда хотим встать
                     #ровна количеству шагов это значит по пути есть дорога
                     if sum(self.choosen_city[self.home[0]][self.home[1] + 1: self.home[1] + steps + 1]) == steps:
                         #ставим звёздочку на новое место self.home[1] + steps
                         self.choosen_city[self.home[0]][self.home[1] + steps] = '*'
                         #стаавим единицу на старое место self.home[1]
                         self.choosen_city[self.home[0]][self.home[1]] = 1
                         #запоминаем новые координаты
                         self.home = [self.home[0],self.home[1] + steps]
                         for i in self.choosen_city:
                             print(*i)
                     else:
                         print('нельзя сделать шаг')
             else:
                print('включите фары чтобы начать движение')
        else:
            print('включите двигатель чтобы начать движение')
        print('\n')


    def left(self,steps):
        if self.power == True:
            if self.time == True or (self.time == False and self.lights == True):
                #if self.choosen_city[self.home[0]][self.home[1] - steps] >
                    if self.choosen_city[self.home[0]][self.home[1] - steps] == 1:
                         #если сумма всех элементов от позиции где стоит машина до позиции куда хотим встать
                         #ровна количеству шагов это значит по пути есть дорога
                        if sum(self.choosen_city[self.home[0]][self.home[1] - steps - 1:self.home[1] - 1 ]) == steps:
                             #ставим звёздочку на новое место self.home[1] + steps
                             self.choosen_city[self.home[0]][self.home[1] - steps] = '*'
                             #стаавим единицу на старое место self.home[1]
                             self.choosen_city[self.home[0]][self.home[1]] = 1
                             #запоминаем новые координаты
                             self.home = [self.home[0],self.home[1] - steps]
                             for i in self.choosen_city:
                                 print(*i)
                        else:
                            print('нельзя сделать шаг')
                    else:
                         print('Нельзя сделать шаг')
            else:
                print('включите фары чтобы начать движение')
        else:
            print('включите двигатель чтобы начать движение')
        print('\n')


    def up(self,steps):
        sum = 0
        if self.power == True:
            if self.time == True or (self.time == False and self.lights == True):
                if self.choosen_city[self.home[0] - steps][self.home[1]] != 0:
                    for b in range(self.home[0] - 1,self.home[0] - steps - 1,-1):
                        sum += self.choosen_city[b][self.home[1]]
                    if sum == steps:
                        self.choosen_city[self.home[0] - steps][self.home[1]] = '*'
                        self.choosen_city[self.home[0]][self.home[1]] = 1
                        self.home = [self.home[0 ] - steps,self.home[1]]
                        for i in self.choosen_city:
                            print(*i)
                    else:
                        print('на пути препятствие')
                else:
                    print('нельзя переместится в пункт назначения')
            else:
                print('включите фары чтобы начать движение')
        else:
            print('включите двигатель чтобы начать движение')
        print('\n')


    def down(self, steps):
        sum = 0
        if self.power == True:
            if self.time == True or (self.time == False and self.lights == True):
                #if self.choosen_city[self.home[0] + steps][self.home[1]] < len(self.choosen_city
                    if self.choosen_city[self.home[0] + steps][self.home[1]] != 0:
                        for i in range(self.home[0] + 1, self.home[0] + steps + 1,1):
                            sum += self.choosen_city[i][self.home[1]]
                        if sum == steps:
                            self.choosen_city[self.home[0] + steps][self.home[1]] = '*'
                            self.choosen_city[self.home[0]][self.home[1]] = 1
                            self.home = [self.home[0] + steps,self.home[1]]
                            for i in self.choosen_city:
                                for g in i:
                                    if g == 1:
                                        print(f'\033[34m{g}\033[0m',end=' ')
                                    else:
                                        print(g,end=' ')
                                print()
                        else:
                            print('на пути препятствие')
                    else:
                        print('нельзя переместится в пункт назначения')
            else:
                print('включите фары чтобы начать движение')
        else:
            print('включите двигатель чтобы начать движение')
        print('\n')


car = Car()
print(car.map)
car.choice_city('city')
for i in car.choosen_city:
    print(*i)
car.open_doors()
car.power_on()
car.lights_on()
car.lights_off()
car.power_off()
car.close_doors()
car.set_night()
car.open_doors()
car.power_on()
car.lights_on()
car.down(1)
car.right(1)
car.down(4)
car.left(3)
car.down(1)
car.right(3)



