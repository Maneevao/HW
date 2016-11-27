import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy
import LoadFile
import Gause

if __name__ == "__main__":
	x1,y1,x2,y2 = LoadFile.LoadFiles("x1","y1","x2","y2")
	x,y = LoadFile.LoadXYFile("xy")

	fig = plt.figure()
	for i in range(10):
		plt.scatter(x1[i],y1[i],c='b',marker="^")
		plt.scatter(x2[i],y2[i],c='g',marker="+")
	plt.scatter(x,y,c='r',marker="o")
	
	plt.savefig('Pic1.png')

#Get gause lines params
	x1_mn,x1_std = Gause.GetGauseLine(x1)
	y1_mn,y1_std = Gause.GetGauseLine(y1)
	x2_mn,x2_std = Gause.GetGauseLine(x2)
	y2_mn,y2_std = Gause.GetGauseLine(y2)

	print "$\\mu(x|H_{1}) = " + str(x1_mn) + "$\\\\"
	print "$\\sigma(x|H_{1}) = " + str(x1_std) + "$\\\\"

	print "$\\mu(y|H_{1}) = " + str(y1_mn) + "$\\\\"
	print "$\\sigma(y|H_{1}) = " + str(y1_std) + "$\\\\"

	print "$\\mu(x|H_{2}) = " + str(x2_mn) + "$\\\\"
	print "$\\sigma(x|H_{2}) = " + str(x2_std) + "$\\\\"

	print "$\\mu(y|H_{2}) = " + str(y2_mn) + "$\\\\"
	print "$\\sigma(y|H_{2}) = " + str(y2_std) + "$\\\\"

	G = Gause.GauseFunc

#Calculate
	print G(x,x1_mn,x1_std)
	print G(y,y1_mn,y1_std)
	print G(x,x2_mn,x2_std)
	print G(y,y2_mn,y2_std)

	print (G(x,x1_mn,x1_std)*G(y,y1_mn,y1_std))/ \
		(G(x,x2_mn,x2_std)*G(y,y2_mn,y2_std))

	line = numpy.linspace(0,20,100)
	plt.plot(line,5*mlab.normpdf(line,x1_mn,x1_std))
	plt.plot(5*mlab.normpdf(line,y1_mn,y1_std),line)
	plt.plot(line,5*mlab.normpdf(line,x2_mn,x2_std))
	plt.plot(5*mlab.normpdf(line,y2_mn,y2_std),line)

	plt.savefig('Pic2.png')

	plt.show()
