"""Game player one"""


class PlayerCharacter:
    """Game with more players"""

    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        print("Running with player: ", self.name)

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2


cy = PlayerCharacter("Cindy")
cy.run()
print(cy.adding_things(4, 9))
