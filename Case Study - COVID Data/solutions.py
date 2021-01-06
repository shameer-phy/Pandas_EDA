# Assignment-1         # Solutions from Shameer Khan.

# Required libraries

import pandas as pd

# Reading the Dataset
# Please insert the path to dataset in your system

df_covid = pd.read_csv("C:\\my records\\python\\Advaith\\Week 1-2\\9.Assignment - 1\\covid_19_data.csv")

'''
list(df_covid)
df_covid.head()
df_covid.describe()
'''

# 1. Calculate the average death cases of confirmed, deaths, recovered

print('Average cases confirmed:', df_covid['Confirmed'].mean(),'\n')
print('Average cases of death:', df_covid['Deaths'].mean(),'\n')
print('Average cases of recovered:', df_covid['Recovered'].mean(),'\n')

# 2. What are the maximum cases confirmed in a single day

date_groupby_table_sum = df_covid.groupby('ObservationDate').sum()['Confirmed']

max_sing_day_cases = date_groupby_table_sum[date_groupby_table_sum.max() == date_groupby_table_sum]

print('Maximum number of cases confirmed in a single day: \n',max_sing_day_cases.item(),'on',max_sing_day_cases.index[0],'\n')

# 3. Which Region contains maximum cases Confirmed on that single day? (Referring to above date)


single_day_table = df_covid[df_covid['ObservationDate'] == max_sing_day_cases.index[0]]

region_grouby_single_day = single_day_table.groupby('Country/Region').sum()['Confirmed']

print('Region with max cases on that single day: \n',region_grouby_single_day.idxmax(), 'with',region_grouby_single_day.max() )

# 4. On which Date contains maximum cases Confirmed on that single day

print('\n Date with max cases in that single day: \n',max_sing_day_cases.index[0],'\n')

# 5. Construct a table using Region variable with groupby

groupby_table = df_covid.groupby('Country/Region')

print('\n',groupby_table)

inp = input('Groupby table for Region is constructed. Its lengthy. Do you want to display it? (y/n): \n')
if inp in {'y','Y'}:
    for x,y in groupby_table:
        print(x,'\n',y)

# 6. From the overall data, which region contains maximum cases Confirmed?
'''
groupby_table.size()
type(df_covid.count())
df_covid.count()['Deaths']
'''
reg_max = groupby_table.sum()[groupby_table.sum()['Confirmed'] == groupby_table.sum()['Confirmed'].max()]['Confirmed']

print('\n Region with maximum cases: \n \n',reg_max.index[0],'has',reg_max.item(),'cases.')

# 7. Create a subset of only India from the Region column

df_india = df_covid[df_covid['Country/Region'] == 'India']

print('\n Subset of India Region: \n \n',df_india)


# 8. Total number of cases confirmed in India

print('\n Total number of confirmed cases in India: \n',df_india['Confirmed'].sum())

# 9. On which day India confirmed the maximum number of cases registered

print('\n Maximum cases were registered in India on: \n',df_india[df_india['Confirmed'].max() == df_india['Confirmed']]['ObservationDate'].item())

# 10. Calculate the percentages of death cases from total confirmed cases in India

tot_con = df_india['Confirmed'].sum()
tot_dth = df_india['Deaths'].sum()

print('\n Percentage of deaths from total confirmed cases:', (tot_dth/tot_con)*100)

####################
# The End
