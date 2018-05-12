import numpy
n = 8
def num(x, y) : global n; return x * n + y
def neighbors(x,y) :
	global n
	return [(x,i) for i in range(n) if i != y] + [(i,y) for i in range(n) if i != x]

if __name__ == '__main__' :
	P = numpy.zeros((64, 64))
	for i in range(n) :
		for j in range(n) :
			for k, l in neighbors(i, j) :
				P[num(i, j)][num(k, l)] = 1.0 / 14.0
	for i in range(64) : P[63][i] = 1.0 if i == 63 else 0
	for i in range(63) : P[i][i] -= 1.0
	b1 = numpy.full(64,-1.0)
	b1[63] = 0
	E1 = numpy.linalg.solve(P, b1)
	b2 = 1.0 - 2.0 * E1
	E2 = numpy.linalg.solve(P, b2)
	print "E[T] =", E1[0], "; Var[T] =", E2[0] - E1[0]**2
