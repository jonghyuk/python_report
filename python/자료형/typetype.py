s = 'Hello world'
print(type(s))#출력:<class'str'>....문자열이라는 뜻
f = 3.14
print(type(f))#출력:<class 'float'>..부동소수점
i=42
print(type(i))#출력:<class 'int'>...정수형
#42.0은 float(부동소수점)으로 나옴
print(isinstance(42,int))
print(isinstance(42,float))#42.0은 float
#isinstance 는 type이 맞는지 판독하는것