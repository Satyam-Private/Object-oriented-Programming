class house:
    area = 4000
    color = 'dark grey'
    pool = True
    #self indicates that which object is getting accessed 
    #sefl is an instance on which object is calling
    def info(self):
        print(f"""
            {self.area}
            {self.color}
            {self.pool}  """)

house1 = house()
house1.info()
# in above case the self is pointing towards the house1 
#take another example
house2 = house()
house2.area = 4500
house2.color = "white"
house2.pool = True
house2.info()
#in this case the self is pointing to house2 object 
