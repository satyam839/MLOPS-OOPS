# initiate a class
class Employee:
    # special dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")



# create an instance / obj of the class
sam = Employee()
print(sam.designation,sam.id,sam.salary)
sam.travel("Bodhgaya")
print(id(sam))
# you can create attribute outside class as well
sam.name = "satyam kumar"
print(sam.name)