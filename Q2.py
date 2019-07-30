chacha = [1,2,3,4,5,6,7,8,9,10]
list0 = [x+2 for x in chacha]
listchacha = [x**3 for x in chacha]
list1 = []
for x in chacha:
    if x%3 == 0:
        list1.append(x)
list2 = [x+3 for x in list1]
print(chacha)
print(list0)
print(listchacha)
print(list1)
print(list2)
        
       

