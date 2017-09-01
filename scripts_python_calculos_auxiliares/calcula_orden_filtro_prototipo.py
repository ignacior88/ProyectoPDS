from math import *

def calculaOrdenEC1(fc, fa):
	wc = 2*pi*fc
	wa = 2*pi*fa
	
	print("wc: ", wc)
	print("wa: ", wa)
	for atenuacion in range(4, 81, 1):
		n = 0.5 * (log10(pow(10,(atenuacion/10)) - 1) / log10(wa/wc))
		print("Para una Atenuacion de %ddb ---> orden N = %f" %(atenuacion, n))


print("FORMULA 1 de PDS")
calculaOrdenEC1(83.407, 86.307)
#calculaOrdenEC1(83.4, 87.3)
print("\n\n")

#84.05514
#85.70328
