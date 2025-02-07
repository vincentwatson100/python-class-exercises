
fhand = open('mbox.py')




count=0
for line in fhand:
    line=line.rstrip()
    if line.startswith('From:'):
        continue

    print(line)


