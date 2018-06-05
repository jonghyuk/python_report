class Animal():
    def __init__(self,name):
        self.name = name
    def walk(self):
        print("걷는다")
    def eat(self):
        print("처먹는다")
    def greet(self):
        print("{}이인사한다".format(self.name))
class Human(Animal):
    def __init__(self, name ,hand):
        super().__init__(name)
        self.hand=hand
    def wave(self):
        print("{} 손흔들면서".format(self.hand))
    def greet(self):
        self.wave()##덮어씀
        super().greet()
person = Human("사람","오른손")
person.greet()
