class Car:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand 
        self.year = year
        
    def car_model(self):
        print(f'Car model: {self.model}')
        
    def car_brand(self):
        print(f'Car brand: {self.brand}')
        
    def car_year(self):
        print(f'Car year: {self.year}')
        
    def __str__(self):
        return f'MOdel: {self.model}\nBrand: {self.brand}\nYear: {self.year}'