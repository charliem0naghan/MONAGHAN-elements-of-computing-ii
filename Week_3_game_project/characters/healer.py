from .character import Character

# Adding Methods for Specialized Behavior
class Healer(Character):
    """
    Represents a Healer character, inheriting from the Character class.

    Attributes:
        name (str): The healer's name.
        level (int): The healer's level.
        health (int): The healer's current health.
        healing_power (int): The amount of health the healer can restore.
    """
    def __init__(self, name, level, health, healing_power):
        """
        Initializes a new Healer object.

        Args:
            name (str): The healer's name.
            level (int): The healer's level.
            health (int): The healer's starting health.
            healing_power (int): The healer's healing power.
        """
        # Call the parent class's __init__ method to initialize common attributes
        super().__init__(name, level, health)

        # Initialize the healer's specific attribute: healing_power
        self.healing_power = healing_power

    # Create healing method that interacts with other character
    def heal(self, target):
        """
        Heals the target character.

        Args:
            target (Character): The character to heal.

        Returns:
            str: A message indicating the healing action.
        """

        # Increase the target's health by the healer's healing power
        target.health += self.healing_power

        # Return a message describing the healing action
        return f"{self.name} heals {target.name} for {self.healing_power} HP!"