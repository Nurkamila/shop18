# Mixins - Примеси
# В конце названия хранить Mixin
# PostMixin
# Не должен хранить состоянии(переменные класса, объекта)
# mixins - должен расширять класс с минимальными действиями, расширять функционал

# class CreateMixin:
#     def create(self):
#         return 'Create'

# class UpdateMixin:
#     def update(self):
#         return 'Update'

# class DeleteMixin:
#     def delete(self):
#         return 'Delete'

# class Restaurant(CreateMixin, UpdateMixin, DeleteMixin):

#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def create_restaurant(self):
#         self.create()
#         # print('Создание ресторана')
# res = Restaurant('Freshbox', 'Isanova')
# print(res.create())
# print(res.delete())
# print(res.update())

# class LoginRequiredMixin:
    # pass

# users = {
#     'user1': 123,
#     'user2': 321
# }
# def login_required(func):
#     def wrapper(user):
#         # for x in kwargs.keys()
#         if user not in users:
#             raise AuthenticationError('User is not Authenticated')
#         func(user)
#         print('Успешно авторизован')
#     return wrapper

# @login_required
# def some_page(user):
#     pass
# some_page('user2')

# from multiprocessing import AuthenticationError

# class View():
#     def __init__(self) -> None:
#         self.users = ['john', 'raychel']

#     # def dispath(self):
#     #     print('Метод диспатч')
#     #     self.users

# class LoginRequiredMixin:
#     def dispatch(self, request, user):
#         if user not in self.users:
#             raise AuthenticationError('User is not Authenticated')
#         return self.users

# class AboutPage(View, LoginRequiredMixin):
#     pass

# obj = AboutPage()
# print(obj.dispatch('test', 'john'))

# Композиция
# class Author:
#     def __init__(self) -> None:
#         self.name = 'John'

# class Restaurant:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#         self.owner = Author() -> композиция

# res = Restaurant('test', 'test')
# print(res.owner.name)

# author = Author()
# res = Restaurant('test', 'test', author) - агрегация, автор у нас теперь независимый