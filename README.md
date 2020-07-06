# Encapsulation

#### A concept related to the object oriented approach of programming.

Encapsulation is the packing of data and functions operating on that data into a single component
and restricting the access to some of the object's components. It essentially means the internal representation of
an object is generally hidden from view outside of the objects definition.

A good example is a class, it encapsulates all the data that its member methods and attributes have.

[**devops_student**](devops_student.py) **[Parent/ Base Class]**
* **Attributes**
    * current_grade `private`
    * current_trainer `public`
* **Methods**
    * print_details `public`
    * change_current_grade `private` 

[**student_data**](student_data.py) **[Child/ Derived Class]**
* **Methods**
    * public_method `public`
    * private_method `private`

Some would say that Encapsulation is very similar to Abstraction, however there is one major difference :
* **Encapsulation** = Information hiding
* **Abstraction** = Implementation hiding

To declare a member as **protected** you use a `_` by convention. This tells others : 
> **"** Don't touch this, unless you are a
subclass of this class **"**. 

To declare a member as private you use two `__` in front of it to hide it from users when accessing
them from outside the class.

If you change the value of a private attribute it will actually take place but you are
expected to not do it if it has been distinguished as a private attribute. A proper way to do this is
to add a getter and setter property function that allows proper alterations of private attributes inside
a class.

```python 
    # Setter method
    def setcurrentgrade(self, current_grade):
        print("set current_grade() called")
        self.__current_grade = current_grade

    # Getter method
    def getcurrentgrade(self):
        print("get current_grade() called")
        return self.__current_grade

    current_grade = property(getcurrentgrade, setcurrentgrade)
```

Trying to access private attributes and methods of a class will return an attribute error usually,
this is because python essentially hides a variable to everyone outside the class by performing
a technique called name mangling, this changes the name of a variable. This is not
100% secure though as you can still access the attributes and methods by
entering the altered name which looks like this:

`object._Class__private_method` 

`object._Class__private_attribute`