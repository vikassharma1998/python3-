# with open('weather_data.csv') as weather_data:
#     data_file = weather_data.readlines()
#     print(data_file)


# import csv
#
# with open('weather_data.csv') as weather_data:
#     data_file = csv.reader(weather_data)
#     temperatures = []
#     for row in data_file:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas
import pandas as pd
# data = pd.read_csv('weather_data.csv')
# max_temp = ()
#
# f_data = data[data.temp == data.temp.max()]
# c_data = int(f_data['temp'])
# df1 = c_data - 32 * 5/9
# df2 = c_data * 9/5 + 32
# print(df1)
# print(df2)

# data_dict = {
#     'name': ['vikas', 'viku', 'robo'],
#     'roll_no': [22, 11, 9]
#     }
# data_convert_into_csv = pandas.DataFrame(data_dict)
# data_convert_into_csv.to_csv('new_data')
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data_gray = len(data[data['Primary Fur Color'] == 'Gray'])
data_cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
data_White = len(data[data['Primary Fur Color'] == 'White'])

data_dict = {
    'For color': ['gray', 'cinnamon', 'White'],
    'Count': [data_gray, data_cinnamon, data_White]
    }

data_convert_into_csv = pandas.DataFrame(data_dict)
data_convert_into_csv.to_csv('new_data')
print(data_convert_into_csv)

