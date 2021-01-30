class Hero:
    """Class to create Hero for our game"""
    def __init__(self, name, level, race):
        """Initiate our hero"""
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        """print all parameters of his Hero"""
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + self.race + " " +
                       str(self.health)).title()
        print(description)

    def level_up(self):
        """Upgrade level of hero"""
        self.level += 1

    def move(self):
        """Start moving Hero"""
        print("Hero " + self.name + " start moving...")

    def set_health(self, new_health):
        self.health = new_health


# -------------------------------------------------------------------------------------
class SuperHero(Hero):
    """Class to create to Super Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our Super hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100

    def makemagic(self):
        """Use magic"""
        self.magic -= 10

    def show_hero(self):
        description = (self.name + " Level is: " + str(self.level) + " Race is: " + (self.race + " " + str(self.health)
                                                                                     + " Magic is " + str(self.magic)))
        print(description)
