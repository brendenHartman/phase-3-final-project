#1/usr/bin/env python3
from models.team import Team
from models.player import Player
def clear_data():
    Player.drop_table()
    Team.drop_table()

def seed_database():
    Player.drop_table()
    Team.drop_table()
    Player.create_table()
    Team.create_table()

    chicago = Team.create("Chicago Fire", "Chicago Illinois", "east", 0)
    la = Team.create("LAFC", "Los Angeles, California", "west", 0)
    miami = Team.create("Miami FC", "Miami, Florida", "east", 0)
    nashville = Team.create("Nashville SC", "Nashville, Tennessee", "east", 0)

    Player.create("Walker Zimmerman", 4, 25, nashville.id)
    Player.create("Hany Mukhtar", 10, 10, nashville.id)
    Player.create("Jacob Shaffelburg", 11, 14, nashville.id)

    Player.create("Lionel Messi", 9, 10, miami.id)
    Player.create("Luis Suarez", 9, 9, miami.id)
    Player.create("Jordi Alba", 3, 18, miami.id)

    Player.create("Xherdan Shaqiri", 7, 10, chicago.id)
    Player.create("Brian Gutierrez",10,17,chicago.id)
    Player.create("Chris Brady",1,34,chicago.id)

    Player.create("Hugo Lloris", 1, 1, la.id)
    Player.create("Denis Bouanga",7,99,la.id)
    Player.create("Aaron Long", 3, 33, la.id)

seed_database()
print("Seeded database")