class Car:
    wheels=4
    type="vehicle"
    fuel_type="petrol"
    # def __init__(self, brand, color):
    #     self.brand=brand
    #     self.color=color
    def initializn(self,brand, color):
        self.brand=brand
        self.color=color
    def display(self):
        print("I am from " , self.brand ,"brand and "  "color is ", self.color)


c1=Car()        # object created turbocharger
c2=Car()       # object created no turbocharger


c1.initializn("Toyota","red")
c2.initializn("BMW","color")

c1.display()
c2.display()