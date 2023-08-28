#!/usr/bin/env python
# coding: utf-8

# # Spotify Streaming Pattern Analysis
# 
# Author: Arun Ganapathy <br>
# Dated: 9th December 2022
# 
# In this project, we aim to analyze Billboard chart data and Spotify track information to gain insights into popular music trends. The project involves the following key steps:
# 
# 1. **Data Collection**: We retrieve historical Billboard chart data for pop songs from 2008 to 2021. This data includes details about artists, track titles, and years of charting.
# 
# 2. **Data Cleaning and Transformation**: We preprocess the collected data by cleaning it, converting data types, and handling any discrepancies.
# 
# 3. **Exploratory Analysis**: We explore the dataset to identify patterns, trends, and interesting insights related to artists, genres, and charting over the years.
# 
# 4. **Genre Correction**: We correct and standardize the genre information using text processing techniques.
# 
# 5. **Integration with Spotify Data**: We integrate Spotify track information with the Billboard data to enhance our analysis. This includes identifying popular artists and tracks based on Spotify metrics.
# 
# 6. **Data Export**: After processing and analyzing the data, we export the final dataset to a CSV file for further use.
# 
# Through this project, we aim to uncover how music popularity has evolved over the years, identify dominant genres, and highlight noteworthy artists and tracks within the given time frame.
# 

# In[1]:


import billboard
import pandas as pd
from tqdm import tqdm


# In[2]:


# Specify the chart type ('pop-songs') and the year (2008) for the ChartData.
# This will retrieve Billboard chart data for the specified year and chart type.
chart = billboard.ChartData('pop-songs', year=2008)


# In[3]:


# Create an empty DataFrame called 'df'.
df = pd.DataFrame()

# Add two empty columns 'Artist' and 'Title' to the DataFrame.
df[['Artist', 'Title']] = ""

# Add a new column 'Year' with default value 0 to the DataFrame.
df['Year'] = 0


# In[4]:


# Loop through years from 2008 to 2021 (inclusive).
for i in tqdm(range(2008, 2022)):
    # Retrieve Billboard chart data for 'pop-songs' chart and the current year (i).
    chart = billboard.ChartData('pop-songs', year=i)
    
    # Loop through the entries in the current year's chart.
    for j in range(len(chart)):
        # Append a new row to the DataFrame 'df' with artist, title, and year information.
        df.loc[len(df)] = [chart.entries[j].artist, chart.entries[j].title, i]


# In[5]:


# Export the DataFrame 'df' to a CSV file named 'billboard_08_21.csv'. # this billboard data is later used during visual development
df.to_csv('data/billboard_08_21.csv')


# ## Data Cleaning

# In[6]:


# Read in Spotify data for cleaning
data = pd.read_csv('data/final_data.csv')
data.head()


# In[7]:


# Converting specific columns in the 'data' DataFrame to string data type.
# This ensures consistent data type for 'track_name', 'genre', and 'artist_name' columns.
data = data.astype({"track_name": str, "genre": str, "artist_name": str})


# In[8]:


# Filtering out rows in the 'data' DataFrame where the 'track_name' column contains "?".
# The tilde (~) operator is used to negate the condition, keeping only rows without "?".
data = data[~data.track_name.str.contains("?", regex=False)]


# In[9]:


# Grouping the 'data' DataFrame by unique combinations of 'track_name' and 'artist_name'.
# The 'first()' function is applied to each group, retaining the first occurrence within each group.
# Finally, the 'reset_index()' function is used to reset the index and create a new DataFrame.
data = data.groupby(['track_name', 'artist_name']).first().reset_index()


# In[10]:


# Filtering the 'data' DataFrame to select rows where the 'artist_name' column is 'Cardi B'.
cardi_b_data = data[data.artist_name == 'Cardi B']
cardi_b_data.head()


# In[11]:


# Replacing occurrences of 'Children’s Music' with 'Children's Music' in the 'genre' column of the 'data' DataFrame.
data.genre = data.genre.str.replace('Children’s Music', "Children's Music")


# In[12]:


# Importing the 're' module for working with regular expressions.
import re

# Looping through each row in the 'data' DataFrame using the 'iterrows()' function.
for i, row in data.iterrows():
    # Checking if the 'genre' column in the current row is equal to 'Reggae'.
    if data.loc[i, 'genre'] == 'Reggae':
        # Replacing the 'genre' value with 'Reggaeton' for the current row.
        data.loc[i, 'genre'] = 'Reggaeton'


# In[13]:


print(set(data.genre))


# In[14]:


data.head(5)


# In[15]:


# Exporting the 'data' DataFrame to a CSV file named 'spotify_data.csv'.
# The 'index' parameter is set to False to exclude the index column from the CSV.
data.to_csv('data/spotify_data.csv', index=False)


# ### End of data processing
