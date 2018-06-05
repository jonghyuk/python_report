class Human():
    '''인간'''
    def __init__(self, name,weight):
        """초기화 함수"""
        print("__init__실행")
        self.name=name
        self.weight= weight

    def __str__(self):
        """문자열과 함수"""

    def eat(self):
        person.weight += 0.1
        print("{}가 먹어서{}kg이 되었습니다".format(person.name,person.weight))
    def walk(self):
        person.weight-=0.1
        print("{}가 걸어서{}가 되었습니다".format(person.name,person.weight))
person = Human("사람",60.5)
print(person.name)
print(person.weight)