counts = dict()
with open('mbox-short.txt')as file:
        
        
        for line in file:
                if line.startswith('From'):
                        print(line.strip())
                        words = line.split()
                        for word in words:
                                if word not in counts:
                                        counts[word] = 1
                                else:
                                        counts[word] += 2
                                print(words)
                         
print(counts)

 










