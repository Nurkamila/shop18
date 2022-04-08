# ООП -> объектно-ориентированное программирование
# Аттрибуты - переменные внутри класса
# print(object)
# print(dir(object))

# class Person:
#     legs = 2
#     arms = 2
#     eyes = 2
#     mouth = 1

#     def __init__(self, name, age):
#         self.name = name
#         self._age = age
#         # self.__secret = 'secret'

#     def __str__(self):
#         return f'STR METHOD: {self.name} - {self._age}'


#     # def walk(self, km):
#         # print(f'{self.name} ходит {km} km')

# person1 = Person('Nurka', 19)
# # person2 = Person('Nurgazy', 39)

# # person1.walk(3)
# # person2.walk(4)
# print(person1)

# print(person1.__secret) - так он не найдет
# print(person1._Person__secret) - но так найдет

# Наследование - это когда мы создаем наследование
# Инкапсуляция - 1) это _ - защищенные методы или __ == сокрытие данных
#                2) один класс для одной задачи + в одном классе есть все необходимые методы и аттрибуты для решения этой задачи

# Полиморфизм - это одинаковое имя, но разной логики


# TASK1
# class Person:
#     def walk(self);
#     print('человек ходит')

# def func(objects):
#     for obj in objects:
#         obj.walk()

# list_ = [Dog(), Cat(), Person()]

# TASK2
# def func_start_time(func):
#     from datetime import datetime
#     date = datetime.now()
#     def wrapper():
#         print(f"Функция запущена {date}")
#         func()
#     return wrapper

# @func_start_time
# def func():
#     print('Hello world')
# func()

# TASK3
# def make_bold(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         return f'<i>{func()}</i>'
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper


# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
# print(hello())

# TASK4
# def benchmark(func):
#     import time
#     def wrapper():
#         start = time.time()
#         end = time.time()
#         final = end - start
#         func()
#         return f'Время выполнения: {final}'
#     return wrapper


# @benchmark
# def fetch_webpage():
#     import requests
#     webpage = requests.get('https://google.com')
# print(fetch_webpage())

# TASK5
# users = {'jaanger': '123312', 'vlad': '46456',
#          'nazar': '456132', 'tima': '456123'}


# def validate_password(func):
#     def wrapper(username, password):
#         if username not in users.keys():
#             print('Username is not defined')
#         elif password != users[username]:
#             print('Password is invalid')
#         else:
#             func(username, password)
#     return wrapper


# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')


# login('jaanger', '123312')


# users = {"bob": '1234', "ren": '4567',
#          "garry": '9876'}

# def validate_password(func):
#     def wrapper(username, password):
#         if username not in users.keys():
#             print('Username is not defined')
#         elif password != users[username]:
#             print('Password is invalid')
#         else:
#             func(username, password)
#     return wrapper

# @validate_password
# def login(username, password):
#     print(f'Welcome, {username}')
# login('ren', '4567')

# TASK6
# def is_admin(func):
#     def wrapper(arg):
#         if arg['is_admin'] == True:
#             print(f"Доступ разрешен {arg['username']}")
#         else:
#             print(f"Доступ запрещен {arg['username']}")
#     return wrapper

# @is_admin
# def get_user(dict):
#     return dict

# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})

# TASK7
# def route(func):
#      def wrapper(path):
#           return 'https://www.mywebsite.com/' + path
#      return wrapper

# @route
# def get_page(path):
#      return path

# print(get_page('about/'))
# print(get_page('products/'))

# TASK8
# TASK9
# TASK10

# ООП - объектно-ориентированное программирование
# Отличие от функций, находится в области видимости класса

# class Person:
#     def __init__(self, name, age, sex) -> None:
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.is_run = False
#         self.is_speak = False
#         self.is_go = False


#     def speak(self):
#         if self.age > 5:
#             self.is_speak = True
#         if self.is_speak:
#             print('Speak successfully')
#         else:
#             print('I can\'t speak')

#     def go(self):
#         if self.age > 5:
#             self.is_go = True
#         if self.is_go:
#             print('Go successfully')
#         else:
#             print('I can\'t go')

#     def run(self):
#         if self.age > 5:
#             self.is_run = True
#         if self.is_run:
#             print('Run successfully')
#         else:
#             print('I can\'t run')

# person = Person(name = 'Nurka', age = 19, sex = 'female')
# person.speak()
# person.go()
# person.run()

