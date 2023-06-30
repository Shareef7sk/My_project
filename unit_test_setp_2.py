import re
import logging


aa = open('unit_test.txt', 'r')
l=aa.readlines()
aa.close()

ll=len(l)   #no of lines 
sli=[]
eli=[]
c=0
input_list_tables=[]
dub_list=[]
ed=" "  
s=True
jo=''

while s==True:
    in_put=input("enter a table name : ")
    sl=in_put.split("_")
    print(len(sl))
    if len(sl)==2:
        jo = in_put.replace("_", ".")
        jo=jo.upper()
        print(jo)
    pp=''
    
    
    if len(sl)>2 :
        for i in range(2,len(sl)):
            pp=pp+('_'+sl[i])  
        sta=sl[0]+'.'+sl[1]
        jo = sta+pp
        jo=jo.upper()
        print(jo)


    for i in range(ll+1):
        n=i
        line=l[n-1].rstrip('\n')
        ed=ed+line+'\n'
        if jo in line:

            print(line)

    
