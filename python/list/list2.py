#list = str.split() 문자열에서 리스트로
#"Hello world".join(list)리스트에서 문자열으로
word = "아 집에 가고싶다"
word = word.split()
print(word) #문자열에서 리스트로

characters = list("abcdef")
print(characters)#각글자가 들어있는 리스트


time_str = "10:35:27"
time_list = time_str.split(":")#자르는 기준이 :콜론
time_list = ":".join(time_list)#리스트에서 문자열
print(time_list)
