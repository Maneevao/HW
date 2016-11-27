def GetGauseLine(x):
	return mean(x),std(x)

def GauseFunc(x,mean,std):
	return (2.72**(-(((x-mean)**2)/(2*std**2))))/(std*pow(2*3.14,0.5))

def mean(x):
	sum = 0
	for o in x:
		sum = sum + o
	return sum/len(x)

def std(x):
	mn = mean(x)
	sum = 0
	for o in x:
		sum = sum + (o-mn)**2
	return pow((sum/10),0.5)
