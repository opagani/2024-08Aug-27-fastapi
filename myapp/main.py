# import the FastAPI class, to create a FastAPI app
from fastapi import FastAPI

# create a new application instance
app = FastAPI()

# let's define a new API "endpoint"
# we do that in two parts:
# (1) we use a decorator, @app.get('/the_url') to associate the function with a URL
# (2) we use a function to indicate what functionality we want

@app.get('/hello/{name}')   # curly braces mean: capture this part of the URL, and turn into a function parameter
async def hello(name):      # we'll get name defined based on the URL, thanks to FastAPI's assignment
    return {'message':f'Hello out there, {name}!'}

@app.get('/greeting/{name}')  # we'll have one path parameter, name
async def hello(name, x=None, y=None):  # we have two query parameters, x and y
    return {'message':f'Hello out there, {name}!',
            'x':x,
            'y':y,
            'x+y':x+y}
