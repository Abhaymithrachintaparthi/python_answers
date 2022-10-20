class student:
    def student_info(self, name, surname, age, lectures_attended):
        self.name=name
        self.surname=surname
        self.age=age
        self.lectures_attended=lectures_attended
    def add_class(self,newly_added_list):
        choice=input("you want to add any lectures yes/no ")
        try:
            if choice=="yes":
                print("please provide space after adding class")
                self.a=list(map(str, input("please enter the lectures you want to add:").split(" ")))
                self.newly_added_list=lectures_attended+self.a
            newly_added_list.append(self.newly_added_list)
            print(self.newly_added_list)
        except:
            print("you didn't add any thing")
    def remove_list(self,newly_added_list):
        choice = input("if you want to remove any thing from lecture list yes/no:")
        try:
            if choice == "yes":
                d = input("please enter the lectures you want to remove:")
                self.newly_added_list.remove(d)
                print("the list after removing lectures is")
                print(self.newly_added_list)
                newly_added_list=self.newly_added_list
            else:
                print("you didn't remove any thing")
        finally:
                print(f"yours  final lecture list is {self.newly_added_list}")

print("enter the details of your own:")
name=input("please enter the name:")
surname=input("please enter the surname:")
age=int(input("please enter the age:"))
print("please provide space for adding new lecture")
lectures_attended=list(map(str, input("please enter the classes attended:").split(" ")))
newly_added_list=[]
removed_list=[]
s=student()
s.student_info(name, surname, age, lectures_attended)
print(f"fullname: {name} {surname}")
print(f"attended lectures: {lectures_attended}")
s.add_class(newly_added_list)
s.remove_list(newly_added_list)
#output
'''enter the details of your own:
please enter the name:Abhaymithra
please enter the surname:Chintaparthi
please enter the age:22
please provide space for adding new lecture
please enter the classes attended:linux
fullname: Abhaymithra Chintaparthi
attended lectures: ['linux']
you want to add any lectures yes/no yes
please provide space after adding class
please enter the lectures you want to add:git kubernetes aws docker
['linux', 'git', 'kubernetes', 'aws', 'docker']
if you want to remove any thing from lecture list yes/no:yes
please enter the lectures you want to remove:aws
the list after removing lectures is
['linux', 'git', 'kubernetes', 'docker']
yours  final lecture list is ['linux', 'git', 'kubernetes', 'docker']
'''


class professsor:
    def __int__(self,name,surname,age,subject_teaches):
        self.name = name
        self.surname =surname
        self.age = age
        self.subject_teaches = subject_teaches
    def add_subjects(self):

        choice=input("do you want to add any subjects yes/no:")
        if choice=="yes":
            self.add=input("please enter the classes you want to add:")
            subject_teaches.append(self.add)
            print(subject_teaches)
        else:
            print("you didn't add any subjects")
    def remove_lectures(self):
        try:
            choice=input("do you want to remove subjects yes/no: ")
            if choice=="yes":
                self.remove=input("please enter the subjects you want to remove: ")
                subject_teaches.remove(self.remove)
                print(subject_teaches)
            else:
                print("you didn't remove anything")
        finally:
            print(f"yours final class list is: {subject_teaches}")
print("please enter the professors details")
name=input("please enter your firstname:")
surname=input("please enter your last name:")
age=int(input("please enter your age:"))
subject_teaches=list(map(str, input("please enter the subjects you teaches:").split(" ")))
print(f"yours full name is: {name} {surname}")
print(f"you teached subjects are:{subject_teaches}")
newly_added_class_list=[]
p=professsor()
p.__int__(name,surname,age,subject_teaches)
p.add_subjects()
p.remove_lectures()
#Output
'''please enter the professors details
please enter your firstname:manoj
please enter your last name:machireddy
please enter your age:29
please enter the subjects you teaches:linux docker kubernetes git aws
yours full name is: manoj machireddy
you teached subjects are:['linux', 'docker', 'kubernetes', 'git', 'aws']
do you want to add any subjects yes/no:no
you didn't add any subjects
do you want to remove subjects yes/no: yes
please enter the subjects you want to remove: aws
['linux', 'docker', 'kubernetes', 'git']
yours final class list is: ['linux', 'docker', 'kubernetes', 'git']'''




class lecture_class:
    def __int__(self,name,max_number_of_students,duration,list_professors_giving_this_lecture):
        self.name=name
        self.max_number_of_students=max_number_of_students
        self.duration=duration
        self.list_professors_giving_this_lecture=list_professors_giving_this_lecture
    def adding_professors(self):
        choice=input("if you want to add any professors yes/no:")
        if choice=="yes":
            self.add=input("please enter the professor yow want to add:")
            list_professors_giving_this_lecture.append(self.add)
        print("newly added professors list is:")
        print(list_professors_giving_this_lecture)

name=input("enter name of the class: ")
max_number_of_students=int(input("enter the maximum number of students to attend the class:"))
duration=int(input("enter the duration of the class(in minutes):"))
print("please provide space to add new professor")
list_professors_giving_this_lecture=list(map(str,input("enter the professors list of the lecture:").split(" ")))
l=lecture_class()
l.__int__(name,max_number_of_students,duration,list_professors_giving_this_lecture)
print(f"the name of the class is {name} and duration is {duration} mins")
print(f"the professors list is {list_professors_giving_this_lecture}")
l.adding_professors()
#output
'''enter name of the class: kubernets
enter the maximum number of students to attend the class:20
enter the duration of the class(in minutes):50
please provide space to add new professor
enter the professors list of the lecture:devops
the name of the class is kubernets and duration is 50 mins
the professors list is ['devops']
if you want to add any professors yes/no:yes
please enter the professor yow want to add:docker
newly added professors list is:
['devops', 'docker']'''

























