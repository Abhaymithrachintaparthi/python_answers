#calculator program
# Define our function
def calculate():
    count = 0
    decision = ""
    while decision!="exit":
        pass
        count = count+1
        operation = input('''
        Please type in the math operation you would like to complete:
        1 for addition
        2 for subtraction
        3 for multiplication
        4 for division
        enter:
        ''')
        if operation > '4':
            print("please enter the value between 0 and 4")
        else:
            try:
                number_1 = int(input('Please enter the first number: '))
                number_2 = int(input('Please enter the second number: '))
                if operation == '1':
                    print(f'{number_1} + {number_2} = ')
                    print(number_1 + number_2)
                elif operation == '2':
                    print(f'{number_1} - {number_2} = ')
                    print(number_1 - number_2)
                elif operation == '3':
                    print(f'{number_1} * {number_2} = ')
                    print(number_1 * number_2)
                elif operation == '4':
                    print(f'{number_1} / {number_2} = ')
                    print(number_1 / number_2)
            except ZeroDivisionError as e:
                print("you cannot divide a number by zero", e)
            except ValueError as e:
                print("invalid input, please enter numbers only not strings")
            decision=input("if you want to exit, please type exit or type any key to continue :")
            if decision=="exit":
                print(f"the number of calculations done by the user is {count}")
calculate()
#output:

#  Please type in the math operation you would like to complete:
#         1 for addition
#         2 for subtraction
#         3 for multiplication
#         4 for division
#         enter:
#         3
# Please enter the first number: u
# invalid input, please enter numbers only not strings
# if you want to exit, please type exit or type any key to continue :
#
#         Please type in the math operation you would like to complete:
#         1 for addition
#         2 for subtraction
#         3 for multiplication
#         4 for division
#         enter:
#         3
# Please enter the first number: 6
# Please enter the second number: 8
# 6 * 8 =
# 48
# if you want to exit, please type exit or type any key to continue :exit
# the number of calculations done by the user is 2