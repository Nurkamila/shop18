"""ООП - Объектно - ориентированное программирование (парадигма), состоящий из классов и объектов,
он легко расширяем, класс это некая форма в котором будут соответственные методы и аттрибуты"""

"""Упрощает и сокращает код"""

""" 
    Принципы ООП:
    "Основные"
    1. - Наслдеование
    1.2 - Множественное наследование
    2. - Полиморфизм
    3. - Инкапсуляция
    "Дополнительные"
    # 1. - Абстракция
    # 2. - Ассоциация
    # 2.1 - Аггрегация
    # 2.2 - Композиция
"""

# instance -> обЪект -> экземпляр класса
# self - ссылка на себя самого
# class var vs instance vs 

"""
    Наследование - принцип ООП, где мы можем в дочернем классе унаследовать, переопределять
    и использовать все методы и аттрибуты родительского класса
"""
class A:
    def method1(self):
        print('method1 in class A')

class B(A):
    """Наследование все методы и аттрибуты у класса А"""

b = B() # Создали обЪект (экземпляр) от класса B
b.method1() # Можем вызвать метод method1, который был создан в классе A

"""
    Полиморфизм - принцип ООП, где мы можем создавать в разных классах 
    одноименные методы и аттрибуты с разным функционалом
"""
class A:
    def __str__(self) -> str:
        """
            метод __str__ работает когда:
            1. мы оборачиваем объект в str -> str(A())
            2. принтим объект -> print(A())
        """
        return 'A object'

class B:
    def __str__(self) -> str:
        return 'B object'

print(A()) # 'A object'
print(B()) # 'B object'

"""
    Инкапсуляция - принцип ООП, где мы можем делать атрибуты и методы с разным уровнем доступа
"""
class A:
    attribute1 = 'публичный аттрибут'
    _attribute2 = 'защищенный аттрибут'
    __attribute3 = 'приватный аттрибут (но можно обратиться так: _A__attribute3)'

    def method1(self):
        return 'публичный метод'

    def _method2(self):
        return 'защищенный метод'

    def __method3(self):
        # self.__attribute3 -> все ок 
        return 'приватный метод (_A__method3)'

# A().__attribute3 -> AttributeError
# A()._A__attribute3 -> "приватный аттрибут (но можно обратиться так: _A__attribute3)"

"""
    Множественное наследование - принцип ООП, 
    в котором мы наследуем все аттрибуты и методы у всех родителей
"""

class A:
    def method_a(self):
        ...
class B:
    def method_b(self):
        ...

class C(A,B):
    """
        Класс унаследовал все аттрибуты и методы класса A и класса B 
        и все аттрибуты и методы их родителей (object)
    """
    ...

c = C()
c.method_a()
c.method_b()

"""Проблемы множественно наследования"""
"""
    1. - Проблема ромба(решена через mro)
    2. - Проблема перекрестного наследования (не решена)
"""
"""Проблема ромба"""
class A:
    """корневой метод"""
    def method_a(self):
        return 'A'

class B(A):
    """первый дочерний класс от А"""
    def method_b(self):
        return 'B'

class C(A):
    """первый дочерний класс от А"""
    def method_c(self):
        return 'C'

class D(B,C):
    """Дочерний класс от B и C"""
    def method_d(self):
        return 'D'

d = D()
print(d.method_a())
print(d.method_b())
print(d.method_c())
print(d.method_d())

# print(D.__mro__)
# MRO - D -> B -> C -> A

"""Проблема перекрестного наследования"""

# class A: ...
# class B: ...
# class C(A,B): ...
# class D(B,A): ...
# class E(C,D): ... -> Error

"""
    class E(C,D): ...
    TypeError: Cannot create a consistent 
"""

"""Getters and Setters"""
# это методы, через которые мы можем получать (getter) и изменять (setter) 
# значения защищенных и приватных аттрибутов

class A:
    _attr1 = 'защищенный аттрибут'
    __attr2 = 'приватный аттрибут'

    def get_attr1(self):
        """Возвращает значение аттрибута _attr1"""
        return self.get_attr1

    def get_attr2(self):
        """Возвращает значение аттрибута _attr2"""
        return self.get_attr2

    def set_attr1(self, value):
        """Меняет значение _attr1"""
        self._attr1 = value

    def set_attr2(self, value):
        """Меняет значение __attr2"""
        self.__attr2 = value

a = A()
print(a.get_attr1(), a.get_attr2())
a.set_attr1('New val')
a.set_attr2('Val')
print(a.get_attr1(), a.get_attr2())

"""
1) Напишите декоратор, который печатает перед вызовом полученной функции строку: 
"Вызываю функцию <имя_функции>". Затем следует вызов функции. 
После вызова функции должна печататься строка: "Вызов функции <имя_функции> прошёл успешно"
"""

# DRY - do not repeat yourself
# KISS - keep it simple stupid
# SOLID
# S - single responsibility

# RetrieveUpdateDeleteView