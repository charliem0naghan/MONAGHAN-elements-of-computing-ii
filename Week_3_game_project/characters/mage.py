from .character import Character

# Polymorphism in Action
class Mage(Character):
    """
    Represents a Mage character, inheriting from the Character class.

    Attributes:
        name (str): The mage's name.
        level (int): The mage's level.
        health (int): The mage's current health.
        mana (int): The mage's mana points.
    """
    def __init__(self, name, level, health, mana):
        """
        Initializes a new Mage object.

        Args:
            name (str): The mage's name.
            level (int): The mage's level.
            health (int): The mage's starting health.
            mana (int): The mage's starting mana.
        """
        # Call the parent class's __init__ method to initialize common attributes
        super().__init__(name, level, health)

        # Initialize the mage's specific attribute: mana
        self.mana = mana


    def cast_spell(self, mana_cost):
        """
        Simulates the mage casting a spell.

        Returns:
            str: A message indicating the spellcasting action.
        """
        # Could include if/else to avoid negative mana
        self.mana -= mana_cost
        return f"{self.name} casts a spell using {mana_cost} mana! They now have {self.mana} mana."