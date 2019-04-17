print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst_number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    try:
        anwers = int(first_number) / int(second_number)
    except ValueError:
        print("Used letters when dividing!!!!")
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(anwers)