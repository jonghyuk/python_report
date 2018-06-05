try:
    list = []
    print(list[0])

    text = 'abc'
    number = int(text)
except Exception as ex:#에러발생의 원인출력
    print('{}이라는 에러발생'.format(ex))