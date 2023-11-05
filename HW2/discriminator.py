import random
import csv
import os
import math
import generator
import pandas as pd

def switch_discriminator(p, rt, learning_rate=None, rt_accuracy=None):
	## 變數設定
	delta = []		# 計算出來的更新值
	count = 0		# 計算相同個數
	error = 0
	accuracy = 0

	## 生成fake_data
	fd = generator.fake_data(p)

	## real_test和fake_data準確率計算
	for i in range(len(fd)):
		if( fd[i] == rt[i] ):	count += 1
	accuracy = count/len(fd)
	error = abs( accuracy - rt_accuracy )

	## 更新值計算
	if( accuracy > rt_accuracy ):				# 改相同答案
		for i in range(len(fd)):
			if( fd[i] == rt[i] and generator.judge(1-error)==1 ):	p[i] = (fd[i]==1)
	elif( accuracy < rt_accuracy ):				# 改相異答案
		for i in range(len(fd)):
			if( fd[i] != rt[i] and generator.judge(1-error)==1  ):	p[i] = (fd[i]==1)

	return p,error[0]



def discriminator(p, rt, learning_rate=None, rt_accuracy=None):
	## 變數設定
	delta = []		# 計算出來的更新值
	count = 0		# 計算相同個數
	error = 0
	accuracy = 0

	## 生成fake_data
	fd = generator.fake_data(p)

	## real_test和fake_data準確率計算
	for i in range(len(fd)):
		if( fd[i] == rt[i] ):	count += 1
	accuracy = count/len(fd)
	error = abs( accuracy - rt_accuracy )
	prob = (math.log(error[0]+0.5)+0.7)			# error越小需要改的機率越小

	## 更新值計算
	for i in range(len(fd)):
		if( fd[i] == 1 ):	delta.append( learning_rate*generator.judge(prob) )	
		else:	delta.append( -learning_rate*generator.judge(prob) )
	## 機率計算
	for k in range(len(p)):
		### math.pow(4,-2*abs(p[k]-0.5)+1)：機率離0.5越近，變化越大
#		p[k] = p[k] + delta[k] * math.pow(4,-2*abs(p[k]-0.5)+1) * ( p[k]!=0 ) * ( p[k]!=1 )	 	#不可跳開
		p[k] = p[k] + delta[k] * math.pow(4,-2*abs(p[k]-0.5)+1)									#可跳開

	# 機率函數校正，讓機率大於1小於零的修正
	for i in range(len(p)):
		if(p[i]>=0.7):	p[i]=1
		elif(p[i]<=0.3):	p[i]=0

	return p,error[0]