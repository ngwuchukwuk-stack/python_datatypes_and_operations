
# import math
# from fractions import Fraction
# import random

# # name = input("Enter name: ")
# # age = int(input("Enter age: "))
# # info = f"Hello, {name} you are {age} years old"
# # print(info)

# # # print(f"Hello, {name} you are {age} years old!!!")

# # name = input("what is your name:")
# # info_about_account_number = float(input("how much do you earn monthly: "))
# # job = input ("where do you work: ")
# # # conclusion =input ("you will make it: ")
# # if job == "builder" :
# #     print ("you will make it")
# # # else:
# # #     print ("change work")
# # name = input ("Enter name:")
# # age = int(input("type your age"))
# # birthday = input ("date of birth")
# # if birthday == "13th febuary" :
# #     print("happy birthday")
# # else:
# # #     print("WELCOME")


# # name = "Enter name:"
# # print(name.find("a"))
# # # print(name[4:6]):
# # age = input =("how old are you")
# # if age =="18" :
# #     print("you are an adult")
# # else:
# # #     print("your a min

# # number = 20
# # print(30/9)
# # frtn = Fraction("3.3")
# # print(frtn)

# # rdm1 = random.randint(1,100)

# # rdm2 = random.randrange(10,100)

# # rdm3 = random.uniform(1,100)
# # rdm4 = random.choices([1,2,"for","win"],k=2)
# # print(rdm1)


# # name ="john"
# # age ="18"

# # print("my name is",name)
# # # prdoglas"
# # age ="13"
# # money ="200000"
# # print("my name is",name)
# # print("i am",age," years old")
# # print("you have",money,"in your account")
# # print(f"my name is {name} i am {age} years old i have {money} in my account")
# # word ="everybody must eat to nurish themselves"
# # print(word.find("e"))
# # print(word.count("e"))
# # print(word.capitalize())
# # print(word[3:9:2])
# # print(f"the reason i just gained {money} is because im {name}")
# # name =input ("Enter name:")
# age = input ("AGE :")
# password = input ("Input password :")
# if password =="12345":
#     print("WELCOME")int("i am",age,"years old")
# name ="
# else :
#           print(f"my name is {name} i am {age} years old ")
# name ="ken"
# age ="13"
# phone_number ="23455677"
# print(f"my name is {name} i am {age} years old this is my phone number:{phone_number}")
# name = input("NAME OF BENEFACTOR:")
# subject = input("SPECIAL SUBJECT:")
# amount_paid= int(input("AMOUNT PAID: "))
# if amount_paid =="1000":
#     print("HERE IS YOUR RECIEPT")
# else:
#     print("PURCHASE GOODS FIRST")
# name = input("Enter name :")
# age =input("Enter age :")
# password =int(input("enter keyword :"))
# if password ==12345:
#     print(f"welcome {name} to coding have fun")
# else:
#     print(f"{name} you fool your {age} years old and your jobless")
# word ="evil lurks in holes"
# print(word.isspace())
# print(word[::4])
# fruits =["orange","mango","apple"]
# fruits.extend("apple")
# print(fruits)
# student ={
#     "name":"chi",
#     "age":"16",
#     "subject":"english",
#     "score":12,
# }
# print(student.get("name"))
# print(student.keys())
# print(student.values())
# a = int(12)
# b = int(13)
# result = (a+b)
# print(f"the answer is {result}")
# list =[
#     "fruit" 
# ]
# if "fruit"  not in (list):
#     print( "not check "),
# else:
#     print("check")

# name = input("Enter name :")
# age = input("input age :")
# password = int(input("enter password :"))
# if password== 1234:
#     print(f"access granted {name}")
# else:
#     print("acsess denied")

# list=["bread", "milk" ,"meat"]
# list.insert(1,"milo")
# print(list[1:2])

# student={
#     "name":"john",
#     "age":20,
#     "course":"python"
# }
# student.pop("age")
# student["country"]="nigeria"
# print(student.keys())
# print(student.values())
# print(student.items())
book ="python"
amount =200000
alternative="javascript"
alternative_amount= 150000

need= input("which book do you want to buy: ")
money = input("how much do you have:   ")

if need == book and int(money)>= amount:
    print("book is available")
elif need != book and money < amount:
    print(" book is not available")
elif book == alternative or int(money) ==alternative_amount:
    print("we have javascript")
else:
    print("we don't have youre book")

