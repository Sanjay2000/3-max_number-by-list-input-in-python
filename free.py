# user = int(input("enter the number"))

# for j in range(1,user+1):
# 	if user%j == 0:
# 		print9J





# numbers = [
# [1,2,3,7,8,9,10],
# [56,43,21,89,76],
# [45,78,90,21,56,78],
# [24,56,8900,9,10,11],
# [100, 123, 567]
# ]
# s=[]
# l=0
# c=0
# for i in range(len(numbers)):
# 	x=0
# 	for j in numbers[i]:
# 		x+=j
# 	s.append(x)
# 	if l<x:
# 		l=x
# for k in s:
# 	if(l==k):
# 		break
# 	c+=1
# print(numbers[c])

# s="sanjay"
# d=s[::-1]
# print(d)

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



