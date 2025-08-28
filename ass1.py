# Base Class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery  # in percentage

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery = min(100, self.battery + amount)
        print(f"{self.brand} {self.model} charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage and {self.battery}% battery."


# Child Class (Inheritance Example)
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system.")
            self.battery -= 10
        else:
            print("⚠️ Battery too low to play games!")

    # Polymorphism: Overriding __str__
    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition) with {self.cooling_system} cooling."
    

# Testing
phone1 = Smartphone("Samsung", "Galaxy S24", 256, 80)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 512, 50, "Liquid Cooling")

print(phone1)
phone1.call("123-456-789")
phone1.charge(15)

print("\n" + str(gaming_phone))
gaming_phone.play_game("Call of Duty")
gaming_phone.charge(30)
