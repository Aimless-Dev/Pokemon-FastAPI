from fastapi import APIRouter, HTTPException
from models.pokemon import pokemons
from config.db import conn
from schemas.pokemon import Pokemon, PokemonUpdateImg

pokemon = APIRouter()

@pokemon.get('/pokemons')
def get_pokemons():
    return conn.execute(pokemons.select()).fetchall()

@pokemon.post('/pokemons')
def insert_pokemon(newPokemon: Pokemon):
    result = conn.execute(pokemons.insert().values(newPokemon.dict()))
    return conn.execute(pokemons.select().where(pokemons.c.id == result.lastrowid)).first()

@pokemon.get('/pokemons/{name_pokemon}')
def get_pokemon(name_pokemon: str):
    result = conn.execute(pokemons.select().where(pokemons.c.name == name_pokemon)).first()

    if not (result == None):
        return result

    raise HTTPException(status_code=404, detail='Pokemon not found')

@pokemon.put('/pokemons/{name_pokemon}')
def update_pokemon(name_pokemon: str, newData: PokemonUpdateImg):
    result = conn.execute(pokemons.select().where(pokemons.c.name == name_pokemon)).first()
    if not (result == None):
        conn.execute(pokemons.update().values(img = newData.img).where(pokemons.c.name == name_pokemon))
        return {'message': 'Pokemon has been updated successfully'}

    raise HTTPException(status_code=404, detail='Pokemon not found')

@pokemon.delete('/pokemons/{name_pokemon}')
def delete_pokemon(name_pokemon: str):
    result = conn.execute(pokemons.select().where(pokemons.c.name == name_pokemon)).first()
    if not (result == None):
        conn.execute(pokemons.delete().where(pokemons.c.name == name_pokemon))
        return {'message': 'Pokemon has been deleted successfully'}

    raise HTTPException(status_code=404, detail='Pokemon not found')