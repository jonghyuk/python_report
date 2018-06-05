class Animal():
    def walk(self):
        print("걷는다")
    def eat(self):
        print("처먹는다")

class Human(Animal):
    def wave(self):
        print("손흔듬")
class Dog(Animal):
    def wag(self):
        print("꼬리를 흔듬")
person = Human()
person.walk()
person.eat()
person.wave()
dog = Dog()
dog.walk()
dog.eat()
dog.wag()