# class Student:
#     def __init__(self, first_name, last_name) -> None:
#         self.first_name = first_name
#         self.last_name = last_name
#         self.books = []
#         self.knowledge = 0
#         self.is_ready_to_work = False
#         self.languages = {}

#     def read_book(self, book_title):
#         self.books.append(book_title)
#         self.__add_points(100)

#     def do_homework(self):
#         self.__add_points(10)

#     def do_real_world_project(self):
#         self.__add_points(50)

#     def __add_points(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             print('This student is ready to work')
#             self.is_ready_to_work = True

#     def learn_new_language(self, name_of_language, number):
#         if number < 1 or number > 100:
#             raise ValueError('Invalid number')
#         self.languages[name_of_language] = number


# st1 = Student('John', 'Connor')
# print(f'Количество баллов у {st1.first_name}: ',st1.knowledge)
# st1.read_book('Terminator1')
# st1.read_book('Чынгыз Айтматов - Первый учитель')
# st1.read_book('Jack London - Морской Волк')
# st1.read_book('Марк Лутц - Python3')
# st1.do_homework()
# st1.do_real_world_project()
# st1.do_real_world_project()
# st1.learn_new_language('Python', 10)
# print(st1.languages)
# print(f'Количество баллов у {st1.first_name}: ',st1.knowledge)

""" self - сам объект
 __init__ - инициализатор"""

# CRUD == create read update delete

# class BaseCrud:
#     def __init__(self) -> None:
#         self.data = []
#         self.id_ = 1

#     def get(self, number_id):
#         for d in self.data:
#             if d.get(number_id):
#                 return d
#         else:
#             return None
    
#     def create(self, data):
#         self.data.append({self.id_:data})
#         self.id_ += 1

#     def update(self, number_id, data: dict):
#         pass

#     def delete(self, number_id):
#         for d in self.data:
#             if d[number_id]:
#                 self.data.remove(d)

# class Book(BaseCrud):
#     pass

# book = Book()
# print('Before call method create: ', book.data)
# book.create({'name': 'Python3'})
# book.create({'name': 'Python3'})
# print('After call method create: ', book.data)
# print('Searched: ', book.get(1))

# 1:'Some book'
# 2:'Some book'

# list_ = [1, 5, 4, 10, 3]
# a = list_.sort()
# print(a)

# def sort_names(func):
#     def wrapper(list_):
#         b = sorted(list_, key = lambda x:x[2])
#         abc = []
#         for x in b:
#             if x[3] == 'M':
#                 b = (f'Mr. {x[0]} {x[1]}')
#                 abc.append(b)
#             else:
#                 c = (f'Ms. {x[0]} {x[1]}')
#                 abc.append(c)
#         return func(abc)
#     return wrapper

# @sort_names
# def prefix_name(list_):
#     return list_
    
# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),('Carrie', 'Fisher', 35, 'F'),('Harrison', 'Ford', 38, 'M')]))


# TASK9
# def get_full_number(func):
#     def wrapper(b):
#         res = []
#         for num in b:
#             if num.startswith('0'):
#                 res.append(f'+996 {num[1:4]} {num[4:]}')
#         return func(res)
#     return wrapper


# @get_full_number
# def sort_phone_nums(list_):
#     a = ''
#     nums = sorted(list_)
#     for num in nums:
#         a += num + '#'
#     b = a.rstrip('#')
#     print(b)

# sort_phone_nums(['0777987456', '0555123456', '0770369852'])
    

#TASK10
# def type_check(correct_type):
#     def wrapper(func):
#         def wrapper(x):
#             if correct_type is int and type(x) is int:
#                 func(x)
#             elif correct_type is str and type(x) is str:
#                 func(x)
#             elif correct_type is list and type(x) is list:
#                 func(x)
#             elif correct_type is dict and type(x) is dict:
#                 func(x)
#             else:
#                 print('Неверный тип данных :(')
#         return wrapper
#     return wrapper

 
# @type_check(int)
# def func1(num):
#     print(num*2)

# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})

# Наследование
# Инкапсуляция - приватные и публичные методы или атрибуты
# Инкапсуляция - объединение в единоцелое атрибутов и методов

# class A():
#     a = 12
#     def __init__(self):
#         self.hello = 'hello'

#     def set(self):
#         print('set')

# public static method
# private static method

# _ - защищенный
# __ - приватный

# Наследование
# Инкапсуляция - приватные и публичные методы или атрибуты
# Инкапсуляция - объединение в единоцелое атрибутов и методов

