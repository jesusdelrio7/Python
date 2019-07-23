f=open("punto1.csv")

def divideData (x):
    return x.split(sep=",")

def setNumericData(x):
    for i in range(0,len(x)):
        x=x[i].replace(",",".")
        return x

    
data=(f.read().split(sep="\n"))
f.close() 
data=list(map(divideData,data))

data=list(map(setNumericData,data))
         
    
print(data)
