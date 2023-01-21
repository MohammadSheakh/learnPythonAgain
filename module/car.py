class Car:
    # pass
    # make = None
    # model = None
    # year = None
    # color = None

    wheels = 4 # class variable # ekta default value assign kore dite hobe

    # special method called init method .. that will construct objects for us
    def __init__(self, make, model, year, color):
        # this method will create object for us
        self.make = make
        self.model = model # instance variable
        self.year = year
        self.color = color

    def drive(self):
        # self refers to the object that is using this method ..
        print("this " + self.model + " car is driving ")

    def stop(self):
        print("This car is stopped")