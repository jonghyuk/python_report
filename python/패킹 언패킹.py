c = (3,4)
d,e=c#c의 값을 언패킹해서 d와e에 넣음
print(d)
f = d,e
print(f)#변수de를 f에 패킹
x = 5
y=4#x와y를 바꾸려면
x,y=y,x
print(x,y)
def func():
    return 1,2
q,w= func()
print(q,w)