class Character():

    def __init__ (self, name, character_class, race):

        self.name = name
        self.character_class = character_class
        self.race = race

    def presentation(self):

        yourCharacter = ("\nWelcome player, your character is {}, a {} {}.")
        print (yourCharacter.format(self.name, self.race, self.character_class))

    def attack (self):
        pass

    def magic (self):
        pass

    def sleep (self):
        pass
