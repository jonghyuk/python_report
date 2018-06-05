age ={"Tod":35,"Jane":23,"Faul":64}

for key in age.keys():
    print(key)
for value in age.values():
    print(value)
for key, value in ages.items():
    print('{}의 나이는 {} 입니다'.format(key, value))

def check_and_clear(box):
    if "불량품" in box.keys():
        box.clear()
        print("불량품이 있으면 box를 clear합니다.")
    else:
        print(box.keys())

# products.update(catalog)
# print(products)리스트와 비교실습2