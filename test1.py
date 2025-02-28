a = [1,2]
b = [3,4]
c = []

for el1, el2 in zip(a, b):
	c.append(el1+el2)

print(c)