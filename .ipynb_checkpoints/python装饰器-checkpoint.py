class  Person:
    #__slots__ = ('x')

    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        self._name = name

    @staticmethod
    def test():
        print(1)

if __name__ == '__main__':
    person = Person('张山', 23)
    person.age = 21
    person.test()
    print(person.name,person.age)

