from abc import ABC, abstractmethod

# Base Item Class
class Item(ABC):
    def __init__(self, name, damage, legendary=False):
        self.name = name
        self.damage = damage
        self.legendary = legendary
        self.owner = None  # The player who owns this item

    def __str__(self):
        if self.legendary:
            return f"⚔️ [Legendary] {self.name} - Damage: {self.damage}\nThis item radiates power!"
        return f"{self.name} - Damage: {self.damage}"

    @abstractmethod
    def use(self):
        pass

# Weapon Base Class
class Weapon(Item):
    def __init__(self, name, damage, legendary, weapon_type):
        super().__init__(name, damage, legendary)
        self.weapon_type = weapon_type

    @abstractmethod
    def attack_move(self):
        pass

    def use(self):
        print(f"{self.name} is equipped by {self.owner}.")
        print(self.attack_move())
        print(f"{self.name} is used, dealing {self.damage} damage.")

# Subclasses of Weapon
class SingleHandedWeapon(Weapon):
    def __init__(self, name, damage, legendary):
        super().__init__(name, damage, legendary, "Single-Handed")

    def attack_move(self):
        return f"{self.name} performs a Slash attack!"

class DoubleHandedWeapon(Weapon):
    def __init__(self, name, damage, legendary):
        super().__init__(name, damage, legendary, "Double-Handed")

    def attack_move(self):
        return f"{self.name} performs a Spin attack!"

class Pike(Weapon):
    def __init__(self, name, damage, legendary):
        super().__init__(name, damage, legendary, "Pike")

    def attack_move(self):
        return f"{self.name} performs a Thrust attack!"

class RangedWeapon(Weapon):
    def __init__(self, name, damage, legendary):
        super().__init__(name, damage, legendary, "Ranged")

    def attack_move(self):
        return f"{self.name} performs a Shoot attack!"

# Inventory Class
class Inventory:
    def __init__(self, owner=None):
        self.owner = owner
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        item.owner = self.owner
        print(f"{item.name} added to {self.owner}'s backpack.")

    def drop_item(self, item):
        self.items.remove(item)
        item.owner = None
        print(f"{item.name} removed from {self.owner}'s backpack.")

    def view(self, item_type=None):
        if item_type:
            filtered_items = [item for item in self.items if isinstance(item, item_type)]
            for item in filtered_items:
                print(item)
        else:
            for item in self.items:
                print(item)

    def __iter__(self):
        return iter(self.items)

    def __contains__(self, item):
        return item in self.items

# Example Usage
if __name__ == "__main__":
    # Create some items
    master_sword = SingleHandedWeapon("Master Sword", 300, legendary=True)
    muramasa = DoubleHandedWeapon("Muramasa", 580, legendary=True)
    gungnir = Pike("Gungnir", 290, legendary=True)
    belthronding = RangedWeapon("Belthronding", 500, legendary=True)

    # Create an inventory (backpack)
    beleg_backpack = Inventory(owner='Beleg')

    # Add items to inventory
    beleg_backpack.add_item(master_sword)
    beleg_backpack.add_item(muramasa)
    beleg_backpack.add_item(gungnir)
    beleg_backpack.add_item(belthronding)

    # View all items in the inventory
    print("\nAll items in the backpack:")
    beleg_backpack.view()

    # Show items by type
    print("\nView only Ranged Weapons:")
    beleg_backpack.view(RangedWeapon)

    # Drop an item
    beleg_backpack.drop_item(belthronding)

    # Use an item (equip and attack)
    if master_sword in beleg_backpack:
        master_sword.use()

    # Iterate over the inventory
    print("\nIterating through backpack:")
    for item in beleg_backpack:
        if isinstance(item, Weapon):
            print(item.attack_move())
            
