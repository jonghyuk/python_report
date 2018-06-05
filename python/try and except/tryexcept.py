text ='100%'
try:
    number = int(text)
except ValueError:#에러발생후 별도 처리
    print("{}는 문자가아니네요".format(text))
def safe(list,index):
    try:#if (index<len(list))
        print(list.pop(index))
    except IndexError:#else
        print('{}index의 값을 가져올수 없습니다.'.format(index))
safe([1,2,3],5)

try:
    import my_module
except ImportError:
    print("모듈이 없습니다.")



