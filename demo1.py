print('hello world')
print('hello hello')
list1 = [1, 2, 3, 4, 5, 6]
for i in list1:
    print('---->', i)


class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print('名字是:', self.name)

    def __str__(self):
        return self.name
