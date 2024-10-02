class Person(object):
    def __init__(self, name, job, salary):
        self._name = name
        self._job = job
        self._salary = salary

    def __str__(self):
        return ("%s %s %i" % (self._name, self._job, self._salary))

    def givePayRaise(self, percentage):
        self._salary += self._salary * (percentage / 100)
    
    def getName(self):
        return self._name

    def getJob(self):
        return self._job

    def setJob(self, jobTitle):
        self._job = jobTitle

    def getSalary(self):
        return self._name

    def setSalary(self, salary):
        if type(salary) != int:
            print("Pass a number")
            return 
        self._salary = salary

    name = property(getName)
    job = property(getJob, setJob)
    salary = property(getSalary, setSalary)

class Manager(Person):
    def __init__(self, name, job, salary, project):
        super().__init__( name, job, salary)
        self._project = project

    def getProject(self):
        return self._project

    def setProject(self, project):
        self._project = project
    project = property(getProject, setProject)

    def getPayRaise(self, percentage):
    #self._salary += self._salary * (percentage / 50)
        super().givePayRaise(percentage * 2)

    def __str__(self):
        return ("%s with project %s" % (super().__str__(), self._project))


class Engineer(Person):
    def __init__(self, name, job, salary, speciality):
        super().__init__(name, job, salary)
        self._speciality = speciality

    def getSpeciality(self):
        return self._speciality
    
    def setSpeciality(self, speciality):
        self._speciality = speciality
    speciality = property(getSpeciality, setSpeciality)

    def getPayRaise(self, percentage):
        super().givePayRaise(percentage * 2)

    def __str__(self):
        return ("%s with speciality %s" % (super().__str__(), self._speciality))

def main():
    cathal = Person("Cathal", "Software person", 120000)
    cathal.givePayRaise(10)
    print(cathal)
    
    luca = Manager("Luca", "Manger", 120000, "The Big Job")
    luca.getPayRaise(10)
    print(luca)
    print(luca.project)
    
    john = Engineer("John", "Engineer", 120000, "Programming")
    john.getPayRaise(10)
    print(john)
    print(john.speciality)

if __name__ == "__main__":
    main()  


