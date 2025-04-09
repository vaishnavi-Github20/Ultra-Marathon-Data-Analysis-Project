#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import pandas as pd


# In[2]:


import seaborn as sns


# In[4]:


df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv")


# In[5]:


#See the data that's been imported
df .head(10)


# In[7]:


df.shape


# In[11]:


df.dtypes


# In[ ]:


# clean up data


# In[ ]:


# Only want USA Races, 50k or 50Ml, 2020


# In[ ]:


# Step 1 show 50Mi or 50K


# In[13]:


df[df['Event distance/length'] == '50mi']


# In[15]:


# combine 50k/50mi with isin
df[df['Event distance/length'].isin(['50km','50mi'])]


# In[16]:


df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020) ]


# In[19]:


df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']


# In[24]:


df[df['Event name'] == 'Everglades 50 Mile Ultra Run (USA)']['Event name'].str.split('(').str.get(1).str.split(')').str.get(0)


# In[25]:


df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA' ]


# In[26]:


# combine all filters together


# In[29]:


df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA' ) ]


# In[31]:


df2 = df[(df['Event distance/length'].isin(['50km','50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA' ) ]


# In[32]:


df2.head(10)


# In[33]:


df2.shape


# In[ ]:


# remove usa from event name


# In[34]:


df2['Event name'].str.split('(').str.get(0)


# In[35]:


df2['Event name'] = df['Event name'].str.split('(').str.get(0)


# In[36]:


df2.head(5)


# In[37]:


# clean up atlete age


# In[39]:


df2['athlete_age'] = 2020 - df2['Athlete year of birth']


# In[ ]:


# remove h from athlete performance


# In[42]:


df2['Athlete performance'] = df['Athlete performance'].str.split('h').str.get(0)


# In[43]:


df2.head(5)


# In[ ]:


# drop columns: ahlete club, country, atlete year of birth, atlehete age category


# In[46]:


df2 = df2.drop(['Athlete club','Athlete country', 'Athlete age category', 'Athlete year of birth' ], axis = 1)


# In[48]:


df2.head()


# In[ ]:


# clean up null values


# In[50]:


df2.isna().sum()


# In[51]:


df2[df2['athlete_age'].isna()==1]


# In[52]:


df2 = df2.dropna()


# In[53]:


df2.shape


# In[ ]:


# check for dupes


# In[54]:


df2[df2.duplicated() == True]


# In[ ]:


# reset index


# In[55]:


df2.reset_index(drop = True)


# In[ ]:


# fix types


# In[56]:


df2.dtypes


# In[57]:


df2['athlete_age'] = df2['athlete_age'].astype(int)


# In[58]:


df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)


# In[59]:


df2.dtypes


# In[60]:


df2.head()


# In[ ]:


# rename columns 


# In[ ]:


# Year of event                  int64
# Event dates                   object
# Event name                    object
# Event distance/length         object
# Event number of finishers      int64
# Athlete performance           object
# Athlete gender                object
# Athlete average speed        float64
# Athlete ID                     int64
# athlete_age                    int32
# dtype: object


# In[77]:


df2 = df2.rename(columns ={ 'Year of event': 'year',
                            'Event dates': 'race_dates',
                            'Event name': 'race_name',
                            'Event distance/length': 'race_length',
                            'Event number of finishers': 'race_number_of_finishers',
                            'Athlete performance': 'athlete_performance',
                            'Athlete gender': 'athlete_gender',
                            'Athlete average speed': 'athlete_average_speed',
                            'Athlete ID': 'athlete_id',
})


# In[79]:


df2.head(1)


# In[ ]:


# reorder columns


# In[80]:


df3 = df2[['race_dates','race_name', 'race_length','race_number_of_finishers','athlete_performance','athlete_gender','athlete_average_speed','athlete_id','athlete_age']]


# In[81]:


df3.head()


# In[82]:


# find 2 races I ran in 2020 - Sarasota | Evereglades


# In[83]:


df3[df3['race_name'] == 'Everglades 50 Mile Ultra Run ']


# In[84]:


df3[df3['athlete_id'] == 222509 ]


# In[85]:


# charts and graphs


# In[86]:


sns.histplot(df3['race_length'])


# In[87]:


sns.histplot(df3, x = 'race_length', hue = 'athlete_gender')


# In[88]:


sns.displot(df3[df3['race_length'] == '50mi']['athlete_average_speed'])


# In[91]:


sns.violinplot(data = df3, x ='race_length', y = 'athlete_average_speed', hue = 'athlete_gender', split = True, inner = 'quart', linewidth = 1)


# In[97]:


sns.lmplot(data = df3, x='athlete_age', y='athlete_average_speed', hue='athlete_gender')


# In[ ]:


# questions to find out from the data


# In[ ]:


# race_dates
# race_name	
# race_length
# race_number_of_finishers
# athlete_performance	athlete_gender	
# athlete_average_speed
# athlete_id	
# athlete_age


# In[ ]:


# difference in speed for 50k, 50mi male to female


# In[98]:


df3.groupby(['race_length', 'athlete_gender'])['athlete_average_speed'].mean()


# In[ ]:


# what age group are the best in 50m race (20+ races min)


# In[105]:


df3.query('race_length == "50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean','count']).sort_values('mean', ascending = False).query('count>19').head(20)


# In[ ]:


# what age group are the worst in 50m race (10+ races min) (show 20)


# In[104]:


df3.query('race_length == "50mi"').groupby('athlete_age')['athlete_average_speed'].agg(['mean','count']).sort_values('mean', ascending = True).query('count>9').head(20)


# In[ ]:


# seasons for the data => slower in summer than winter?

# spring 3-5
# summer 6-8
# fall 9-11
# winter 12-2

# split between two decimals


# In[109]:


df3['race_month'] = df3['race_dates'].str.split('.').str.get(1).astype(int)


# In[111]:


df3['race_season'] = df3['race_month'].apply(lambda x: 'Winter' if x > 11 else 'Fall' if x > 8 else 'Summer' if x > 5 else 'Spring' if x > 2 else 'Winter')


# In[118]:


df3.head()


# In[120]:


df3.groupby('race_season')['athlete_average_speed'].agg(['mean','count']).sort_values('mean', ascending = False)


# In[ ]:


# 50 miler only


# In[123]:


df3.query('race_length == "50mi"').groupby('race_season')['athlete_average_speed'].agg(['mean','count']).sort_values('mean', ascending = False)


# In[ ]:




