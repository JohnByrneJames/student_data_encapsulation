class StudentData:
    __current_grade = None  # This is a private attribute
    current_trainer = None

    def __init__(self, __current_grade, current_trainer):
        self.__current_grade = __current_grade
        self.current_trainer = current_trainer

    def print_details(self):
        return "Grade : " + self.__current_grade.__str__() + "\nTrainer : " + self.current_trainer

    def __change_current_grade(self):  # This is a private method
        new_grade = int(input("What grade have you achieved now [0 - 100]: "))
        print(new_grade.__str__() + " is your new grade.")
        __current_grade = new_grade

