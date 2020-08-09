#!/usr/bin/env python3
n = int(input("Enter the number of students:"))
data = {} #用来存储数据的字典变量
subjects = ('Physics','Maths','History')# 科目
for i in range(0,n):
	name = input('Enter the name of the student{}:'.format(i+1)) #获得第i+1名学生的名字
	marks = []
	for x in subjects:
		marks.append(int(input('Enter marks of{}:'.format(x))))#获得每一科的分数
		data[name] = marks
for x,y in data.items():
	total = sum(y)
	print("{}'s total marks {}".format(x,total))
	if total <120:
		print(x,"failed :(")
	else:
		print(x,"passed :)")
