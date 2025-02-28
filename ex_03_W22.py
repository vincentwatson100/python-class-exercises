#open file
file_dict = {}
with open ('mbox-short.txt', 'r') as file:
    for line in file:
#if it starts with from print it
        
        if line.startswith('From'):
            print(line.strip())
            #count_from_lines +=1
#open file
line_count = 1
line_count = line_count+1
file_dict()
with open ('mbox-short.txt', 'r') as file:
    for line in file:
#if it starts with from print it
        
        if line.startswith('From'):
            print(line_count)
            
#make it so it is like a histogram
