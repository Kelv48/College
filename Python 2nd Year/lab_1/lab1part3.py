class Dog():
    def __init__(self, name, human_years):
        self._name = name
        self._human_years = human_years
        dog_years = human_years * 7
        self._dog_years = dog_years

    

dog = Dog(input("What is the dogs name "), int(input("What is the dogs age in human years ")))
print("The dogs name is %s, They are %i human years old and %i dog years old" %(dog._name, dog._years, dog._dog_years))
