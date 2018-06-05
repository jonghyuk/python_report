import os#os 관한 함수 모두 사용가능
print(os.getcwd())#현재 디렉토리 출력
try:
    n=os.mkdir((input("파일을 생성할 디렏토리 입력:")))#파일을 생성할 디렉토리 입력
except:
    if not os.mkdir(n):
        print("입력한 디렉토리는 존재하지 않습니다.")
