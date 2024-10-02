class Cartesian_point():
    def __init__(self):
        x = 0
        y = 0
        self.x = x
        self.y = y
        Cartesian_point.getX(self)
        Cartesian_point.getY(self)

    def getX(self):
        x = int(input("Please enter a number for the x coordinate ")) 
        self.x = x

    def getY(self):
        y = int(input("Please enter a number for the y coordinate "))
        self.y = y
    
        print((self.x , self.y))


Cartesian_point()


