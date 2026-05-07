class Smartphone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb

phone_obj = Smartphone("Apple", "iPhone 15", 256)

print(f"Brand: {phone_obj.brand}")
print(f"Model: {phone_obj.model}")
print(f"Storage: {phone_obj.storage_gb}GB")