# class A():
#     a = 12
#     def __init__(self):
#         self.hello = 'hello'

#     def set(self):
#         print('set')

# public static method
# private static method

# _ - защищенный
# __ - приватный

# class BaseTest:

#     def equal(self, a, b):
#         return a == b

# class Test(BaseTest):
#     pass

# test = Test()
# print(dir(test))


# TASK1
# class Song:

#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year}'

# song = Song('Show must go on', 'Adele', 1990)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())

# TASK2
# class Circle:
#     color = 'синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def get_area(self):
#         res = self.pi * (self.radius ** 2)
#         return res

# circle = Circle(2)
# circle.color = 'yellow'
# print(circle.get_area())

# TASK3 
# class BankAccount:

#     def __init__(self):
#         self.balance = 0
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance}')

#     def deposit(self, amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance}')
# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

# TASK4
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
    
#     def get_total_cost(self, km):
#         res = self.cost + (self.cost_km * km)
#         return f'Такси {self.name}, стоимость поездки: {res} сом'
# taxi1 = Taxi('Namba', 79, 10)
# taxi2 = Taxi('Yandex', 37, 15)
# taxi3 = Taxi('Jorgo', 56, 13)
# print(taxi1.get_total_cost(10))
# print(taxi2.get_total_cost(6))
# print(taxi3.get_total_cost(14))

# TASK5
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name= name
#         self.last_name = last_name
#         self.phone = phone
#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}'

# contact = Phone('John', 'Snow', +996707707707)
# print(contact.get_info())

# TASK6
# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience
    
#     def count_percent(self):
#         res = self.salary * self.experience * (self.percent / 100)
#         return res

# obj = Salary(10000, 10)
# print(obj.count_percent())

# TASK7
# import datetime
# year = datetime.date.today().year
# print(year)
# TASK7
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
    
#     def get_year(self):
#         import datetime
#         year = datetime.date.today().year
#         return f'выиграл {year - self.year} лет назад'
    
# winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

# TASK8
# class Password:
#     def __init__(self, password):
#         self.password = password
    
#     def validate(self):
#         length = len(self.password)
#         if length >= 8 and length < 15:
#             pass
#         else:
#             raise Exception('Password should be longer than 8, and less than 15')
#         for x in self.password:
#             if x.isalnum():
#                 # if x.isalpha():
#                 # if self.password.isalpha():
#                 if '@#&$%! ~ *' in self.password:
#                     return 'Ваш пароль сохранен.'
#                 else:
#                     return 'Your password should have some symbols'
#                 # else:
#                 #     return 'Password should contain letters as well'
#             else:
#                 return 'Password should contain numbers too'
#         else:
#             return 'Password should be longer than 8, and less than 15'


# obj = Password('joe@123456')
# print(obj.validate())

# class MyClass: 
#      def __init__(self, name): 
#          self.name = name 

#      def __str__(self): 
#          return self.name

# obj = MyClass('первый объект') 
# print(obj)

# TASK8
# class Password:
#     def __init__(self, password):
#         self.password = password

#     def validate(self):
#         if 8 > len(self.password) or len(self.password) > 15:
#             raise Exception('Password should be longer than 8, and less than 15')
        
#         check_num = list(filter(lambda x: x.isdigit(), self.password))
#         if  len(check_num) == 0:
#             raise Exception('Password should contain numbers too')

#         check_alpha = list(filter(lambda x: x.isalpha(), self.password))
#         if len(check_alpha) == 0:
#             raise Exception('Password should contain letters as well')

#         check_symbol = list(filter(lambda x: x in '@#&$%!~*', self.password))
#         if len(check_symbol) == 0:
#             raise Exception('Your password should have some symbols')
        
#         return 'Ваш пароль сохранен.'
#     def __str__(self):
#         b = len(self.password)
#         return b * '*'

# a = Password('joe@123456')
# print(a.validate())

# TASK9
# from functools import reduce

# class Math:
#     def __init__(self, value):
#         self.value = value
    
#     def get_factorial(self):
#         list_ = [x for x in range(1, self.value + 1)]
#         res = reduce(lambda x, y: x * y, list_)
#         return res

#     def get_sum(self):
#         num = str(self.value)
#         list_ = reduce(lambda x, y: int(x) + int(y), num)
#         return list_
    
#     def get_mul_table(self):
#         res = ''
#         num = list(range(1, 11))
#         for i in num:
#             mul = self.value * i
#             res += f'{self.value} x {i} = {mul}\n'
#         return res

