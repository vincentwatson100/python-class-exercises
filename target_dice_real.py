import random

# Create target number
target = 7

# Create 2 dice
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)

# Calculate total
total = die1 + die2

# Check if total equals target
if total == target:
    print("CORRECT!")
else:
    print("Try again.")