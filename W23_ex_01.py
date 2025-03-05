file_dict = {}
with open('mbox-short.txt', 'r')as file:
        line = [line.strip()for line in file.readlines()]
        file_content = (line)
        count = line.count('From:')

        print(f" From appears {count} times in the file.")










