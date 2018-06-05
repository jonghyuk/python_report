import random
def rsp():
    mine = input()
    list = ["가위","바위","보"]
    choice = random.choice(list)
    if mine == "바위" and choice == "가위":
        print("승리")
    elif mine == "가위" and choice == "보":
        print("승리")
    elif mine == "보"and choice == "바위":
        print("승리")
    elif mine =="보" and choice == "바위":
        print("패배")
    elif mine =="가위" and choice =="바위":
        print("패배")
    elif mine == "바위"and choice =="가위":
        print("패배")
    else:
        return("비김")
    print(choice)
rsp()
