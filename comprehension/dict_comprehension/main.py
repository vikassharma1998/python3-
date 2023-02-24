
# dict = {'elon musk': ['spacex', 'tesla', 'NeuroVigil', 'DeepMind', 'X.com/PayPal'],
#         'bill gates':['apple', 'microsoft', 'sales', 'netflix', 'sap', 'ibm'],
#         }
# import random
#
# names = ['vikas', 'robo', 'rv', 'robo viku', 'elon musk', 'bill gates', 'sundar pichai']
#
# new_dict = {name: random.randint(1, 100) for name in names}
# passes_dict = {name: score for (name, score) in new_dict.items() if score >= 60}
#
# print(passes_dict)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
#
# result = {word:len(word) for word in sentence.split(" ") }
#
#
# print(result)
#
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {key: (value * 9/5) + 32 for (key, value) in weather_c.items()}
#
#
# print(weather_f)
import pandas as pd
student = {
    'name': ['vikas sharma', 'elon musk', 'bill gates'],
    'score': [56, 65, 55]
    }
for (key, value) in student.items():
    print(value)

student_dataframe = pd.DataFrame(student)
print(student_dataframe)