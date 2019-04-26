"""Guest book. Record guests and text alignment."""
filename = 'guest_book.txt'

while True:
    with open(filename, 'a') as file_object:
        file_object.write("Hello, " + input("You name? "))
        file_object.write("!\n")

    with open(filename) as file_object:
        lines = file_object.readlines()

    for line in lines:
        print(str(line.title().strip()))
        continue
    bay = input("If you want to run the work then enter 'q': ")
    if bay == 'q':
        break