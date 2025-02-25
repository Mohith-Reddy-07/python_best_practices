class temperature:
    def __init__(self,celcius):
        self.celcius = celcius
        
    @property
    def fahrenheit(self):
        return (self.celcius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celcius = (value - 32) * 5/9
        
temp = temperature(32)
print(f"temp in fahrenheit: {temp.fahrenheit}")

temp.fahrenheit = 99.2
print(f"temp in celcius: {temp.celcius}")
