import random
print(random.uniform(2,5))#실수표현
print(random.randint(2,5))#정수표현

wintable={
    '가위':'보',#가위라는 이름표,#보라는 값
    '바위':'가위',
    '보':'바위'
}
print(wintable['바위'])#대응하는 지는값


def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'
result = rsp('가위','바위')
print(result)



