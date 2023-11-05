import random
import csv
import os
import math
import generator
import discriminator
import generator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 開CSV並取值
all_rt = pd.read_csv('analysis.csv')
p1 = all_rt.values[:-1,39]	#0.78595
p2 = all_rt.values[:-1,42]	#0.79933
p3 = all_rt.values[:-1,43]	#0.03344

count = []
c = 0
for i in range(399):
	if(p2[i]==p3[i]):	
		count.append(1)
		c+=1
	else:	count.append(0)
print(c)


predict = []
for i in range(399):
	if(count[i]==1):	predict.append( p2[i] )
	else:	predict.append(generator.judge(0.5)) 

print(predict)

'''
# 儲存資料
filename = 'predict_11.csv'
with open('predict_11.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow(["data_id","label"])
	# 寫入列資料
	for i in range(399):
		writer.writerow([i+1,predict[i]])
'''