# m = Math(11)

# print(m.get_factorial())
# print(m.get_sum())
# print(m.get_mul_table())

# TASK 10
# class ToDo:
#     instances = {}
#     def __init__(self, task):
#         self.task = task

#     def give_priority(self, priority):
#         self.instances[priority] = self.task

#     def list_sort(self):
#         list_ = list(self.instances.items())
#         list_.sort()
#         return list_

# td1 = ToDo('сходить в кино')
# td2 = ToDo('сделать домашку')
# td3 = ToDo('выгулять собаку')
# td1.give_priority(3)
# td2.give_priority(1)
# td3.give_priority(2)
# print(td1.list_sort())

# при вызове атрибута экземпляра
# сразу после создания экземпляра класса

# class Nums:
#     def __init__(self):
#         self.a = 0
    
#     def change(self, n):
#         a = n
 
# obj = Nums()
# obj.change(2)
# print(obj.a)

# class Class1:
#     def first(self):
#         pass
#     def second(self):
#         pass

# Наследование TASK1
# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# print(obj.first())
# print(obj.second())
# print(obj.third())
# print(obj.fourth())

# TASK2
# class A:
#     def method1(self):
#         print('Основной функционал')
    
# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# TASK3
# class MyString(str):
#     def __init__(self, word):
#         self.word = word

#     def append(self, other):
#         self.word += other

#     def pop(self):
#         b = self.word
#         self.word = self.word[:-1]
#         return b[-1]

#     def __str__(self) -> str:
#         return self.word

# example = MyString('String')
# example.append('hello')
# print(example.pop())
# print(example)

# TASK4
# class MyDict(dict):
#     def get(self, key, default = 'Are you kidding?'):
#         return super().get(key, default)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some'))

# TASK5
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         return f'name:{self.name}, age:{self.age}'

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age) 
#         self.faculty = faculty
#     def display_student(self):
#         return f'name:{self.name}, age:{self.age}, faculty:{self.faculty}'

# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display()) 
# print(obj_student.display_student())

# Что такое self? Сама привязка метода к объекту - x.method(), 
# то есть в том месте где мы указываем наш объект ставим точку и вызываем метод, 
# и является тем самым self который мы указываем при создании метода.
# В self всегда хранится ссылка на наш объект, поэтому чтобы привязать метод или атрибут к объекту 
# или манипулировать объектом с помощью циклов, функций, 
# встроенных методов мы должны обращаться к нему через self.

# TASK6
# class ContactList(list):
#     def __init__(self, name):
#         self.name = name
#     def search_by_name(self, name):
#         list_ = []
#         for x in self.name:
#             if name in x:
#                 list_.append(x)
#         return list_

# all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 
# print(all_contacts.search_by_name('Olya'))

# TASK7
# class SmartPhones:
#     def __init__(self, name, color, memory, battery = 0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def __str__(self):
#         return f'{self.name} {self.memory}'

#     def charge(self, procent):
#         self.battery += procent
#         return self.battery

# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, string):
#         return f'sending {string} from {self.name} {self.memory}'

# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         from datetime import datetime
#         a = datetime.now()
#         return a.time()
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        # return current_time --> 22:12:22

# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery)

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time()) 

# Task8
# class CustomError(Exception):
#     def __init__(self, exception):
#         self.exception = exception
# capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")

# def check_letters(string):
#     if string.isupper():
#         return f'ВСЕ ОТЛИЧНО! {string}'
#     else:
#         raise capitals_error

# print(check_letters("HELLO")) 
# print(check_letters("hello"))
 
# class Parent:
#     x = 1
#     y = 2
# class Child(Parent):
#     x = 111
#     y = 222
#     def mix(self):
#         return Parent.y
# c = Child()
# print(c.mix())

# POLIMORFIZM
# TASK1
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# total = a, b, c
# for x in total:
#     print(len(x))

# TASK2
# class Dog:
#     def voice(self):
#         return 'Гав'
# class Cat:
#     def voice(self):
#         return "Мяу"

# barsik = Cat()
# rex = Dog()

# def to_pet(x):
#     if x == barsik:
#         return barsik.voice()
#     return rex.voice()

# print(to_pet(barsik)) 
# print(to_pet(rex))

# TASK3
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'{super().get_info()}, я работаю в компании {self.work} на {self.status}.'

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'{super().get_info()}, я учусь в {self.university} на должности {self.course} курсе '

