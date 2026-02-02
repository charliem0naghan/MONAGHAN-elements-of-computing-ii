from .warrior import Warrior

class Archer(Warrior):
    """
    Represents an Archer character, inheriting from Warrior.

    Attributes:
        name (str): The archer's name.
        level (int): The archer's level.
        health (int): The archer's current health.
        strength (int): The archer's strength.
        arrows (int): The archer's number of arrows.
    """
    def __init__(self, name, level, health, strength, arrows):
        """Initializes a new Archer object."""
        # Call the parent class's __init__ method to initialize inherited attributes
        super().__init__(name, level, health, strength)

        # Initialize the archer's specific attribute: arrows
        self.arrows = arrows

    # Create an action fire_arrow that targets and reduces health of another player
    def fire_arrow(self, target):
        """
        Fires an arrow at the target, reducing their health.

        Args:
            target (Character): The target of the arrow.

        Returns:
            str: A message describing the arrow attack.
        """
        # Reduce the target's health by a factor of arrows
        # if arrows are greater than 0, subract 1 from arrows
        if self.arrows > 0:
            self.arrows -= 1
        # subtract health from the target equal to the archer's strength
        target.health -= self.strength  
        # Return a message describing the arrow attack action
        return f"{self.name} fires an arrow at {target.name} with {self.strength} damage!"
        # if there are no arrows left, return a message saying so
        if self.arrows <= 0:
            return f"{self.name} has no arrows left to fire"   
    
        