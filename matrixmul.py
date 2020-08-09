#!/usr/bin/env python3
n = int (input('Enter the value of n:'))
print("Enter values for the matrix A")
a = []
for i in range(n):
	a.append([int(x) for x in input().split()]) 
#通过input获得用户输入的字符串，再用split分割字符串得到一系列数字字符串，然后再用int转换为对应的整数值
print("Enter values for the matrix B")
b = []
for i in range(n):
	b.append([int(x) for x in input().split()])
c = []
for i in range(n):
	c.append([a[i][j]*b[i][j] for j in range(n)])
print("After matrix mutiplication")
print('-'*7*n)
for x in c:
	for y in x:
		print(str(y).rjust(5),end=" ")
	print()
print("-"*7*n)
