import random
import csv
import os
import generator
import discriminator
import pandas as pd

df = pd.read_csv('fake_data_probability.csv')
p = df.values[:,1]
fd = generator.fake_data(p)

filename = '000.csv'
with open('000.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow([" ","probability"])
	# 寫入列資料
	for i in range(399):
		writer.writerow([i+1,fd[i]])