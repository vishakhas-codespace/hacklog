# name="selene"
# age=20
# price=25.99
# print("my name is : ", name)
# print("my age is : ", age)
# age2=age
# print(age2)
# print(type(name))
# print(type(age))
# print(type(price))
# name1="sk"
# name2='sk' 
# name3='''sk'''
# print(name1)
# print(name2)
# print(name3)
# age=20
# old=False
# a=None
# print(type(old))
# print(type(a))
# a=2
# b=5
# sum=a+b
# print(sum)
# A,B=2,3
# Txt="@"
# print(2*Txt*3)
# name=input("name : ")
# age=int(input("age : "))
# price=float(input("price : "))
# print("My name is",name, "and I am",age, "years old")
# marks = int(input("marks : "))
# if(marks >= 90):
#     print("A")
# elif(marks >= 80 and marks < 90):
#     print("B")
# elif(marks >= 70 and marks < 80):
#     print("C")
# else:
#     print("D")
# length=3
# breadth=4
# Perimeter=2*(length+breadth)
# print(Perimeter)
# name = "vishakha"
# age = 21

# for i in range(1, 6):
#     print(i)

# def greet(name):
#     return "Hello " + name

# print(greet("vishakha"))   
# def add(a,b):
#     return a+b
# print(add(5,3))
# print(add(2,3))
# def square(a):
#     return a*a
# print(square(4))
# print(square(7))
# for i in range(1,6):
#     print(i)
# fruits=["mango","apple","pineapple"]
# for fruits in fruits:
#     print(fruits)
# def greet(name):
#     return "Hello" + name
# print(greet("sel"))          
# name="selene"
# age=21
# city="pune"
# print(name)
# print(age)
# print(city)          
# for i in range(1,10):
#     if i % 2 ==0:
#         print(i)
# def isPass():
#     marks = int(input("marks: "))
#     if marks >= 40:
#         print("Pass")
#     else:
#         print("Fail")

# isPass()    # call it at the bottom       
# marks = [85, 92, 78, 60, 95]
# print(max(marks))
# print(min(marks))
# print(sum(marks)/len(marks))

# student = {
#     "name": "Vishakha",
#     "age": 21,
#     "marks": 85
# }
# print(student["name"])

# foods = ["sandwich", "panipuri", "misalpav", "manchurian", "shevpuri"]
# print(len(foods))



# me = {
#     "name": "Selene",
#     "age": 21,
#     "city": "Pune",
#     "university": "Amity"
# }
# print(me["university"])     
# A = int(input("A : "))
# G = input("M/F : ")

# if(A==5 and G=="M"):
#     print("eat")
# elif(A==2 and G=="F"):
#     print("not eat")              


# s = "hello world"

# print(s.upper())         # HELLO WORLD
# print(s.lower())         # hello world
# print(s.capitalize())    # Hello world
# print(s.title())         # Hello World
# print(s.strip())         # removes spaces from both ends
# print(s.replace("world", "Vishakha"))  # hello Vishakha
# print(s.split(" "))      # ['hello', 'world']
# print(s.find("world"))   # 6 → index where found
# print(len(s))            # 11
# print(s.count("l"))      # 3
# print(s.startswith("he")) # True
# print(s.endswith("ld"))   # True
# print(" ".join(["hello", "world"]))  # hello world          

# name = "Vishakha"
# age = 21
# print(f"My name is {name} and I am {age} years old")     

print("My name is {} and I am {} years old".format(name, age))