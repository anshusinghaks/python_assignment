# # a = float(input("Enter first number: "))
# # b = float(input("Enter second number: "))

# # print("Sum =", a + b)
# # print("Difference =", a - b)
# # print("Product =", a * b)
# # print("Division =", a / b)

# # radius = float(input("Enter radius of circle: "))
# # area = (3.14 * radius * radius)
# # print("Area of circle =", area)

# # length = float(input("Enter length: "))
# # width = float(input("Enter width: "))
# # area = (length * width)
# # print("Area of rectangle =", area)

# # marks1 = float(input("Enter marks of subject 1: "))
# # marks2 = float(input("Enter marks of subject 2: "))
# # marks3 = float(input("Enter marks of subject 3: "))
# # marks4 = float(input("Enter marks of subject 4: "))
# # marks5 = float(input("Enter marks of subject 5: "))
# # total = (marks1 + marks2 + marks3 + marks4 + marks5)
# # percentage =(total/500) * 100

# # print("Total Marks =", total)
# # print("Percentage =", percentage, "%")

# # bill_amount = float(input("Enter bill amount: Rs"))
# # gst = (bill_amount * 18 / 100)
# # total_amount =( bill_amount + gst)
# # print("GST (18%) = Rs", gst)
# # print("Total Bill Amount = Rs", total_amount)

# # salary = float(input("Enter salary: Rs"))
# # bonus = (salary * 10 / 100)
# # final_salary = (salary + bonus)
# # print("Bonus = Rs", bonus)
# # print("Salary after 10% bonus = Rs", final_salary)

# # total_minutes = int(input("Enter total minutes: "))
# # hours = total_minutes // 60
# # remaining_minutes = total_minutes % 60
# # print(f"time --{hours}hrs:{remaining_minutes}min") 

# # number = int(input("Enter a number: "))
# # remainder = (number % 5)
# # print("Remainder =", remainder)

# # principal = float(input("Enter principal amount: Rs"))
# # rate = float(input("Enter rate of interest: "))
# # time = float(input("Enter time in years: "))
# # simple_interest = (principal * rate * time) / 100
# # print("Simple Interest = Rs", simple_interest)

# # weight = float(input("Enter weight in kg: "))
# # height = float(input("Enter height in metres: "))
# # bmi = weight / (height * height)
# # print("BMI =", bmi)

# # basic_salary = float(input("Enter basic salary: ₹"))
# # hra = (basic_salary * 20 / 100)
# # da =(basic_salary * 10 / 100)
# # gross_salary = (basic_salary + hra + da)
# # print("\n===== SALARY REPORT =====")
# # print("Basic Salary: Rs", basic_salary)
# # print("HRA (20%): Rs", hra)
# # print("DA (10%): Rs", da)
# # print("Gross Salary: Rs", gross_salary)

# # PROJECT



# name = input("Enter your name: ")

# monthly_income = float(input("Enter monthly income: "))
# rent = float(input("Enter rent: "))
# food = float(input("Enter food expenses: "))
# travel = float(input("Enter travel expenses: "))
# entertainment = float(input("Enter entertainment expenses: "))
# other = float(input("Enter other expenses: "))

# total_expenses = rent + food + travel + entertainment + other
# remaining_money = monthly_income - total_expenses


# savings_percentage = (remaining_money / monthly_income) * 100


# print("Name:", name)
# print("Monthly Income:",(monthly_income))
# print("Total Expenses:",(total_expenses))
# print("Remaining Money:",(remaining_money))
# print("Savings Percentage:",(savings_percentage))


# module2practice question

# age =int(input("enter a age :"))

# if age >= 18:
#     print("Elligible to vote")
# else:
#     print("Not eligible to vote")    

# marks = float(input("Enter the marks :"))
# if marks >= 40:
#     print("passed")
# else:
#     print("Failed")

# year = int(input("Enter year:"))
# if (year % 400 == 0) or (year%4 == 0 and year%100 != 0):
#     print("Leap year")
# else:
#     print("Not leap year")

