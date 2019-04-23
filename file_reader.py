# Reading, removing indents
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

# Reading, output one by one
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

# Reading, outputting one by one and removing gaps from the right edge
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Reading outputting one by one and removing gaps from the right edge
filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())