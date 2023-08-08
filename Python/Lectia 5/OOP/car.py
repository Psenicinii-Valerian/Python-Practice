class Car:
    # attributes and methods

    wheels = 4  # class attribute
    def __init__(self, make, model, year, color):
        self.make = make    # instance attributes
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Vrum Vrum")
    def stop(self):
        print("Stop Stop")

# self = object = class instance
# only objects have access to instance attributes, so classes don't have access for them
# both class and instance have access for class attributes, while only objects(instances) can access instance attributes

car = Car("Nissan", "Silvia", 1984, "Red")
car.drive()
car.stop()