def rsp(mine,yours):
    allowed=['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
try:
    rsp('가위','바')#일부로 잘못된값
except ValueError:
    print("잘못된 값을 넣은것 같습니다.")

school = {'1반':[172,185,198,165],"2반":[165,177,191]}
try:
    for class_number, students in school.items():
        for student in students:
            if student>190:
                print(class_number,"190넘는애 있음")
                raise StopIteration
except StopIteration:
    print("정상종료")