#Base Item class:
class Item:
    def __init__(self, name, description='', rarity='common'):
        self.name = name
        self.description = description
        self.rarity = rarity
        self._ownership = ''

    def pick_up(self, character: str) -> str:
        self._ownership = character
        return f"{self.name} is now owned by {character}"

    def throw_away(self) -> str:
        self._ownership = ''
        return f"{self.name} is thrown away."

    def use(self) -> str:
        if self._ownership:
            return f"{self.name} is used."
        return ''  # No output if the item has no owner

    def __str__(self):
        return f"Item: {self.name}, Rarity: {self.rarity}, Owner: {self._ownership or 'No owner'}"

# Weapon class inherits from Item
class Weapon(Item):
    def __init__(self, name, description='', rarity='common', damage=10, weapon_type='sword'):
        super().__init__(name, description, rarity)
        self.damage = damage
        self.weapon_type = weapon_type
        self._attack_modifier = 1.15 if rarity == 'legendary' else 1.0
        self._equipped = False

    def equip(self):
        if self._ownership:
            self._equipped = True
            print(f"{self.name} is equipped by {self._ownership}")

    def use(self):
        if self._equipped and self._ownership:
            total_damage = self.damage * self._attack_modifier
            print(f"{self.name} is used, dealing {total_damage:.1f} damage")
        elif not self._ownership:
            print("No output")

    def __str__(self):
        return f"Weapon: {self.name}, Type: {self.weapon_type}, Damage: {self.damage}, Rarity: {self.rarity}"

# Shield class inherits from Item
class Shield(Item):
    def __init__(self, name, description='', rarity='common', defense=10, broken=False):
        super().__init__(name, description, rarity)
        self.defense = defense
        self._defense_modifier = 1.10 if rarity == 'legendary' else 1.0
        self.broken = broken
        self._equipped = False

    def equip(self):
        if self._ownership:
            self._equipped = True
            print(f"{self.name} is equipped by {self._ownership}")

    def use(self):
        if self._equipped and self._ownership:
            modifier = 0.5 if self.broken else 1.0
            total_defense = self.defense * self._defense_modifier * modifier
            print(f"{self.name} is used, blocking {total_defense:.1f} damage")
        elif not self._ownership:
            print("No output")

    def __str__(self):
        return f"Shield: {self.name}, Defense: {self.defense}, Rarity: {self.rarity}, Broken: {self.broken}"

# Potion class inherits from Item
class Potion(Item):
    def __init__(self, name, description='', rarity='common', value=0, type_='HP', effective_time=0):
        super().__init__(name, description, rarity)
        self.value = value
        self.type_ = type_
        self.effective_time = effective_time
        self.empty = False

    def use(self):
        if not self.empty and self._ownership:
            print(f"{self._ownership} used {self.name}, and {self.type_} increases by {self.value} for {self.effective_time}s")
            self.empty = True
        elif not self._ownership or self.empty:
            print("No output")

    @classmethod
    def from_ability(cls, name, owner, type_):
        return cls(name, rarity='common', value=50, type_=type_, effective_time=30, description=f"Generated potion by {owner}")

    def __str__(self):
        return f"Potion: {self.name}, Type: {self.type_}, Value: {self.value}, Effective Time: {self.effective_time}s"

# Testing the implementation
if __name__ == "__main__":

    # Example:
    # Weapon:
    belthronding = Weapon(name='Belthronding', rarity='legendary', damage=5000, weapon_type='bow')
    belthronding.pick_up('Beleg')  # Belthronding is now owned by Beleg
    belthronding.equip()  # Belthronding is equipped by Beleg
    belthronding.use()  # Belthronding is used, dealing 5750 damage

    # Shield:
    broken_pot_lid = Shield(name='wooden lid', description='A lid made of wood, useful in cooking. No one will choose it willingly for a shield', defense=5, broken=True)
    broken_pot_lid.pick_up('Beleg')  # wooden lid is now owned by Beleg
    broken_pot_lid.equip()  # wooden lid is equipped by Beleg
    broken_pot_lid.use()  # wooden lid is used, blocking 2.5 damage
    broken_pot_lid.throw_away()  # wooden lid is thrown away
    broken_pot_lid.use()  # NO OUTPUT

    # Potion:
    attack_potion = Potion.from_ability(name='atk potion temp', owner='Beleg', type_='attack')
    attack_potion.use()  # Beleg used atk potion temp, and attack increases by 50 for 30s
    attack_potion.use()  # NO OUTPUT

    # Checking class relationships:
    print(isinstance(belthronding, Item))  # True
    print(isinstance(broken_pot_lid, Shield))  # True
    print(isinstance(attack_potion, Weapon))  # False
