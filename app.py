from fastapi import FastAPI
from routes.pokemon import pokemon

app =  FastAPI(
    title='Pokemon API', 
    description='a REST API using python and mysql',
    version='0.0.1'
)

@app.get('/', tags=['Home'])
def home():
    return {'message': 'Welcome to my Pokemon API'}

app.include_router(pokemon)