# year = int(input("Enter year: "))

# if ((year % 400 == 0)) or ((year % 4 == 0) and (year % 100 != 0)):

#     print("Leap year")

# else:
#     print("Not leap year")

# ch = input("Enter a character:")
# if ch == ("a" or "e" or "i" or "o" or "u"):
#     print("vowels")
# else:
#     print("consonant")

# for i in range (1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# num = int(input("enter a number:"))
# for i in  range(1,11):
#     print(num*i)

# num = int(input("Enter a number:"))
# if num%2==0:
#     print("even nuber")
# else:
#     print("odd number")

# for num1 in range(1,6):
#     for num2 in range(1,6):
#         print(num1,num2)
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# # num= int(input("enter a number"))
# # print(f"table for {num}:-")
# # for i in range (1,11):
# #     print(f"{num}x{i}={num*i}")

# # n= int(input("enter a number :"))
# # sum = 0
# # for i in range (1,n+1):
# #     if i%2==0:
# #         sum+=i
# # print("sum of even number from 1 to n is",sum)

# # num = int(input("Enter a number :"))
# # for i in range(1,11):
# #     print(num*i)
# # count = 0
# # for i in range(1,101):
# #     if i%3==0:
# #           count=count+1
# # print(count)

# correct_password = "12345"

# for i in range(5):
#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Login successful")
#         break
#     else:
#         print("Wrong password")

# else:
#     print("Account locked")


# PRACTICE QUESTION 3

# str=input("enter a string:")
# print("length=",len(str))

# str=input("enter a string:")
# print("first character=",str[0])
# print("last character=",str[-1])

# str=input("Enter a string:")
# print("reverse=",str[ : :-1])

# string = input("enter a string:")
# count= 0
# for ch in string :
#     if ch in "AEIOUaeiou":
#         count+=1
# print("numbers of vowels:",count)

# str=input("enter a string:")
# count=0
# for ch in str:
#     if ch == " ":
#         count +=1
# print("total number of spaces:",count)

# str = input("enter  a string:")
# print(str.upper())

# str = input("enter a string:")
# if  str.startswith("Py"):
#     print("strings starts with py")
# else:
#     print("string not start with Py")

# str = input("enter a string:")
# new_str = str.replace(" ","_")
# print(new_str)

# str=input("enter a string:")
# ch=input("enter a character to count:")
# count=str.count(ch)
# print("occurances:",count)

# str=input("enter a string:")
# if str==str[::-1]:
#     print("palindrome")
# else:
#     print("palindrome not")
# LIST

# list=[2,3,5,8,10]
# print(max(list))

# list=[55,23,78,24,13]
# print(min(list))

# list=[8,5,7]
# total=sum(list)
# avg= total/3
# print("sum:",total)
# print("average:",avg)

# numbers=[7,8,10,6,4]
# even= []
# odd=[]
# for num in numbers:
#      if num %2==0:
#            even.append(num)
#      else:
#            odd.append(num)
# print(even)
# print(odd)

# numbers=[5,4,6,7,9,10]
# count=0
# for num in numbers:
#     if num % 2==0:
#         count+=1
# print("even numbers=",count)

# num=[5,5,6,7,9,7,7]
# remove_duplicate=set(num)
# print(remove_duplicate)

# num=[70,70,80,90,100]
# num.sort()
# print("second largest number=",num[-2])

# num=[1,2,3,4,5]
# reverse=num[::-1]
# print("reverse list:",reverse)

# list1=[10,20,30,]
# list2=[20,30,40,10]
# common=[]
# for x in list1:
#     if x in list2:
#         common.append(x)
# print("common numbers:",common)

# list1=[1,2,3,4,5,6]
# list2=[7,8,9,10,11,12]
# merged=list1+list2
# print(merged)



#DICTIONARY
students={"name":"Anshu","age":20,"course":"B.tech"}
print(students["name"])
print(students["age"])
print(students["course"])

students["marks"]=80
print(students)
students["age"]=21
print(students)

