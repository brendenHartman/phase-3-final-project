# lib/models/team.py
from models.__init__ import CURSOR, CONN

class Team:
    all={}

    def __init__(self, name, location, conference, id=None):
        self.id = id
        self.name = name
        self.location = location
        self.conference = conference

    def __repr__(self):
        return f"{self.name}, {self.location}, {self.conference} conference"
    
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
    def location(self):
        return self._location
    @location.setter
    def location(self,location):
        if isinstance(location, str) and len(location):
            self._location = location
        else:
            raise ValueError("Location must be a non-empty string")
        
    @property
    def conference(self):
        return self._conference
    @conference.setter
    def conference(self, conference):
        if conference.lower() == "west" or conference.lower() == "east":
            self._conference = conference
        else:
            raise ValueError("Conference must be either west, or east")
        
#==========================================ClassMethods===================================================   
     
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS teams (id INTEGER PRIMARY KEY, name TEXT, location TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS teams"""
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def create(cls, name, location, conference):
        team = cls(name, location, conference)
        team.save()
        return team

    @classmethod
    def instance_from_db(cls, row):
        team = cls.all.get(row[0])
        if team:
            team.name = row[1]
            team.location = row[2]
            team.conference = row[3]
        else:
            team = cls(row[1],row[2],row[3])
            team.id = row[0]
            cls.all[team.id] = team
        return team

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM teams"""
        teams = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(team) for team in teams]

    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM teams WHERE id = ?"""
        team = CURSOR.execute(sql, (id,))
        return cls.instance_from_db(team) if team else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """SELECT * FROM teams WHERE name = ?"""
        team = CURSOR.execute(sql, (name,))
        return cls.instance_from_db(team) if team else None

#==========================================InstanceMethods===================================================   

    def save(self):
        sql = """INSERT INTO teams (name, location, conference) VALUES (?,?,?)"""
        CURSOR.execute(sql, (self.name, self.location, self.conference))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """UPDATE teams SET name = ?, location = ?, conference = ? WHERE id = ?"""
        CURSOR.execute(sql, (self.name, self.location, self.conference, self.id))
        CONN.commit()

    def delete(self):
        sql = """DELETE FROM teams WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id= None
    