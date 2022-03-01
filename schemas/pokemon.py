from typing import Text, Optional, Dict
from pydantic import BaseModel

class Pokemon(BaseModel):
    id: Optional[int]
    name: str
    description: str
    type: Dict
    debility: Dict
    evolutions: Dict
    img: Text

class PokemonUpdateImg(BaseModel):
    img: Text