class Fruit:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    def display(self):
        print(f"Fruit Name : {self.name}")
        print(f"Quantity   : {self.quantity} kg")
        print(f"Price      : Rs. {self.price} per kg")


class FruitShop:
    def __init__(self):
        self.fruits = []

    def add_fruit(self, fruit):
        self.fruits.append(fruit)
        print(f"{fruit.name} added successfully.")

    def display_inventory(self):
        if len(self.fruits) == 0:
            print("Inventory is empty.")
        else:
            print("\n--- Fruit Shop Inventory ---")
            for fruit in self.fruits:
                fruit.display()
                


shop = FruitShop()

while True:
    print("\n1. Add Fruit")
    print("2. Display Inventory")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity in kg: "))
        price = float(input("Enter price per kg: "))

        fruit = Fruit(name, quantity, price)
        shop.add_fruit(fruit)

    elif choice == "2":
        shop.display_inventory()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")