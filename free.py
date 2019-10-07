list1 = list(map(int, input().strip().split()))
max1 = 0
max2 = 0
max3 = 0
for i in list1:
	if i>max1:
		max3=max2
		max2=max1
		max1=i
	elif i>max2:
		max3=max2
		max2=i

	elif i>max3:
		max3=i
print(max1,max2,max3)



