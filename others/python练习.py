class Tank:
    def __init__(self, name: object, speed: object, size: object) -> object:
        self.name = name;
        self._speed = speed;
        self._size = size;

    def move(self):
        print(f'{self.name}开始移动，速度是{self._speed}')

    def __attack(self):
        print(f'{self.name}开始攻击,口径是{self._size}')


def main():
    tank = Tank('01号', 120, 220)
    tank.move()
    print(tank._size)
    print(tank._speed)

if __name__ == '__main__':
    main()


class SuperTank(Tank):
    def __init__(self,name,speed,size,good):
        super().__init__(name,speed,size)
        self.good = good

    def change(self):
         print(f'{self.name}开始变形')


#Tank('01号',120,220).move()
# super_tank = SuperTank('01号', 120, 220)
# super_tank.change()