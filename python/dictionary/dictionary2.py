list=[1,2,3,4,5]
list.append(6)
list[1]=22 #값 수정
del(list[3])#3번째값 4를삭제
print(list.pop(1))
#0번째다음 1번째있는걸
#  22를 리턴하고 삭제함
print(list)

dict = {'one':1,'two':2,'four':4,'five':55}
dict['one']=11#값을 수정시키기
dict['three']=3#값 추가하기
del(dict['four'])#four 사라짐
print(dict.pop('five'))#five를리턴하고 삭제
print(dict)
