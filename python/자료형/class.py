class Human():
    """사람"""
person1 = Human()
person2 = Human()

person1.language="한국어"
person2.language="English"
person1.name = "서울사람"
person2.name = "캐나다인"
print(person1.name)
print(person2.name)
def speak(person):
    print("{}은 {}로 말합니다,".format(person.name,person.language))
Human.speak = speak
person1.speak()
person2.speak()

