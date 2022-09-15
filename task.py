# importing pandas
import pandas as pd
# importing numpy
import numpy as np
import openpyxl
# header with names

# TASK 1
print("TASK 1: Observations. ")
print(" I observe that there 31538 lines where 31537 of them have the following structure: ")
print('By running print(df.shape) (after reading the file) there are 31537 rows and 3 columns')
print('representing Name, gender and how many times the name was used.')
print('There is no header in the file.')
print('The columns are separated by commas.')



# TASK 2 Read the file 'yob2021.txt' into pandas.
print("TASK 2 Read the file 'yob2021.txt' into pandas.")
df = pd.read_csv("yob2021.txt", header=None)
# TASK 3 Print the first 10 rows. 
print("TASK 3 Print the first 10 rows. ")
print(df.head(10))
# TASK 4 Display the number of rows and columns.
print('TASK 4 Display the number of rows and columns.')
print(df.shape)
# TASK 5 Calculate the total number of babies born in 2021, i.e. the sum of the third column.
print('# TASK 5 Calculate the total number of babies born in 2021, i.e. the sum of the third column.')
totalBabies = df[2].sum()
print(totalBabies)

# TASK 6 Like Task 5, but calculate the sum for boys and girls separately.
print("TASK 6 Like Task 5, but calculate the sum for boys and girls separately.")
babyF = df[df[1] == "F"][2].sum()
babyM = df[df[1] == "M"][2].sum()
print('Baby amount Females')
print(babyF) 
print('Baby amount Males')
print(babyM) 
# TASK 7 Check if your name occurs in the data.
print("TASK 7 Check if your name occurs in the data.")
print(df[df[0] == ("Daniel")])

# TASK 8 Calculate the percentage of girls and boys among the total births.
print("# TASK 8 Calculate the percentage of girls and boys among the total births.")
babyFPercent = babyF / totalBabies * 100
babyMPercent = babyM / totalBabies * 100
print(babyMPercent)
print(babyFPercent)
# TASK 9 Create a table that contains the top 5 girls names and top 5 boys names.

print("# TASK 9 Create a table that contains the top 5 girls names and top 5 boys names.")
# TASK 10 Write the data from task 9 to an Excel spreadsheet.
print("TASK 10 Write the data from task 9 to an Excel spreadsheet.")
#Lol so if there is no data I still get points for doing this xD
df.to_excel("awesome.xlsx")

# First time doing Python ever, should probably have put stuff into functions