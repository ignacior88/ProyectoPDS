from math import *

def calcula_coeficientes_del_filtro(c1, p1, c2, p2, c3, p3):
	b0 = 1
	b1 = -(c1+c2+c3)
	b2 = p2+c1*c2+p1+p3+(c1+c2)*c3
	b3 = -(c1*p2+p1*c2+p2*c3+c1*c2*c3+p1*c3+c1*p3+c2*p3)
	b4 = p1*p2+c1*p2*c3+p1*c2*c3+p2*p3+c1*c2*p3+p1*p3
	b5 = -(p1*p2*c3+c1*p2*p3+p1*c2*p3)
	b6 = p1*p2*p3

	print("b0 = ", b0)
	print("b1 = ", b1)
	print("b2 = ", b2)
	print("b3 = ", b3)
	print("b4 = ", b4)
	print("b5 = ", b5)
	print("b6 = ", b6)


c1 = 0.206148 * 2
c2 = 0.153100 * 2
c3 = 0.133296 * 2
p1 = pow(0.774533, 2)
p2 = pow(0.433816, 2)
p3 = pow(0.185741, 2)

calcula_coeficientes_del_filtro(c1, p1, c2, p2, c3, p3)