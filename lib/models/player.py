# lib/models/player.py
from models.__init__ import CURSOR, CONN
from models.team import Team

class Player:

    all={}

    def __init__(self, name, position, number, team_id, id=None):
        self.id = id
        self.name = name
        self.position = position
        self.number = number
        self.team_id = team_id

    def __repr__(self):
        return f"{self.name}, {self.position} Number: {self.number} on {Team.find_by_id(self.team_id).name}"
    
#==========================================PropertyFuncs===================================================

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,position):
        if type(position) is int and 0 < position < 12:
            self._position = position
        else:
            raise ValueError("Must chose a position number 1-11")
        
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, number):
        if type(number) is int and -1 < number < 100:
            self._number = number
        else:
            raise ValueError("Player Number must be 0-99")
        
    @property
    def team_id(self):
        return self._team_id
    @team_id.setter
    def team_id(self, team_id):
        if type(team_id) is int and isinstance(Team.find_by_id(team_id), Team):
            self._team_id = team_id
        else:
            raise ValueError(f"Team ID must be a Team ID that already exists")
        
#==========================================ClassMethods===================================================   
     
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS players (id INTEGER PRIMARY KEY, name TEXT, position INTEGER, number INTEGER, team_id INTEGER, FOREIGN KEY (team_id) REFERENCES teams(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS players"""
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls, name, position, number, team_id):
        player = cls(name, position, number, team_id)
        player.save()
        return player

    @classmethod
    def instance_from_db(cls, row):
        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
            player.position = row[2]
            player.number = row[3]
            player.team_id = row[4]
        else:
            player = cls(row[1],row[2],row[3],row[4])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM players"""
        players = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(player) for player in players]

    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM players WHERE id = ?"""
        player = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(player) if player else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """SELECT * FROM players WHERE name = ?"""
        player = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(player) if player else None

#==========================================InstanceMethods===================================================   

    def save(self):
        sql = """INSERT INTO players (name, position, number, team_id) VALUES (?,?,?,?)"""
        CURSOR.execute(sql, (self.name, self.position, self.number, self.team_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """UPDATE players SET name = ?, position = ?, number = ?, team_id = ? WHERE id = ?"""
        CURSOR.execute(sql, (self.name, self.position, self.number, self.team_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM players WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id= None
    