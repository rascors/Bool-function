import numpy as np

class Bool_func():
	def __init__(self, path):
		self.path = path
		self.func = []
		self.size = 0

	def Add(self,x1, x2, x3, value):
		self.func.append([x1, x2, x3, value])
		self.size + 1

	def And(self, f):
		result = []
		if(len(f) != 8):
			return 0;
		else:
			for i in range(8):
				result.append(self.func[i][3]*f[i])
		return result

a = Bool_func('func.txt')
for i in range(8):
	if (i > 1 & i < 3) & (i > 5 & i < 8):
		x2 = 1
	else:
		x2 = 0
	x1 = i//4
	x3 = i%2
	print(str(x1) + str(x2) + str(x3))
	value = np.random.choice([0,1]) 
	a.Add(x1, x2 ,x3, value)

b = Bool_func('func.txt')
for i in range(8):
	if (i > 1 & i < 3) & (i > 5 & i < 8):
		x2 = 1
	else:
		x2 = 0
	x1 = i//4
	x3 = i%2
	print(str(x1) + str(x2) + str(x3))
	value = np.random.choice([0,1]) 
	b.Add(x1, x2 ,x3, value)
		
for i in range(8):
	print(b.func[i])

f = [1, 1, 0, 0, 1, 1, 1, 0]

result = a.And(b.func)
print(result)