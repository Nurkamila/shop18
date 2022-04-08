# class A():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         # print(self.a, self.b)

# class B(A):
#     def __init__(self, a, b, c, d):
#         # self.a = a
#         # self.b = b
#         # A.__init__(self, a, b)
#         super().__init__(a, b)
#         self.c = c
#         self.d = d
#         print(self.a, self.b, self.c, self.d)
#     pass

# b = B(12, 14, 16, 18)