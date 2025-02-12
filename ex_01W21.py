word = dict()
with open ('mbox-short.txt', 'r')as file:
    for line in file:
        if line.startswith ("From"):
            print(line)




