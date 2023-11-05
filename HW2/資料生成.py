import random
import csv
import os
import math
import generator
import discriminator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

temp = []

all_rt = pd.read_csv('analysis.csv')
for i in range(15):
	for j in range(399):
		if ( all_rt.values[j,i+1]==1 ):	temp.append(0)
		else:	temp.append(1)

filename = '777.csv'
with open('777.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow([" ","probability"])
	# 寫入列資料
	for i in range(399):
		writer.writerow([i+1,temp[i+399*0]
							,temp[i+399*1]
							,temp[i+399*2]
							,temp[i+399*3]
							,temp[i+399*4]
							,temp[i+399*5]
							,temp[i+399*6]
							,temp[i+399*7]
							,temp[i+399*8]
							,temp[i+399*9]
							,temp[i+399*10]
							,temp[i+399*11]
							,temp[i+399*12]
							,temp[i+399*13]
							,temp[i+399*14] ])
