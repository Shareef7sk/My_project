#%%
import re
import logging


input_part=input("File Name : ")

aa = open( input_part, 'r')
l=aa.readlines()
aa.close()

s1='cust_ibmb'
e1='cust_ibmb_func'

ll=len(l)   #no of lines 
sli=[]
eli=[]
c=0
input_list_tables=[]
_list=[]
ed=" "                         #statement 
tables_=' '


f = open('unit_test.txt', 'w')
for i in range(ll+1):
    n=i
    line=l[n-1].rstrip('\n')
    ed=ed+line+'\n'
    

# print(ed)
set_ = r'^\s*NOTE\:\sTable\s+.+$'
set_list = re.findall(set_, ed, re.MULTILINE)
for i in set_list:
    # print(i)
    l4=f.write(i + '\n')
    # tables_=tables_+'\n'+i
    
    # l4=f.write('-')
    i=i.split(' ')
    input_list_tables.append(i[1])

print('-----------------------------------------------------------------')

set_ = r'^\s*NOTE\:\sThe\sdata\sset\s+.+$'
set_list = re.findall(set_, ed, re.MULTILINE)
for i in set_list:
    # print(i)
    l4=f.write(i + '\n')
    # tables_=tables_+'\n'+i

    i=i.split(' ')
    input_list_tables.append(i[1])
f.close()  


#%%
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

# set_ = f'''r'^\s*{g}\s+.+$'''
# set_list = re.findall(set_, ed, re.MULTILINE)

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
            
        # print(pp)
        sta=sl[0]+'.'+sl[1]
        # print(sta)

        jo = sta+pp
        jo=jo.upper()
        print(jo)
    # for i in range(ll+1):
    #     n=i
    #     line=l[n-1].rstrip('\n')
    #     ed=ed+line+'\n'
    #     if jo in line:
    #         # print(line)
    #         # pass
    #         print(line)
    #     ed=ed+line+'\n'
    
    # if len(in_put)==1:
    # x = in_put.replace("_", ".")
    # x=x.upper()
    # print(x)
    
    # for j in in_put:
    #     pp+=j
    #     if j=='_':
    #         x = pp.replace("_", ".")
    #         break
        
    # set_ = r'^\s.*+_+$'
    # set_list = re.findall(set_, ed, re.MULTILINE)
    
    # print(pp)
    # print(x)
    # z=in_put.replace(x, y)
    # print(z)
    for i in range(ll+1):
    
        n=i
        line=l[n-1].rstrip('\n')
        ed=ed+line+'\n'
        if jo in line:
            # print(line)
            # pass
            print(line)
        # ed=ed+line+'\n'
    


# %%
print('i')
# %%
