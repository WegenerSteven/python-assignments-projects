class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print("My name is {} and I am {} years old and my gender is {}".format(self.name, self.age, self.gender))
        
#create an instance of the person class
person1 = Person("Shikhule Benard", 21, 'Male')

#call the introduce method to display the person's information
person1.introduce()
        