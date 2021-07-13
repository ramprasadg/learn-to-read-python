x_0 = 0
x_1 = 10
x_2 = 20
x_3 = 30

print x_0
print x_1
print x_2
print x_3

print ""

x_list = [11,22,44,33]

print len(x_list)

print ""


print x_list[0]
print x_list[1]
print x_list[2]
print x_list[3]

print ""

for x in x_list:
	print x


print ""

for x in x_list:
	if x % 2 == 0:
		print x

print ""

largest_so_far = x_list[0]
for x in x_list:
	print x
	if x > largest_so_far:
		largest_so_far = x
print largest_so_far

print ""
