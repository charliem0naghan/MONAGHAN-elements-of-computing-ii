from .warrior import Warrior

# Coding Challenge: Add Your Own Class
class Rogue(Warrior):
    """
    Represents a Rogue character, inheriting from Warrior.

    Attributes:
        name (str): The rogue's name.
        level (int): The rogue's level.
        health (int): The rogue's current health.
        strength (int): The rogue's strength.
        stealth (int): The rogue's stealth level.
    """
    def __init__(self, name, level, health, strength, stealth):
        """Initializes a new Rogue object."""
        # Call the parent class's __init__ method to initialize inherited attributes
        super().__init__(name, level, health, strength)

        # Initialize the rogue's specific attribute: stealth
        self.stealth = stealth

    # Create sneak attack that targets and reduces health of another player
    def sneak_attack(self, target):
        """
        Performs a sneak attack on the target, reducing their health.

        Args:
            target (Character): The target of the sneak attack.

        Returns:
            str: A message describing the sneak attack.
        """
        # Reduce the target's health by a factor of stealth
        target.health -= self.stealth * 3

        # Return a message describing the sneak attack action
        return f"{self.name} performs a sneak attack on {target.name} with {self.stealth * 3} damage!"