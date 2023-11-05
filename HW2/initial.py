import random
import csv
import os
import math
import generator
import discriminator
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = 'fake_data_probability.csv'
with open('fake_data_probability.csv', 'w', newline='') as csvfile:
	# 建立 CSV 檔寫入器
	writer = csv.writer(csvfile)
	writer.writerow([" ","probability"])
	# 寫入列資料
	for i in range(399):
		writer.writerow([i+1,0.5])