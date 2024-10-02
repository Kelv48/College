class person():
    def __init__(self):
        name = input("Please enter your name ")
        age = int(input("Please enter your age "))

        print("Hello %s, you are %i years old" %(name, age))

person()
        