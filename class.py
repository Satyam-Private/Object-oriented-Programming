class person:
    name = 'SAtyam'
    occupation = 'student'

#class is blueprint for creating a object
#self is keyword used to identify the object 
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
a.name = "satyam patil"
a.info()
b = person()
b.name = "sagar"
b.occupation = 'HR'
b.info()

c = person()
c.name = "suraj"
c.occupation = "engineer"
c.info()