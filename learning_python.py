"""Reading a file with the replacement of one and
alignment to the right."""
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    print(line.rstrip())
    print(line.rstrip())
    print("In Python you can:\n" + line.rstrip() + "\n")
    print(line.replace('Python', 'C').rstrip())