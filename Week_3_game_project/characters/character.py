# Defining a Base Class: Character
class Character:
    """
    Represents a generic RPG character.

    Attributes:
        name (str): The character's name.
        level (int): The character's level.
        health (int): The character's current health.
    """
    def __init__(self, name: str, level: int, health: int):
        """
        Initializes a new Character object.

        Args:
            name (str): The character's name.
            level (int): The character's level.
            health (int): The character's starting health.
        """
        self.name = name
        self.level = level
        self.health = health

    def display_info(self):
        """
        Returns a string displaying the character's information.

        Returns:
            str: A formatted string with the character's name, level, and health.
        """
        return f"{self.name} (Level {self.level}) - {self.health} HP"