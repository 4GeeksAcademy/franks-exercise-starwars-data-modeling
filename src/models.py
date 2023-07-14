import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    height = Column(Integer, primary_key=True)
    mass = Column(Integer, primary_key=True)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birthyear = Column(String(250))
    gender = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    model = Column(Integer, primary_key=True)
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(Integer, primary_key=True)
    crew = Column(String(250))
    passengers = Column(String(250))
    hyperdrive_rating = Column(String(250))
    mglt = Column(String(250))
    cargo_capacity = Column(Integer, primary_key=True)
    consumables = Column(String(250))
    pilot_id = Column(Integer, ForeignKey('characters.id'))
    pilot = relationship("Characters")
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    diameter = Column(Integer, primary_key=True)
    rotation_period = Column(Integer, primary_key=True)
    orbital_period = Column(Integer, primary_key=True)
    gravity = Column(Integer, primary_key=True)
    population = Column(Integer, primary_key=True)
    climate = Column(Integer, primary_key=True)
    terrain = Column(String(250))
    surface_water = Column(String(250), nullable=True)
    created = Column(String(250))
    edited = Column(String(250))
    name = Column(String(250))

   
   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
