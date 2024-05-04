#1/usr/bin/env python3
from models.team import Team
from models.player import Player

def seed_database():
    Player.drop_table()
    Team.drop_table()
    Player.create_table()
    Team.create_table()

    chicago = Team.create("Chicago Fire", "Chicago Illinois", "east", 0)
    #la = Team.create()
    #miami = Team.create()
    #nashville = Team.create()

    #walker_z = Player.create()
    #hany_m = Player.create()
    #jacob_s = Player.create()

    #lionel_m = Player.create()
    #luis_s = Player.create()
    #jordi_a = Player.create()

    xherdan_s = Player.create("Xherdan Shakiri", 10, 11, chicago.id)
    brian_g = Player.create("Brian Guttierez",11,12,chicago.id)
    chris_b = Player.create("Chris Barnes",11,13,chicago.id)

    #hugo_l = Player.create()
    #denis_b = Player.create()
    #david_m = Player.create()

seed_database()
print("Seeded database")