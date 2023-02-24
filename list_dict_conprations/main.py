with open('file1.txt') as file1:
   first_file = file1.readlines()

with open('file2.txt') as file2:
    secand_file = file2.readlines()


common_number = [int(num1) for num1 in first_file if num1 in secand_file ]
print(common_number)
