from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import String, Integer, Text, JSON
from config.db import engine, meta

pokemons = Table(
    'pokemons',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('description', String(255)),
    Column('type', JSON),
    Column('debility', JSON),
    Column('evolutions', JSON),
    Column('img', Text)
)

meta.create_all(engine)