import numpy
from random import *
def num(x, y) : global n; return x * n + y
def neighbors(x,y) :
	global n
	return [(x,i) for i in range(n) if i != y] + [(i,y) for i in range(n) if i != x]

def choose(r) :
	x = random()
	for i in range(len(r)) :
		x -= r[i]
		if x < 0 : return i
	print "Fail"

if __name__ == '__main__' :
	n = 8
	P = numpy.zeros((64, 64))
	for i in range(n) :
		for j in range(n) :
			for k, l in neighbors(i, j) :
				P[num(i, j)][num(k, l)] = 1.0 / 14.0
	s1, s2 = 0, 0
	N = 100000
	for i in range(N) :
		x = 0
		step = 0
		while x != 63 :
			x = choose(P[x])
			step += 1
		s1 += step
		s2 += step * step
		if (i + 1) % 1000 == 0 :
			print 1.0 * s1 / (i + 1)
			print 1.0 * s2 / (i + 1)
