class Student(object):

    def __init__(self, name, studentid, credits):
        self._name = name
        self._studentid = studentid
        self._credits = credits

    def __str__(self):
        return "%s %d %d" % (self._name, self._studentid, self._credits)
    
    def setName(self, newName):
        self._name = newName

    def getName(self):
        return self._name
    
    def getStudentId(self):
        return self._studentid
    
    def setCredits(self, newCredits):
        self._credits = newCredits

    def getCredits(self):
        return self._credits
    
    def checkEqual(credits1, credits2):
        if credits1 == credits2:
            equals = True
        else:
            equals = False
        return equals
    
    name = property(getName, setName)
    studentid = property(getStudentId)
    credits = property(getCredits, setCredits)

if __name__ == "__main__":
     
    student1 = Student("John", 123, 350)
    student2 = Student("Tom", 124, 400)
    print(student1)
    print(student2)

result = Student.checkEqual(student1.credits, student2.credits)
if result == True:
    print("True")
else:
    print("False")
    
    
