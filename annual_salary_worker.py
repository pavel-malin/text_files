from worker import Employee

while True:
    first = input("\nPlease give me a first name: ")
    last = input("Please give me a last name: ")
    annual_salary = input("Annual salary: $")
    name = input("Enter 'q' at any time to quit.\n")
    if name == 'q':
        break

my_moneys = Employee(first, last)
my_moneys.show_question()
my_moneys.give_raise(annual_salary)
my_moneys.give_name()