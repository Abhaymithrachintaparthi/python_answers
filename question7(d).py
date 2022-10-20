class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print_name(self):
        print(f"fullname: {self.firstname} {self.lastname}")


class Student(Person):
    def __init__(self, firstname, lastname, age, list1):
        super().__init__(firstname, lastname, age)
        self.lectures_attended = list1
        self.newly_added_list = []

    def add_class(self):
        choice = input("you want to add any lectures yes/no ")

        if choice == "yes":
            self.a = input("please enter the lectures you want to add:")
            self.lectures_attended.append(self.a)
        else:
            print("you didn't add any thing")

    def remove_list(self):
        choice = input("if you want to remove any thing from lecture list yes/no:")

        if choice == "yes":
            d = input("please enter the lectures you want to remove:")
            self.lectures_attended.remove(d)

        else:
            print("you didn't remove any thing")

    def lect_list(self):
        for i in self.lectures_attended:
            self.newly_added_list.append(i)
        print(f"Final list of lectures : {self.newly_added_list} ")


print("enter the details of student:")
firstname = input("please enter the name:")
lastname = input("please enter the surname:")
age = int(input("please enter the age:"))

list1 = list(input("enter list of lectures u r attending:").split(" "))
s = Student(firstname, lastname, age, list1)
s.print_name()
print(list1)

s.add_class()
s.remove_list()
s.lect_list()


class Professor(Person):
    def __init__(self, firstname, lastname, age, subjects_list):
        super().__init__(firstname, lastname, age)

        self.subject_teaches = subjects_list
        self.newly_added_list = []

    def add_subjects(self, new_subjects_list):
        choice = input("you want to add any subjects yes/no ")

        if choice == "yes":
            self.a = input("please enter the lectures you want to add:")

            self.subject_teaches.append(self.a)

        else:
            print("you didn't add any thing")

    def remove_list(self, new_added_list1):
        choice = input("if you want to remove any thing from lecture list yes/no:")

        if choice == "yes":
            d = input("please enter the lectures you want to remove:")
            self.subject_teaches.remove(d)
        else:
            print("you didn't remove any thing")

    def lect_list(self):
        for i in self.subject_teaches:
            self.newly_added_list.append(i)
        print(f"Final list of lectures : {self.newly_added_list} ")


print("enter the details of professor:")
firstname = input("please enter the name:")
lastname = input("please enter the surname:")
age = int(input("please enter the age:"))
subject_list = list(input("please enter the subject teaches:").split(" "))

p = Professor(firstname, lastname, age, subject_list)
p.print_name()
print(subject_list)
new_added_list = []
p.add_subjects(subject_list)
p.remove_list(new_added_list)
p.lect_list()



#output


'''enter the details of student:
please enter the name:abhay
please enter the surname:mithra
please enter the age:22
enter list of lectures u r attending:aws linux devops
fullname: abhay mithra
['aws', 'linux', 'devops']
you want to add any lectures yes/no yes
please enter the lectures you want to add:wkjq
if you want to remove any thing from lecture list yes/no:yes
please enter the lectures you want to remove:wkjq
Final list of lectures : ['aws', 'linux', 'devops'] 
enter the details of professor:
please enter the name:manoj
please enter the surname:machireddy
please enter the age:29
please enter the subject teaches:linux git docker kubernetes
fullname: manoj machireddy
['linux', 'git', 'docker', 'kubernetes']
you want to add any subjects yes/no no
you didn't add any thing
if you want to remove any thing from lecture list yes/no:no
you didn't remove any thing
Final list of lectures : ['linux', 'git', 'docker', 'kubernetes'] 
'''
