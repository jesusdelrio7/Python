f =open("./punto.csv","r")
ls = (f.read())
lines=ls.split(sep="\n")
lines1=lines.split(sep=",")


for i in range (0,len(lines1)):
    newline=lines1[i]
    for j in range (0,len(newline)):
        newline[j].replace(",",".")
    
        print (newline[j])
      
    f.close()
