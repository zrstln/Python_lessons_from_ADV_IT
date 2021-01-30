
# from hero import Hero
# или тоже самое
from  hero import *
# --------------------------Main-------------------------------------------
myhero1 = Hero("Vurdalak", 5, "Orc")
myhero2 = Hero("Aleksand", 4, "Humen")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health(60)
myhero1.show_hero()
