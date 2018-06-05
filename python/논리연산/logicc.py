a =10
if a < 0 and 2**a>1000and a%5==2and rouns(a)==a:
    print("복잡한식")#논리식 틀려서 출력안댐

def return_false():
    print("함수 return_false")
    return False
def return_ture():
    print("함수 return_true")
    return True
print("*************")

# print("테스트1")
# a = return_false()
# b = return_true()
# if a and b: #a는 false 임으로 else문 실행
#     print(True)
# else:
#     print(False)

print("테스트2")
if return_false() and return_true():#첫번째값이 false임으로 뒤에값은안함
    print("True")
else:
    print(False)
print("*****************")
dic = {"Key2":"Value1"}
if "Key1" in dic and dic ["Key1"]=="Value1":
    print("Key1도 있고,그값은 Value1")
else:#근데 ["Key1"]=="Value1"이랑 순서 바꾸면출력X
    print("아니네")


