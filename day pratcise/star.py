# n = int(input("Enter the number of rows"))
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if i % 2 == 0:
#             print(i, end="")
#     print()
#
# odd = []
# even = []
# list =[3,6,7,8,9]
#
# for i in list:
#     if i % 2 ==0 :
#         even.append(i)
#     else:
#         odd.append(i)
# print(f" Even numbers{even}")
# print(f'Odd numbers{odd}')

for i in range(1, 6):
    for j in range(i):
        print("*", end="")

    # for k in range(5, (i - 1), -1):
    #     print(k, end="")

    print("\n")
# This is the example of print simple reversed right angle pyramid pattern
# rows = int(input("Enter the number of rows: "))

# the outer loop is executing in reversed order
# for i in range(5 + 1, 0, -1):
#     for j in range(i - 1):
#         print('*', end=' ')
#     # for l in range(j +1):
#     #     print("*", end=' ')
#     print(" ")
#
#
# rows = int(input("Enter the number of rows: "))
#
# # the outer loop is executing in reversed order
# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

# for x in range(0, 6):
#     for y in range(x+1):
#         print("*", end=' ')
#     print()
num = 5
int(input("Enter your Number: "))
for x in range(num):
    for y in range(num-x):
        print(end=' ')
    for z in range(x+1):
        print('*', end=' ')
    print()

# for x in range(num):
#     print(' '*(num-x-1)+'* '*(x+1))
# for i in range(num-1, 0, -1):
#     print(' '*(num-i)+'* '*(i))

# for x in range(num):
#     print(' '*(num-x)+'* '*(x+1))
# print(' '*(num-x)+'* '*(x+1))

# for x in range(num):
#     print(' ' * (num - x - 1) + '* ' * (x + 1))
#
# for y in range(num - 1, 0, -1):
#     print(' ' * (num - y) + '* ' * y)

# for x in range(5):
#     # for y in range(x+1):
#     #     print("*", end=' ')
#     # print()
#    print('* '*(x-5))






num = int(input("Enter your number:"))

for i in range(num):
    for j in range(i+1):
        print(end=" ")
    for k in range(j, 0, -1):
        print('*', end=" ")
    print()




