# person = Person('Nurka', 'Tur')
# employee = Employee('Nurka', 'Tur', 'Google', 'Senior')
# student = Student('Nurka', 'Tur', 'DrexelU', '1')

# def get_human_info(x):
#     print(x.get_info())
    
# get_human_info(person) 
# get_human_info(employee) 
# get_human_info(student)

# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def get_area(self):
#         self.get_area()

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         res = 0.5 * self.base * self.height
#         return res

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         res = self.length * self.length
#         return res

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     from math import pi
#     def get_area(self):
#         res = self.pi * (self.radius ** 2)
#         return res

# triangle = Triangle(6, 3)
# square = Square(4)
# circle = Circle(5)
# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())

# class OS:
#     def __init__(self, version):
#         self.version = version
    
# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст {text} горячими клавишами CTRL + C'

# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст {text} горячими клавишами COMMAND + C'

# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст {text} горячими клавишами CTRL + SHIFT + C'

# win = Windows(10)
# mac = MacOS(10)
# lin = Linux(10)

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

# class OS:
#     def __init__(self, version):
#         self.version = version
# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'
# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'
# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'

# win = Windows(12)
# mac = MacOS(12)
# lin = Linux(12)
# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type
    
# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f'def {func_name}({arg}):'

#     def create_variable(self, var_name, value):
#         return f"{var_name} = {value.__repr__()}"

# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         a = '{   }'
#         return f'function {func_name}({arg}) {a};'

#     def create_variable(self, var_name, value):
#         return f"let {var_name} = {value.__repr__()};"

# py = Python(12, 'new')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# js = JavaScript(12, 'new')
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'john@123'))

# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol
    
# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f"$ {amount} равен {self.rate * amount} сомам"

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         return f"€ {amount} равен {self.rate * amount} сомам"

# dol = Dollar('USA', '$')
# eu = Euro('GB', '€')
# print(dol.exchange(100))
# print(eu.exchange(80))

# class Planet:
#     def __init__(self, name):
#         self.name = name

# TASK8
# class Mercury(Planet):
#     def __init__(self, orbit):
#         self.orbit = orbit

#     def get_age(self, earth_age):
#         a =  earth_age * 365 // self.orbit
#         return f'на Меркурии ваш возраст составляет {a} лет'

# class Venus(Planet):
#     def __init__(self, orbit):
#         self.orbit = orbit

#     def get_age(self, earth_age):
#         a =  round((earth_age * 365) * (365 / self.orbit))
#         return f'на Венере ваш возраст составляет {a} дней'

# class Jupiter(Planet):
#     def __init__(self, orbit):
#         self.orbit = orbit

#     def get_age(self, earth_age):
#         a = (earth_age * 365 // self.orbit)* (365 * 24)
#         return f'на Юпитере ваш возраст составляет {round(a)} часов'

# v = Venus(12)
# print(v.get_age(17))

# j = Jupiter(88)
# print(j.get_age(23))

# m = Mercury(225)
# print(m.get_age(32))


# Инкапсуляция
# class A:
#     def public(self):
#         return 'Public method'

#     def _protected(self):
#         return 'Protected method'

#     def __private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

# class A:
#     def method1(self):
#         return 'Hello World'
# class B(A):
#     pass
# b1 = B()
# print(b1.method1())

# class Car:
#     def __init__(self):
#         self.__speed = 0
    
#     def set_speed(self, speed):
#         self.__speed = speed
#     def show_speed(self):
#         return self.__speed

# car1 = Car() 
# # print(car1.show_speed()) 
# car1.set_speed(114) 
# print(car1.show_speed()) 

# class Car:
#     def __init__(self):
#         self.__speed = 0
    
#     @property    
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, speed):
#         self.__speed = speed

# car1 = Car() 
# print(car1.speed)
# car1.speed = 20
# print(car1.speed)

# Mixiny
# TASK1
# class Auto:
#     def ride(self):
#         return 'Riding on a ground'
# class Boat:
#     def swim(self):
#         return 'Floating on water'

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# print(obj.ride())
# print(obj.swim())

# TASK2
# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')

# class Auto(RadioMixin):
#     pass
# class Boat(RadioMixin):
#     pass
# class Amphibian(Auto, Boat, RadioMixin):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# auto.play_music('song')
# boat.play_music('bsong')
# boat.play_music('room')

# TASK3
# class Clock:
#     def current_time(self):
#         from datetime import datetime
#         now = datetime.now()
#         time = now.strftime("%H:%M:%S")
#         return time

