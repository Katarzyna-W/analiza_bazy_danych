"""
Created on Sat Oct 16 17:30:00 2021

@author: katarzyna watorska
"""

import csv
import pandas as pd

drinks_file = open('C:/Users/katar/my_env/TIER/Original_data/drinks.csv')
csvreader = csv.reader(drinks_file)
header = next(csvreader)
print(header)
#create a list of the data set
rows = []
for row in csvreader:
    rows.append(row)
    
#convert all country names to lowercase
for i in range(len(rows)):
    rows[i][0] = rows[i][0].lower()
    
#remove duplicates

b = sorted(rows, key=lambda x: x[0])
c = { x[0] : x[1:len(x)] for x in b }

result = [[n] + c[n] for n in c]

#convert country names to uppercase
for i in range(len(result)):
    result[i][0] = result[i][0].capitalize()

result.sort()
#print(result)

#remove entries with None or NaN
for each in result:
    if pd.isna(any(each)) or pd.isnull(any(each)):
        result.remove(each)
        

#remove an entry if its first column does not contain a string
#second, third and fourth column is not an int, fifth is not a float
# =============================================================================
# for each in result:
#     res1 = isinstance(each[0], str)
#     res2 = isinstance(each[1], int)
#     print(type(each[3]))
#     res3 = isinstance(each[2], int)
#     res4 = isinstance(each[3], int)
#     res5 = isinstance(each[4], float)
#     if res1 is False or res2 is False or res3 is False or res4 is False or res5 is False:
#         result.remove(each)
# print(result)
# =============================================================================

result.sort(key = lambda x: x[0])
countries = result
#print(countries)

#export data to a file
# open the file in the write mode
f = open('C:/Users/katar/my_env/TIER/Analysis_data/data_sorted_by_countries_alphabetically.csv', 'w', newline='')

# create the csv writer
writer = csv.writer(f)

# write rows to the csv file
writer.writerow(header)
writer.writerows(countries)

# close the file
f.close()


#sort data starting from the highest consumption of alcohol
result.sort(key=lambda x: (x[1]), reverse = True)
highest_beer_consumption = result
f = open('C:/Users/katar/my_env/TIER/Analysis_data/data_sorted_by_highest_beer_consumption.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
writer.writerows(highest_beer_consumption)
f.close()


result.sort(key=lambda x: (x[2]), reverse = True)
highest_spirit_consumption = result
f = open('C:/Users/katar/my_env/TIER/Analysis_data/data_sorted_by_highest_spirit_consumption.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
writer.writerows(highest_spirit_consumption)
f.close()


result.sort(key=lambda x: (x[3]), reverse = True)
highest_wine_consumption = result
f = open('C:/Users/katar/my_env/TIER/Analysis_data/data_sorted_by_highest_wine_consumption.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
writer.writerows(highest_wine_consumption)
f.close()


result.sort(key=lambda x: (x[4]), reverse = True)
highest_pure_alcohol_consumption = result
f = open('C:/Users/katar/my_env/TIER/Analysis_data/data_sorted_by_highest_pure_alcohol_consumption.csv', 'w', newline='')
writer = csv.writer(f)
writer.writerow(header)
writer.writerows(highest_pure_alcohol_consumption)
f.close()


drinks_file.close()
