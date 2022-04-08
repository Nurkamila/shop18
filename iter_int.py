class iter_int(int):
    def __iter__(self):
        num = self.real
        for i in str(num):
            yield int(i)

    def __getitem__(self, slice):
        i = 0
        for i, obj in enumerate(self):
            if i == slice:
                return obj

num = iter_int(55513346)
print(num[2])

# num = iter_int(5531224)
# for a in num:
#     a = iter(num)
#     print(next(a))

# for x in iter_int(123456):
#     print(x+1)