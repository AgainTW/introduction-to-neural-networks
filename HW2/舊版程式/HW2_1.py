import random
import csv
import os
import generator
import discriminator
import pandas as pd
import matplotlib.pyplot as plt

# 參數設定
lr = 0.01	#learning rate
error = []	#分析誤差

# 開CSV
df = pd.read_csv('fake_data_probability.csv')
all_rt = pd.read_csv('analysis.csv')

# 取值
rt1 = all_rt.values[:-1,1]
rt2 = all_rt.values[:-1,2]
rt3 = all_rt.values[:-1,3]
rt4 = all_rt.values[:-1,4]
rt5 = all_rt.values[:-1,5]
rt6 = all_rt.values[:-1,6]
rt7 = all_rt.values[:-1,7]
rt8 = all_rt.values[:-1,8]
rt9 = all_rt.values[:-1,9]
rt10 = all_rt.values[:-1,10]
rt11 = all_rt.values[:-1,11]
acc1 = all_rt.values[-1:,1]
acc2 = all_rt.values[-1:,2]
acc3 = all_rt.values[-1:,3]
acc4 = all_rt.values[-1:,4]
acc5 = all_rt.values[-1:,5]
acc6 = all_rt.values[-1:,6]
acc7 = all_rt.values[-1:,7]
acc8 = all_rt.values[-1:,8]
acc9 = all_rt.values[-1:,9]
acc10 = all_rt.values[-1:,10]
acc11 = all_rt.values[-1:,11]

# 產生假資料並生成誤差
p = df.values[:,1]

for i in range(5):	
	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt1, lr, acc1)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt2, lr, acc2)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt3, lr, acc3)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt4, lr, acc4)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt5, lr, acc5)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt6, lr, acc6)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt7, lr, acc7)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt8, lr, acc8)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt9, lr, acc9)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt10, lr, acc10)
	p = p+delta
	error.append(temp)

	fd = generator.fake_data(p)
	delta,temp = discriminator.discriminator(fd, rt11, lr, acc11)
	p = p+delta
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
plt.plot(range(11*5),error)
plt.show()

