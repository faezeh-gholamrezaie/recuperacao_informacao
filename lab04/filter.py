# coding: utf-8
import pandas as p
data = p.read_csv('data-set/soc-sign-bitcoinotc.csv', encoding = 'utf-8')
data_filtered = data[(data.RATING >= 8)]
data_filtered = data_filtered.drop(columns=['RATING', 'TIME'])
data_filtered.to_csv('data-set/ratings.csv', index = False)
