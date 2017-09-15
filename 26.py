def sal_cal(sal,lea):
	sal_pday = float(sal/30)
	d=30-lea
	return sal_pday*d

sal = float(input('enter salary'))
lea = int(input('enter no of leaves'))
print ('total salary=>', sal_cal(sal,lea))