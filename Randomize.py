import random

import os

# Print the current working directory
print("Current working directory:", os.getcwd())

friends = ['Alice', 'John', 'Charles', 'Venkat', 'Tushar']
randint = random.randint(0,len(friends) - 1)
print(friends[randint])
