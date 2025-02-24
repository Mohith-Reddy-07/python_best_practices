class car:
    def __init__(self,color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def price(self):
        if self.model=='tesla':
            if self.year >=2024:
                return 20000
        elif self.model=='toyota':
            if self.year >=2024:
                return 10000


car1 = car('black', 'tesla', 2024)

print(car1.price())