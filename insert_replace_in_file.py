import os
import re

# Get the current working directory
part = os.getcwd()

# Get the list of files in the current directory
h = os.listdir()

# Iterate through each file
for i in h:
    ll = 0
    if '.py' in i:
        file = i
        print(i)
        f = open(i, 'r')
        l = f.readlines()
        f.close()
        ed = ""
        ll = len(l)
        ch = ""
        
        # Iterate through each line in the file
        for i in range(ll+1):
            n = i
            line = l[n-1].rstrip('\n')
            print(line)
            ed = ed + line + '\n'
            
            # Split the text into blocks based on the '#%%' delimiter
            split_text = re.split(r'\n#%%', ed)
        
        # Open the file for writing
        write1 = open(file, 'w')
        
        # Iterate through each block
        for block in split_text:
            if "def insert_partition_macrofunc(cxt)" in block:
                # Skip the block containing 'def insert_partition_macrofunc(cxt)'
                continue
            elif "rcset_macrofunc" in block:
                # Replace the 'rcset_macrofunc' block with the desired content
                aa = block.replace(block, ('''#%%''' + '\n' + 'insert_partition_macrofunc(cxt)'))
                print(aa)
                l4 = write1.write(aa)
            else:
                # Write the block to the file
                print('''#%%''' + '\n' + block)
                l4 = write1.write('''#%%''' + '\n' + block)
