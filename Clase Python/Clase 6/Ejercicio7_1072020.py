import random



variables=["1","2","3","4","5","6","A","B","C","D","E","F"]

switch1=False

if (switch1==True):
    f =open("./Ejercicio7.csv","w")
    for i in range (0,1000):
        num=random.randint(0,11)
        if num<=5:
            num1=num+6
        if num>=5:
            num1=num-6
    
        f.write(f'{variables[num]}{variables[num1]}\n')
       
    f.close()

else:
    f=open("./Ejercicio7.csv","r")

    ls = (f.read())
    
    lines=ls.split(sep="\n")
    print(lines)

    f.close()
    
    nlines=0
    c1=0
    c2=0
    c3=0
    c4=0

    for i in range(0,len(lines)-3):
        #print(lines[i])
        nlines1=lines[i][0]
        nlines2=lines[i+1][0]
        nlines3=lines[i+2][0]
        
        if nlines1=="A" or nlines1=="1" and nlines2=="C" or nlines2=="3" and nlines=="D" or nlines=="4":
            c1=c1+1

        if nlines1=="A" or nlines1=="1" and nlines2=="B" or nlines2=="2" and nlines=="C" or nlines=="3":
            c2=c2+1
        
        if nlines1=="F" or nlines1=="6" and nlines2=="B" or nlines2=="2" and nlines=="F" or nlines=="6":
            c2=c2+1

        if nlines1=="C" or nlines1=="3" and nlines2=="B" or nlines2=="2" and nlines=="F" or nlines=="6":
            c4=c4+1
            
    print(c1)
    print(c2)
    print(c3)
    print(c4)


  
