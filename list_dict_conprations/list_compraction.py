numbers = [1, 2, 3, 4]
# new_list = []
# for items in numbers:
#     add_s = items+1
#     new_list.append(add_s)
# print(new_list)

# using list  comprehension
# new_list = [items + 1 for items in numbers]
# print(new_list)

# name = ['vikas', 'robo', 'rv', 'roboviku']
# letters_list = [item for item in name if len(item) < 5]
# print(letters_list)
# num_list = [i for i in range(1, 5) ]
# print(num_list)
#
# num_list = [i*2 for i in range(1, 5) if i!= 1]
# print(num_list)
name = ['vikas', 'robo', 'rv', 'robo viku', 'elon musk', 'bill gates', 'sundar pichai']
# letters_list = [item.upper() for item in name if len(item) > 5 ]
# print(letters_list)

number_of_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n*n for n in number_of_list]
# print(squared_numbers)
even_numbers = [n for n in number_of_list if n % 2 == 0]
print(even_numbers)