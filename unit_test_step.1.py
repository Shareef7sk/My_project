import re
import logging





input_part=input("Enter Log file name : ")
aa = open( input_part, 'r')
l=aa.readlines()
aa.close()



ll=len(l)   #no of lines 
sli=[]
eli=[]
c=0
input_list_tables=[]
_list=[]
ed=" "                         #statement 
tables_=' '

# open new file and write the data
f = open('unit_test.txt', 'w')
for i in range(ll+1):
    n=i
    line=l[n-1].rstrip('\n')
    ed=ed+line+'\n'


print('-----------------------------------------------------------------')  

  
# Note: Table line
set_ = r'^\s*NOTE\:\sTable\s+.+$'
set_list = re.findall(set_, ed, re.MULTILINE)
for i in set_list:
    l4=f.write(i + '\n')
  
    i=i.split(' ')
    input_list_tables.append(i[1])

print('-----------------------------------------------------------------')

# Note: There line
set_ = r'^\s*NOTE\:\sThere\s+.+$'
set_list = re.findall(set_, ed, re.MULTILINE)
for i in set_list:
    l4=f.write(i + '\n')
    i=i.split(' ')
    input_list_tables.append(i[1])

print('-----------------------------------------------------------------')

# Note: There line   
set_ = r'^\s*NOTE\:\sAppending\s+.+$'
set_list = re.findall(set_, ed, re.MULTILINE)
for i in set_list:
    # print(i)
    l4=f.write(i + '\n')
    i=i.split(' ')
    input_list_tables.append(i[1])
    
print('-----------------------------------------------------------------')

set_ = r'^\s*NOTE\:\sThe\sdata\sset\s+.+$'
set_list = re.findall(set_, ed, re.MULTILINE)
for i in set_list:
    
    l4=f.write(i + '\n')
    i=i.split(' ')
    input_list_tables.append(i[1])
f.close()  
