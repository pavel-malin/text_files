class Employee():
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.responses = []
    
    def show_question(self):
        print(self.first + ' ' + self.last)
        

    def give_raise(self, annual_salary):
        self.responses.append(annual_salary)

    def give_name(self):
        print("Survey: ")
        for response in self.responses:
            print("\tFirst name " + self.first.title() + ' ' + self.last.title() + " annual salary $" + response)