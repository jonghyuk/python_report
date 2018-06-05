selected = None
while selected not in ['가위','바위','보']:#조건이 맞으면 계속실행
    selected = input("가위,바위,보 중에 선택하세요")
print("선택된값은:",selected)

patterns = ['가위','보','보']
for pattern in patterns:
    print(pattern)

list = ['가위','가위','가위']
length = len(list)
i=0
while i<length:
    print(list[i])
    i=i+1
