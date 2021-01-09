# Analysis by Shameer Khan

import pandas as pd
import numpy as np

# Reading 3 seperate datasets

movies_data = pd.read_excel('movies.xlsx')
del movies_data['Unnamed: 0']
movies_data.head()
movies_data.dtypes
movies_data.shape

ratings_data = pd.read_excel('ratings.xlsx')
del ratings_data['Unnamed: 0']
ratings_data.head()
ratings_data.dtypes
del ratings_data['timestamp']
ratings_data.shape

user_data = pd.read_excel('users.xlsx')
user_data.head()
del user_data['Unnamed: 0']
user_data.shape

movies_data.head()
ratings_data.head()
user_data.head()

# merging the dataframes 

merge1 = pd.merge(movies_data,ratings_data,on='movie_id')
merge1.head()
merge1.shape

df = pd.merge(merge1,user_data,on='user_id')
df.head()
df.shape

# Check for blank values
df.isnull().sum()

# 1.Calculate the Each movie average rating

df.head()
df.columns

avg_rating = pd.pivot_table(df,index='title',
                            values='rating')
print('\nEach movie average rating is: \n\n', avg_rating)

# 2.Present the highest average rating movies list

top_rating = avg_rating.sort_values('rating',ascending=False)

print('\nTop 20 average rating movies: \n\n',top_rating.head(20))

# 3. Calculate the each movie rating gender wise

gender_wise = pd.pivot_table(df,index='title',
                             columns='gender',values='rating')

print('\nGender wise movie ratings: \n\n',gender_wise)

# 4. What is the most watched movie from the dataset?

df.head()
list(df)
mvi_cnt = df.groupby('title').size()
mvi_cnt.sort_values(ascending=False)
mvi_cnt.max()
mvi_cnt.idxmax()
print('\n\nThe most watched movie form the dataset:\n\n',mvi_cnt.idxmax())

# 5. What are the total number of unique movies in the dataset
# and how many of them are rated atleast 3 on average

uni_mvi = df.groupby('title').size().count()

print('\n\nTotal number of unique movies in dataset are:  ',uni_mvi)

abv3_rating = avg_rating[avg_rating['rating'] > 3]
abv3_rating['rating'].count()

print('\n\nNumber of movies with atleast 3 as average rating:  ',abv3_rating['rating'].count())

# 6. how many movies were watched only by male and how many only by female?

''' As there are no zero values in any columns, I will consider movie was
watched only female when the average male rating is not available, 
and vice-versa '''

only_male = gender_wise['F'].isnull().sum()

print('\n\nNumber of movies watched only by male:  ', only_male)

only_female = gender_wise['M'].isnull().sum()

print('\n\nNumber of movies watched only by female:  ', only_female)

# 7. What is the top 20 rated movies in the age group 20 to 25 and most watched movie for same group

age_group = df[(df['age'] >= 20) & (df['age'] <= 25)]

# age_group dataset if 20 to 25 age group subset of total dataset

age_top_rated = pd.pivot_table(age_group,index='title',values='rating').sort_values(by='rating',ascending=False).head(20)

print('\n\nTop 20 rated movies in age group 20 to 25:  \n', age_top_rated)

print('\n\nMost watched movie in 20 to 25 age group: \n',
      age_group.groupby('title').size().idxmax())

# 8. Plot a bargraph to know how the users are spread across zipcodes.

user_zip = df[['user_id', 'zip']].drop_duplicates()

zip_cnt = user_zip.groupby('zip').size()
print('\n\n',zip_cnt.shape)

#zip_cnt.plot(kind='bar',figsize=(10,15))

'''We can see that as the number of zip codes on x axis are many
the bar plot doesn't show any clear information
'''





