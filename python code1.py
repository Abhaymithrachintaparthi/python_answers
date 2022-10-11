my_list = [1,2,2,4,4,5,6,8,10,13,22,35,52,83]
new_list=[]
new_list_2=[]
for numbers in my_list:
    if numbers>=10:
        new_list.append(numbers)
print(new_list)
n=int(input("enter a number:"))
for number in my_list:
    if number>n:
        new_list_2.append(number)
print(new_list_2)


