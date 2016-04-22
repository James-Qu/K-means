import numpy as np

#Needs commandline arguments for these variables
K=5
MaxIter=10
FileName="test_data.txt"
OutputFile="output.txt"

#import file
data=np.genfromtxt(FileName,dtype='float',skip_header=1)
data=data[:,1:3]
#print data

from sklearn.cluster import KMeans
km=KMeans(n_clusters=K,max_iter=MaxIter)
km.fit(data)
result=km.predict(data)
print result
print km.cluster_centers_

#create output file
output=open(OutputFile,'a')

#create a list
matrix =[]


for point in result:
    print point