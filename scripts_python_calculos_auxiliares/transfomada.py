from math import *

def gz(alfa,k):
	a=(k-1)/(k+1)
	b= 2*alfa*(k/(k+1))

	print("\t%f - %f z^-1 + z^-2" %(a,b))
	print("   -  ---------------------------------------")
	print("\t1 - %f z^-1 + %f z^-2" %(b,a))

def alfa(wc, fs):
	a = cos(wc/fs)
	print("alfa = ", a)
	return a

def k(w2,w1,b,fs):
	k = 1/(tan((w2-w1)/(2*fs))) * tan(b/(2*fs))
	print("K = ", k)
	return k


a = alfa(517.778, 400)
k = k(524.061, 511.495, 524.061, 400)
print()
gz(a,k)
