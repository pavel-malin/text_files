# +file (alice.txt, moby_dick.txt, little_women.txt)
def reading_file(filename):
    """So you can do a search on different books or text and 
    the result will show how many words were used in this book.
    You can do so through the terminal or inside the code to
    set the request. But if the request goes through the input
    terminal (not inside the code), it displays only the very 
    first one. To see the result from other files. Then you
    need to change the shape."""
    while True:
        try:
            with open(filename) as f_obj:
                contents = f_obj.read()
        except ValueError:
            print("Not text")
        else:
            prif = input("Text file: ")
            if prif == 'quit':
                break
            say = contents.lower().count(str(prif))
            print(say)

filename = 'alice.txt'
reading_file(filename)
''' Use the bottom form.It is necessary to remove white, if and
remove str(prif) from count
filenames = ['alice.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    reading_file(filename)
'''
