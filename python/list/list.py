# list.index( value ) : 값을 이용하여 위치를 찾는 기능
# list.extend( [value1, value2] ) : 리스트 뒤에 값을 추가
# list.insert( index, value ) : 원하는 위치에 값을 추가
# list.sort( ) : 값을 순서대로 정렬
# list.reverse( ) : 값을 역순으로 정렬
list1 =[1,2,3,4]
list2 = [35,12,34,56,78]
print(list1+list2)
list1.extend([10]) #ㅣist1뒤에 10이라는 값 추가
list1.insert(0,999) #0번째에 999넣음
list1.insert(-1,888) #맨뒤에서 첫번째에 888넣음
print(list1)
list2.sort()
print(list2)
list2.reverse()
print(list2)



