import sys

# terminal: python task2.py movielist.txt

file = sys.argv[1]
with open(file, 'r') as f:
    contents = f.read()

print(contents)