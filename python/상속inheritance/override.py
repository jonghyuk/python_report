class Animal():
    def walk(self):
        print("걷는다")
    def eat(self):
        print("처먹는다")
    def greet(self):
        print("인사한다")
class Cow(Animal):
    """소소"""

class Human(Animal):
    def wave(self):
        print("손흔듬")
    def greet(self):
        self.wave()##덮어씀
class Dog(Animal):
    def wag(self):
        print("꼬리를 흔듬")
    def greet(self):
        self.wag()##덮어씀
person = Human()
person.greet()
dog =Dog()
dog.greet()
cow = Cow()
cow.greet()
