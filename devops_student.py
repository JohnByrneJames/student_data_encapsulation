from student_data import StudentData

class DevOpsStudent(StudentData):  # subclass to StudentData
    def __init__(self, current_grade, current_trainer):
        # super().__init__ is taking all the members of the parent class
        super().__init__(current_grade, current_trainer)
        self.__current_grade = current_grade  # Private attribute
        self.current_trainer = current_trainer  # Public attribute

    def public_method(self):  # public method
        return "This method is public, welcome!!"

    def __private_method(self):  # private method
        return "This method is private! I love cake! How are you seeing this?!"

    # Example of getter and setter method - not usually used in Python
    # But better practice for formally setting attributes values
    # Setter method
    def setcurrentgrade(self, current_grade):
        print("set current_grade() called")
        self.__current_grade = current_grade

    # Getter method
    def getcurrentgrade(self):
        print("get current_grade() called")
        return self.__current_grade

    current_grade = property(getcurrentgrade, setcurrentgrade)


# outside the scope of DevOps class
John = DevOpsStudent(70, "Billy bog-man")
print(John.public_method)

# Attribute Error: 'DevOpsStudent' object (class) has no attribute '__current_grade'
# This is because the attribute current_grade does not exist to anyone trying to access the class from outside.
# >>> print(John.__current_grade)
# The same can be applied to methods inside a class, this can be done with the same __.

print()  # Add Space in the terminal

# Outside scope of DevOpsStudent Class
print(John.public_method())

# Attribute Error: 'DevOpsStudent' object has no attribute '__private_method'
# Again this method is private therefore cannot be accessed outside the DevOpsStudent class.
# >>> print(John.__private_method())

# This is called a mangled method, by changing the name you an actually access this private method.
# Showing that the private function doesn't actually provide much protection. Accessing a private member like
# this should be refrained as it is bad practice.
print(John._DevOpsStudent__private_method())  # object._Class__private_method (name mangling)

# Essentially when a variable has been made private python will perform name mangling, effectively changing the name
# of the variable to '_object._class__variable'.
print()

# This below is possible as the property() function has been used and allows appropriate assignment
# and retrieval of the last_name attribute form outside the class scope.
John.current_grade = 100  # Set the last_name even though it is private
print(John.current_grade)  # Get the last_name, return the last name (despite it being private)
