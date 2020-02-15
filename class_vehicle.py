class Vehicle:
    def __init__(self, name, color, worth):
        self.name = name
        self.color = color
        self.worth = worth

car1 = Vehicle("Fer", "red", "$60,000.00")
car2 = Vehicle("Jump", "blue", "$10,000.00")

print(car1.name)
