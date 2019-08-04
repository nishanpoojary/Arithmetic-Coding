from collections import Counter
from collections import OrderedDict
import numpy as np
import math

inputstr = input()
print  (inputstr + "\n")

res = Counter(inputstr)
print (str(res))

#sortlist = sorted(res.iteritems(), lambda x, y : cmp(x[1], y[1]), reverse = True)
#print sortlist

#od = OrderedDict(res)
#print od

M = len(res)
#print (M)
N = 5
A = np.zeros((M,5),dtype=object)
#print (A)

#A = [[0 for i in range(N)] for j in range(M)]
#print (A)

reskeys = list(res.keys())
#print (reskeys)
resvalue = list(res.values())
totalsum = sum(resvalue)

# Creating Table
A[M-1][3] = 0
for i in range(M):
   A[i][0] = reskeys[i]
   A[i][1] = resvalue[i]
   A[i][2] = ((resvalue[i]*1.0)/totalsum)
i=0
A[M-1][4] = A[M-1][2]
while i < M-1:
   A[M-i-2][4] = A[M-i-1][4] + A[M-i-2][2]
   A[M-i-2][3] = A[M-i-1][4]
   i+=1
print (A)

# Encoding
strlist = list(inputstr)
LEnco = []
UEnco = []
LEnco.append(0)
UEnco.append(1)

for i in range(len(res)):
    #print (reskeys[i])
    result = np.where(A == reskeys[i])
    #print (A[result[0],2])
    #print (A.index(reskeys[i]))
    addtollist = (LEnco[i] + (UEnco[i] - LEnco[i])*float(A[result[0],3]))
    addtoulist = (LEnco[i] + (UEnco[i] - LEnco[i])*float(A[result[0],4]))

    LEnco.append(addtollist)
    UEnco.append(addtoulist)

    tag = (LEnco[-1] + UEnco[-1])/2.0
    print(tag)

# Decoding

ltag = 0
utag = 1
decodedSeq = []
for i in range(len(inputstr)):
    numDeco = ((tag - ltag)*1.0)/(utag - ltag)
    print(numDeco)
    for i in range(M):
        if (float(A[i,3]) < numDeco < float(A[i,4])):

            decodedSeq.append(str(A[i,0]))
            ltag = float(A[i,3])
            utag = float(A[i,4])
            tag = numDeco

#print(decodedSeq)
print("The decoded Sequence is \n ")
print("".join(decodedSeq))
