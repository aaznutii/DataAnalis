"""Первичная оценка данных"""

import pandas as pd

import matplotlib as mpl
import re
import csv
import numpy as np


data = pd.read_csv('games_a_copy.csv')

data.set_axis(['name', 'platform', 'year_of_release', 'genre', 'na_sales', 'eu_sales',
             'jp_sales', 'other_sales', 'critic_score', 'user_score', 'rating'],
              axis='columns', inplace=True)

new_name_col = ('name', 'platform', 'year_of_release', 'genre', 'na_sales', 'eu_sales',
                'jp_sales', 'other_sales', 'critic_score', 'user_score', 'rating')

# Пространство имен для обработки датасета по частям
games_columns = ['name', 'platform', 'year_of_release', 'genre', 'rating']
sales_columns = ['name', 'na_sales', 'eu_sales', 'jp_sales', 'other_sales']
score_columns = ['name', 'critic_score', 'user_score', 'rating']
df_games = data.loc[:, games_columns]
df_sales = data.loc[:, sales_columns]
df_score = data.loc[:, score_columns]
df_all = [df_score, df_sales, df_games]

# for dtype in ['float', 'int', 'object']:
#     selected_dtype = data.select_dtypes(include=[dtype])


def get_info(list):
    for column in list:
        print(f'Уникальных значений {column}: {len(data[column].unique())}. '
        f'Всего значений: {len(data[column])}.'
        f'Пустых значений: {data[column].isna().sum()}')
        if len(data[column].unique()) < 50:
            print(data[column].unique())


def write_df():
    data.to_csv('year_err.csv', encoding='utf-8')
# write_df()


# Убираем пустые значения name.
data.dropna(subset=['name'], inplace=True)


# Анализируем пропуски данных в столбце 'year_of_release'
games_for_req = data['name'][data['year_of_release'].isna()]
view_years_err = data.loc[:, ['name', 'year_of_release', 'genre', 'platform',
                              'na_sales', 'eu_sales', 'jp_sales', 'other_sales']]\
    .query('name in @games_for_req')\
    .sort_values('name')

"""
Значительная часть пропусков значений по годам  релиза- это дублирующие названия игр. 
Частью - год находится в столбце name.
Данные столбца необходимо привести к типу int
Исправим.
"""
# Превращение столбца года релиза в int с сохранением non как 0
data['year_of_release'] = data['year_of_release'].astype(str, errors='ignore')\
    .apply(lambda x: ''.join(re.findall(r'\d\d\d\d', x)) if re.findall(r'\d\d\d\d.\d', x) else 0)

# first_name_list = set(data.query('name in @games_for_req and year_of_release != 0')['name'])
name_good_date = data.query('name not in @games_for_req')['name']
name_with_date_1 = data.query('name in @games_for_req and year_of_release != 0')
first_list_name = [[n, y] for n, y in zip(list(name_with_date_1['name']), list(name_with_date_1['year_of_release']))]

print(len(name_good_date))


# result_list = []
# for el in first_list_name:
#     if el in result_list:
#         continue
#     else:
#         result_list.append(el)
# Получено 113 уникальных сочетаний

# for name, year in data['name', 'year_of_release'].items():
#     if name in :
#
# print(first_list_name)
# print(data['name'][data['year_of_release'].isna()])
# print(data[data.name == view_years_err.name].count())
# print(data.groupby('year_of_release')['name'].count())
# print(data['year_of_release'].isna().sum())

# data['user_score'] = pd.to_numeric(data['user_score']
#                                    .astype(str, errors='ignore'), errors='coerce', downcast='float')
#
# print(data.info(), data['year_of_release'].head(12))
# print(data['year_of_release'].value_counts())

# for name in games_for_req:
#     if re.findall(r'\d'*4, name):
#         year = int(''.join(re.findall(r'\d' * 4, name)))
#         print(f'{name}: {year}')
#         # data_copy['year_of_release']
#
# print(data_copy.info())
            # data_copy['year_of_release'] = year
# print(data_copy['year_of_release'].isna().count())
    # elif data_copy['name'] in games_for_req:



