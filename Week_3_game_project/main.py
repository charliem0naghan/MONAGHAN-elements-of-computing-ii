from characters.character import Character
from characters.warrior import Warrior
from characters.mage import Mage
from characters.healer import Healer
from characters.rogue import Rogue


# Simulating Dynamic Behavior
def battle_round(character, target):
    """
    Simulates a single round of battle between two characters.

    Args:
        character (Character): The character performing the action.
        target (Character): The target of the action.
    """
    # Display the character's information
    print("\nBefore round info:")
    print(character.display_info())
    print(target.display_info())

    print("\nAction taken:")
    # Check the character's type and perform the corresponding action
    if isinstance(character, Rogue):  # If the character is a Rogue
        print(character.sneak_attack(target))  # Perform a sneak attack
    elif isinstance(character, Mage):  # If the character is a Mage
        print(character.cast_spell())  # Cast a spell
    elif isinstance(character, Healer):  # If the character is a Healer
        print(character.heal(target))  # Heal the target
    elif isinstance(character, Warrior):  # If the character is a Warrior
        print(character.strength)  # Display the warrior's strength

    print("\nAfter round info:")
    print(character.display_info())
    print(target.display_info())

    if __name__ == "__main__":
        # Create sample characters
        gandalf = Mage("Gandalf", 50, 200, 150)
        dark_knight = Warrior("Dark Knight", 45, 250, 80)

        # Simulate a battle round
        battle_round(gandalf, dark_knight)