# class Alarm:
#     def on(self):
#         return 'Будильник включен'
#     def off(self):
#         return 'Будильник выключен'

# class AlarmClock(Alarm, Clock):
#     def alarm_on(self):
#         return super().on()

# clock = AlarmClock()
# print(clock.current_time())
# print(clock.alarm_on())

# TASK4
# from abc import ABC, abstractmethod

# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass
#     @abstractmethod
#     def coding(self):
#         pass 

# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

#     def coding(self, hours):
#         self.count_code_time = hours

# class Frontend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend

#     def get_info(self):
#         return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'
    
#     def coding(self, hours):
#         self.count_code_time = hours

# class Fullstack(Backend, Frontend):
#     pass

# a = Backend('Senior', 'Ruby')
# b = Frontend('Junior', 'C++')
# c = Fullstack('Ultra mega super puper senior', 'HTML')
# a.coding(100)
# b.coding(520)
# c.coding(87946532)
# print(a.get_info())
# print(b.get_info())
# print(c.get_info())

# TASK5
# class Square:
#     def __init__(self, side):
#         self.side = side

#     def get_area(self):
#         res = self.side ** 2
#         return res

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base

#     def get_area(self):
#         res = (self.base * self.height)/2
#         return int(res)

# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         Triangle.__init__(self, height, base)
    
#     def get_volume(self):
#         res = 1/3 * self.base ** 2 * self.height
#         return res

# sq = Square(12)
# tr = Triangle(15, 12)
# py = Pyramid(12, 13)

# print(tr.get_area())
# print(sq.get_area())
# print(py.get_volume())

# '%d-%m-%Y'

"""
в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить 
задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, 
и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value 
и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
"""

# TASK6
# class CreateMixin:
#     def creat(self, todo, key):
#         if key in self.todos.keys():
#             return 'Задача под таким ключём уже существует'
#         self.todos[key] = todo
#         return self.todos
        
# class DeleteMixin:
#     def delete(self, key):
#         key.pop()
#         for key, v in ToDo.todos:
#             return f'удалили {v} задачу'

# class UpdateMixin:
#     pass

# class ReadMixin:
#     pass

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, data):
#         import datetime
#         now = datetime.datetime.now().strftime('%d/%m/%Y')
#         return now

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#     def get_area(self):
#         res = (self.base * self.height)/2
#         return int(res)
# class Square:
#     def __init__(self, side):
#         self.side = side
#     def get_area(self):
#         res = self.side ** 2
#         return res
# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         Triangle.__init__(self, height, base)
#     def get_volume(self):
#         res = 1/3 * self.base**2 * self.height
#         return res
# triangle = Triangle(15, 12)
# print(triangle.get_area())
# square = Square(15)
# print(square.get_area())
# piramid = Pyramid(12, 13)
# print(piramid.get_volume())

# Hero Task
# class Solder:
#         def __init__(self, id, team):
#                 self.id = id
#                 self.team = team
#         def go_hero(self, id):
#                 return f'Иду за героем {id}'
# class Hero:
#         level = 0
#         def level_up(self):
#                 self.level += 1
#                 return self.level
# from datetime import datetime
# now = datetime.now()
# time = now.strftime("%H:%M:%S")
# print(time)

# TASK1 -> Magic methods
# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city

#     def __repr__(self):
#         return f'{self.name} {self.balance}'

#     def __str__(self):
#         print('Счет создан')
#         return f'Hello {self.name} {self.balance} {self.city}'

#     def __del__(self):
#         print('Пока')
        
# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account))

# TASK2
# class MyNumber(int):
#     pass
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, num):
#         res = self.value + num
#         return f'Это сложение и результат равен: {res}'
#     def __sub__(self, num):
#         res = self.value - num
#         return f'Это вычитание и результат равен: {res}'
#     def __mul__(self, num):
#         res = self.value * num
#         return f'Это умножение и результат равен: {res}'
#     def __truediv__(self, num):
#         res = self.value / num
#         return f'Это деление и результат равен: {res}'
    
# obj_int = MyNumber(5)
# print(obj_int + 5)
# print(obj_int - 5)
# print(obj_int * 5)
# print(obj_int / 5)


# TASK3
# class MyList(list):
#     def __init__(self, list_):
#         self.list_ = list_
#     def __getitem__(self, index):
#         return self.list_[index - 1]

# obj_list = MyList([1,2,3,4,5])
# print(obj_list[2])

# TASK4
