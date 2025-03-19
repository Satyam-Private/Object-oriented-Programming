class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        print(f"the name {self.name} and the age is {self.age}")
    def set_info(self, name , age):
        self.name = name
        self.age = age


p1 = person("satyam" , 20)
p1.get_info()
p1.set_info("shivam" , 23)
p1.get_info()