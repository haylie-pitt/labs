import json

# Base Item class
class Item:
    def __init__(self, name, item_type, damage=0):
        """Initialize an Item with a name, type, and optional damage."""
        self.name = name
        self.item_type = item_type
        self.damage = damage

    def to_json(self):
        """Convert the item instance to a JSON-encodable object (dict)."""
        return {
            'name': self.name,
            'item_type': self.item_type,
            'damage': self.damage
        }

    @classmethod
    def from_json(cls, data):
        """Deserialize the item from a JSON string."""
        return cls(data['name'], data['item_type'], data['damage'])

    def __str__(self):
        return f"{self.name} (Type: {self.item_type}, Damage: {self.damage})"


# Weapon class inheriting from Item
class Weapon(Item):
    def __init__(self, name, damage, item_type='weapon'):
        """Initialize a Weapon with a name and damage value."""
        super().__init__(name, item_type, damage)

    @classmethod
    def from_json(cls, data):
        """Deserialize the weapon from JSON."""
        return cls(data['name'], data['damage'])


# Inventory class
class Inventory:
    def __init__(self, owner):
        """Initialize the inventory with an owner and an empty list of items."""
        self.owner = owner
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory."""
        self.items.append(item)

    def to_json(self):
        """Convert the inventory instance and all items to a JSON-encodable object."""
        return {
            'owner': self.owner,
            'items': [item.to_json() for item in self.items]
        }

    @classmethod
    def from_json(cls, data):
        """Deserialize the inventory and items from a JSON string."""
        inventory = cls(data['owner'])
        for item_data in data['items']:
            inventory.add_item(Item.from_json(item_data))  # Adjust if specific item types (e.g., Weapon)
        return inventory

    def __str__(self):
        """Display all items in the inventory."""
        inventory_content = f"Inventory of {self.owner}:\n"
        for item in self.items:
            inventory_content += f"{item}\n"
        return inventory_content


# Function to serialize an Inventory object into a JSON string
def inventory_to_json(inventory):
    """Helper function to serialize an Inventory instance into a JSON string."""
    return json.dumps(inventory.to_json(), indent=4)

# Function to deserialize a JSON string into an Inventory object
def json_to_inventory(json_str):
    """Helper function to deserialize a JSON string into an Inventory instance."""
    data = json.loads(json_str)
    return Inventory.from_json(data)


# Testing serialization and deserialization
if __name__ == "__main__":
    # Create some items
    sword = Weapon("Master Sword", 300)
    bow = Weapon("Belthronding", 500)
    
    # Create an inventory and add items to it
    inventory = Inventory("Beleg")
    inventory.add_item(sword)
    inventory.add_item(bow)
    
    # Serialize the inventory to JSON
    serialized_inventory = inventory_to_json(inventory)
    print("Serialized Inventory (JSON):")
    print(serialized_inventory)
    
    # Deserialize the JSON back into an Inventory object
    deserialized_inventory = json_to_inventory(serialized_inventory)
    print("\nDeserialized Inventory (Object):")
    print(deserialized_inventory)
