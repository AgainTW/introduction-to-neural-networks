import random
import csv
import os
import math
import generator
import discriminator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 參數設定
lr = 0.1	#learning rate
error = []	#分析誤差
rt = []		#處存資料
acc = []
index = [35,36,37]

# 開CSV並取值
df = pd.read_csv('fake_data_probability.csv')
all_rt = pd.read_csv('analysis.csv')
p = df.values[:,1]

# 產生假資料並生成誤差
for turn in range(3):					# 總共跑幾輪
	for i in range(3):					# 幾個rt在輪
		# 選擇要隨機訓練還是固定訓練
#		num = random.randint(0,2)
		num = index[i]
		for j in range(20):			# 每個rt訓練幾次			
			delta,temp = discriminator.switch_discriminator(p, all_rt.values[:-1,num+1], lr, all_rt.values[-1:,num+1])
			error.append(temp)

# 儲存資料
filename = 'fake_data_probability.csv'
with open('fake_data_probability.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow([" ","probability"])
	# 寫入列資料
	for i in range(399):
		writer.writerow([i+1,p[i]])

print(p)

# 繪製誤差圖
plt.plot(range(len(error)),error)
plt.show()

