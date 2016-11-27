def LoadOneFile(filePath):
	f = file(filePath,"r")
	m = [float(x.replace(",",".")) for x in f.read().split('\n')[:-1]]
	f.close()
	return m

def LoadXYFile(filePath):
	f = file(filePath,"r")
	m = [float(x.replace(",",".")) for x in f.read().rstrip().split(' ')]
	return m[0],m[1]

def LoadFiles(x1_filePath,y1_filePath,x2_filePath,y2_filePath):
	x1 = LoadOneFile(x1_filePath)
	y1 = LoadOneFile(y1_filePath)
	x2 = LoadOneFile(x2_filePath)
	y2 = LoadOneFile(y2_filePath)
	return x1,y1,x2,y2
	
if __name__ == "__main__":
	x1,y1,x2,y2 = LoadFiles("x1","y1","x2","y2")
