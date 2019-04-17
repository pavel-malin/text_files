
filename = 'poll.txt'

while True:
    with open(filename, 'a') as file_object:
        file_object.write(input("Why do you like programming? "))
        file_object.write(".\n")
        bay = input("If you want to run the work then enter 'q': ")
    if bay == 'q':
        break