from .character import Character

# Subclass Example: Warrior
class Warrior(Character):
    """
    Represents a Warrior character, inheriting from the Character class.

    Attributes:
        name (str): The warrior's name.
        level (int): The warrior's level.
        health (int): The warrior's current health.
        strength (int): The warrior's strength attribute.
    """
    def __init__(self, name, level, health, strength):
        """
        Initializes a new Warrior object.

        Args:
            name (str): The warrior's name.
            level (int): The warrior's level.
            health (int): The warrior's starting health.
            strength (int): The warrior's strength.
        """
        # Call the parent class's __init__ method to initialize common attributes
        super().__init__(name, level, health)

        # Initialize the warrior's specific attribute: strength
        self.strength = strength