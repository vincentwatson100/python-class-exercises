#creat target number
target=(7)
#create 2 dice
die1=random.randint(1,6)
die2=random.randint(1,6)
total=(die1+die2)
if total== 7:
print('CORRECT!')
else:
print('try again')

