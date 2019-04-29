""" Displays a list of cats and dogs and 
handles an error if the file does not exist."""
def cat_dog(filename):
    try:
        with open(filename) as f_obj:
            animals = f_obj.read()
    except FileNotFoundError:
       pass
       # msg = "Sorry, the file " + filename + " does not exist."
       # print(msg)
    else:
        words = animals.split()
        print(words)

filenames = ['dog.txt', 'cat.txt']
for filename in filenames:
    cat_dog(filename)