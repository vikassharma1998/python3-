# name = input("Enter your Name: ")
# class_held = int(input("Number of a classes Held: "))
# class_attended = int(input("Number of a classes Attended: "))
# medical = input("medical cause applicable(Y/N): ").lower()
#
# percentage = class_attended/class_held *100
# print(f"Attendence : {int(percentage)}%")
# if percentage>=75 or medical=="y":
#
#     print(f"{name} Allowed to sit in the exam")
# else:
#     print(f"{name} Not Allowed to sit in the exam")

# age = int(input("Enter your Age: "))
# sex = input("Enter your sex(Male/Female): ").lower()
# marital_status = input("You are marital(Y/N) : ").lower()
#
# if sex == "female":
#     print("she will work only in Urban areas")
# elif age >= 20 or age <= 40:
#     print("He is work anywhere")
# elif age >= 40 or age <= 60:
#     print("he will work only in Urban areas")
# else:
#     print("sorry you are not working")

# Year = int(input("Enter the year: "))
# # 1st Method
# if((Year % 400 == 0) or
#     (Year % 100 != 0) and
#     (Year % 4 == 0)):
#     print(f"{Year} Year is a leap Year")
# else:
#     print(f"{Year} Year is not a leap Year")
#
# # 2nd Method
# if Year % 400 == 0:
#     if Year % 100 != 0:
#         if Year % 4 == 0:
#             print(f"{Year} Year is a leap Year")
# else:
#     print(f"{Year} Year is not a leap Year")
# english = int(input("Enter your English Marks: "))
# math = int(input("Enter your Math Marks: "))
# science = int(input("Enter your science Marks: "))
# social_studies = int(input("Enter your social studies Marks: "))
#
#
# if english >= 80 and math >= 80 and science >= 50:
#     print("commerce Stream")
# elif english >= 80 and social_studies >= 80:
#     print("Humanities")
# elif english >= 80 and math >= 80 and science >= 80 and social_studies >= 80:
#     print("Science Stream")
# else:
#     print("not selected")
# def result(name, hours, rate):
#     try:
#         hours = int(hours)
#         rate = int(rate)
#         if hours > 40:
#             pay = (hours-40)*1.5*rate + (hours*rate)
#             print(pay)
#         else:
#             pay = hours*rate
#             print(pay)
#     except:
#         print("Error,please enter numeric value")
# name = input("Enter your name: ")
# hours = input("Enter a working Hours: ")
# rate = input("Enter a Rate: ")
# result(name, hours, rate)

# human_age = int(input("Enter a human age : "))
# dog_age = 0
# count = 0
# for i in range(human_age):
#     count += 1
#     if count <= 2:
#         dog_age += 10.5
#     else:
#         dog_age += 4
# print(f"The dog's age is {int(dog_age)}")


# first_num = int(input("Enter a first no: "))
# secand_num = int(input("Enter a first no: "))
# third_num = int(input("Enter a first no: "))
#
# if first_num > secand_num and first_num < third_num or first_num < secand_num and first_num > third_num:
#     print(first_num)
# elif first_num < secand_num and secand_num > third_num or secand_num < first_num and secand_num > third_num:
#     print(secand_num)
# else:
#     print(third_num)
# for i in range(1, 51):
#      if i % 3 == 0 and i % 5 == 0:
#           print("FizzBuzz")
#      elif  i % 5 == 0:
#           print("Buzz")
#      elif i % 3 == 0:
#           print("Fizz")
#      else:
#           print(i)


# table = int(input("Enter a number: "))
# for i in range(11):
#      print(f"{table} X {i} = {table*i}")
#
#
# num = int(input("Enter a number: "))
# result = 1
# for i in range(1, num+1):
#      result = result*i
#
# print(result)
#
#
# start = True
# number = []
# sum= 0
# while start:
#      num = input("Enter a number: ")
#      if num == "q":
#           start = False
#           for i in number:
#                sum += int(i)
#           length = len(number)
#           answer = sum/length
#           print(f"The Average number is {answer}")
#      else:
#           number.append(num)
#           print("if you want quit press q")


# for num in range(100, 500 + 1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#         if num == sum:
#             print(num)

# word = "Hello, Good, Morning.word"
# length = len(word)
# first = word.find(",", length, 1)
# print(first)

# string = "Hello,Good,Morning.World"
# word = ","
# last = string.rfind(word)
# print(last)
# first = string.find(word)
# print(first)
# result = string[first+1:last]
# print(result)

# name = input("Enter your Name: ")
# first = string.find(" ")
# print(name[first+1])
#
# first_name = input("Enter your First name: ")
# secand_name = input("Enter your Secand name: ")
# name1= sorted(first_name)
# name2= sorted(first_name)

# line = input("enter anything you want to right: ")
# width = int(input("enter width you want: "))
# name = ''
# count = 0
# for i in line:
#      name += i
#      count+=1
#      if(count!=0 and count %width==0):
#           name+="\n"
# print(name)


# wrap a string into a para
# input_string = input("Enter a string ")
# width = int (input("Enter the width of the paragraph "))
# counter = 0
# output_string =''
# for letter in input_string:
#     output_string = output_string+letter
#     counter += 1
#     if(counter!=0 and counter %width==0):
#         output_string += '\n'
# print(output_string)

# list = 'abcdefghijklmnopqrstuvwxyz'
# word = input("enter anything you want to right: ")
# input_number = int(input("enter width you want: "))
# answer = ""
# for i in word:
#      postion = list.find(i)
#      answer += list[postion-input_number]
# print(answer)

# #Caesar encryption
# text= input("Enter Plain Text: ")
# encrypted_text=''
# for letter in text:
#     encrypted_text+=chr(ord(letter)-3)
# print(encrypted_text)

word = input("Enter your words: ")
names= word.split()
print(names)