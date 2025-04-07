# Designing the Smartphone class
class Smartphone:
    def __init__(self, brand, model, price, battery_life):
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_life = battery_life

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"Battery Life: {self.battery_life} hours")

    def make_call(self, number):
        print(f"Calling {number}...")

    def browse_internet(self, url):
        print(f"Browsing {url} on {self.model}...")

# Inheritance layer
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, battery_life, camera_quality):
        super().__init__(brand, model, price, battery_life)
        self.camera_quality = camera_quality

    def take_photo(self):
        print(f"Taking a photo with {self.camera_quality} camera!")

# Creating an instance of Smartphone and SmartphoneWithCamera
phone1 = Smartphone("Apple", "iPhone 13", 999, 20)
phone1.display_info()
phone1.make_call("+1234567890")

phone2 = SmartphoneWithCamera("Samsung", "Galaxy S21", 799, 22, "108MP")
phone2.display_info()
phone2.take_photo()
