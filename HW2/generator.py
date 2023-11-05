import random
import csv
import os
import pandas as pd

'''
######1.建立初始機率數據
filename = 'fake_data_probability.csv'
with open('fake_data_probability.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow([" ","probability"])
	# 寫入列資料
	for i in range(399):
		writer.writerow([i+1,0.5])
######2.讀取.csv機率並轉成陣列
df = pd.read_csv('fake_data_probability.csv')
p = df.values[:,1]
'''

def judge(a):
	ju = random.random() 
	if( ju > a ):
		return 1
	else: return 0

def fake_data_film(p):
	filename = 'fake_data.csv'
	with open('fake_data.csv', 'w', newline='') as csvfile:
		# 建立 CSV 檔寫入器
		writer = csv.writer(csvfile)
		writer.writerow([" ","label"])
		# 寫入列資料
		count = 0
		for i in p:
			count += 1
			writer.writerow([count,judge(i)])

def fake_data(p):
	fd = []
	for i in p:
		fd.append(judge(i))
	return fd