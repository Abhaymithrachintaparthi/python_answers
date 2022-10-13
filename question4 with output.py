employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]
name_age=[]
n = len(employees)
for i in range(n):
    a={"name":employees[i]["name"], "age":employees[i]["age"]}
    name_age.append(a)
print(name_age)
def min_age(name_age):
    return name_age.get("age")
name_age.sort(key=min_age)
print("the minimum age employee is:")
print({name_age[0]['name']: name_age[0]['age']})
#output:
'''[{'name': 'Tina', 'age': 30}, {'name': 'Tim', 'age': 35}]
the minimum age employee is:
{'Tina': 30}'''



# function that accepts a string and calculates the number of upper case letters and lower case letters.
def string():
    user_input = input("enter a string:")
    lower = 0
    upper = 0
    for i in user_input:
        if i.islower():
            lower=lower+1
        elif i.isupper():
            upper=upper+1
    print(f"the lower cases in given string is:{lower}")
    print(f"the upper cases in given string is:{upper}")
string()
#OUTPUT
'''enter a string:hdGHJSJ
the lower cases in given string is:2
the upper cases in given string is:5'''


#Write a function that prints the even numbers from a provided list
def even():
    print("please give space after entering a number")
    user_input=list(map(int, input("please enter numbers:").split(" ")))
    print(user_input)
    even_list=[]
    for i in user_input:
        if i % 2 == 0:
            even_list.append(i)
    print("the even list is:")
    print(even_list)
even()

#output
'''please give space after entering a number
please enter numbers:3 4 6 7 8 393 02 47 48 9 26
[3, 4, 6, 7, 8, 393, 2, 47, 48, 9, 26]
the even list are:
[4, 6, 8, 2, 48, 26]'''







