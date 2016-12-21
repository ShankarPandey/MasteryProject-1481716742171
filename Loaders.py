'''
Program to read Data from the files
'''
import numpy as np

def readFile(filename, mode = False):
	f = open(filename,'r')
	data = []
	labels = []
	for eachLine in f:
		eachLine =eachLine.strip()
		if(len(eachLine) == 0 or eachLine.startswith("#")):
			continue
		linedata = eachLine.split(",")
		# print linedata
		if( mode == True):
			data.append([1,float(linedata[0]),float(linedata[1]), float(linedata[2]), float(linedata[3]), float(linedata[4])])
		else:
			data.append([float(linedata[0]),float(linedata[1]), float(linedata[2]), float(linedata[3]), float(linedata[4])])
		labels.append(int(linedata[5]))
	data = np.array(data)
	labels = np.array(labels)
	return data, labels