
class User:
    # Class attributes - use the class to call and keeps track for all instances of Users.
    user_count = 0
    # Class Methods - concerned with the class itself and used with the @classmethod decorator.
    @classmethod
    def display_user_count(cls):
        print(User.user_count)

    # Dunder Methods
    # __len__ overide length function
    # __str__ string representation
    # __add__(self, other) when you want to do object + something
    # __mul__(self, other) multiply when you want to do object * something

    def __init__(self, first, last, age):
        User.user_count += 1 
        # Instance Attributes
        self.first = first
        self.last = last
        self._age = age
        # Private
        self._SIN = 123465789
        # Name mangling makes the attributes or methods unique to the User class and not inherited to sub-classes.
        self.__bank_account = 50397846513246
    # reprentation of the object: can be string, dict, list, etc..
    def __repr__(self):
        return f"{self.first} {self.last} {self._age}"

    # Properties 
    # This allow user.age as a getter without a method to be used.
    @property
    def age(self):
        return self._age
    
    # Setter decorator
    # we can use this just like straight up assignment. Also allows for value validation unlike public assignment.
    @age.setter
    def age(self, value):
        # do some value checking
        self._age = value



# print(User.user_count)
# user = User("Emma", "Wickenheiser", 21)
# user2 = User("Brandon", "Best", 25)
# print(user2)
# print(User.user_count)
# print(user2.age)
# user.age = 22
# print(user)

class Student(User):
    def __init__(self, first, last, age,school):
        # User.__init__()
        super().__init__(first, last, age)
        self.school = school
        self._gpa = 0.0

    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, new_gpa):
        if new_gpa >= 0.0 and new_gpa <= 4.0:
            self._gpa = new_gpa


