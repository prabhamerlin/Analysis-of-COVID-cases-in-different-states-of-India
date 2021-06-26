
import json
from js2py.host.jsfunctions import parseInt
from numpy import var
from pandas import DataFrame
from pymongo import MongoClient
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")

db = client['covid_db']
# statewise_tested_collection = db['statewise_tested']
covid_cases_collection = db['covid_cases']

with open('covid_cases_till_may10.json') as file:
    file_data = json.load(file)



#
# if isinstance(file_data, list):      #executed only once intially
#     covid_cases_collection.insert_many(file_data)
# else:
#     covid_cases_collection.insert_one(file_data)
#
#
# print(client.list_database_names())
# print(db.covid_cases_collection.count_documents({}))


cursor = covid_cases_collection.find()
list_cur = list(cursor)
df = DataFrame(list_cur)
pd.set_option('display.max_columns', None)
# print(df.head(50))


population_collection = db['population']
with open('Population.json') as file:
    file_data = json.load(file)



cursor = population_collection.find()   #displays population collection elements
list_cur = list(cursor)
df_population = DataFrame(list_cur)
pd.set_option('display.max_columns', None)
# print(df_population.head(50))


india_states_path = 'India_States_ADM1_GADM-shp/3e563fd0-8ea1-43eb-8db7-3cf3e23174512020330-1-layr7d.ivha.shp'
geo_df = gpd.read_file(india_states_path)


geo_df.rename(columns={'NAME_1':'State/UT'}, inplace=True)
# print(geo_df.head(50))

geo_df = geo_df.merge(df, on='State/UT')  #combine india map with covid data
geo_df = geo_df.merge(df_population, on='State/UT')  #combine india map with covid data

geo_df.rename(columns={'Active cases':'Active_cases'}, inplace=True)
geo_df['Active_cases'] = geo_df['Active_cases'].str.replace(',', '').astype('int64') #float
geo_df['Population'] = geo_df['Population'].str.replace(',', '').astype('int64')

geo_df['Active_cases'] = pd.to_numeric(geo_df['Active_cases'])
geo_df['Population'] = pd.to_numeric(geo_df['Population'])

print(geo_df.info())
geo_df['positive_density'] = geo_df.apply(lambda row: (row.Active_cases/row.Population)*100, axis = 1)
print(geo_df.head(50))

geo_df.plot(column = 'positive_density', legend = True)
plt.title("State-wise Percentage of Active Covid cases by population")
plt.show()



















# print(db.statewise_tested.find_one({}))
#
# states = db.statewise_tested.distinct('State')
# print(states)
#
#
# cursor = statewise_tested_collection.find()
# list_cur = list(cursor)
# df = DataFrame(list_cur)
# pd.set_option('display.max_columns', None)
#
#
# df.fillna(0, inplace = True) #Replace NULL values with 0
# # print(df.info())  #
#
# df['Val_Diff'] = df['Positive'] - df['Negative']
# # print(df['Val_Diff'])
# print(df.head(50))
# # print(df.groupby(['State']).Val_Diff.sum())    #

