import re

aa = open('sascode.txt', 'r')
l=aa.readlines()
aa.close()

s1='cust_ibmb'
e1='cust_ibmb_func'

ll=len(l)   #no of lines 
sli=[]
eli=[]
c=0
input_list_tables=[]
dub_list=[]
ed=" "                         #statement 

for i in range(ll+1):
    n=i
    line=l[n-1].rstrip('\n')
    ed=ed+line+'\n'




def list_1(table):
    
    table_ = r'^(.*table.*)$'
    table_list = re.findall(table_, ed, re.MULTILINE)

    for i in table_list:
        # print(i)
        i=i.split(' ')
        dub_list.append(i[2])
        
table="table"        
list_1(table)

def list_1(data_):
    
    table_ = r'^(.*data.*)$'
    table_list = re.findall(table_, ed, re.MULTILINE)

    for i in table_list:
        # print(i)
        i=i.split(' ')
        dub_list.append(i[1])
        
data_="data"        
list_1(data_)

print(dub_list)
