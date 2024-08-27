# import the FastAPI class, to create a FastAPI app
from fastapi import FastAPI
from pydantic import BaseModel, Field

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
async def hello(name, x:int=3, y:int=4):  # we have two query parameters, x and y
    return {'message':f'Hello out there, {name}!',
            'x':x,
            'y':y,
            'x+y':x+y}

@app.get('/calc/{operator}')
async def calc(operator, x:int|float, y:int|float):
    if operator == '+':
        result = x + y
    elif operator == '*':
        result = x * y
    else:
        result = 'Unknown'

    return {'operator':operator,
            'x':x,
            'y':y,
            'result':result}


@app.get('/lightswitch/{state}')
async def lightswitch(state:bool):
    return {'new_state':state}

class Person(BaseModel):
    first_name: str = Field(min_length=1, max_length=15)
    last_name: str = Field(min_length=1, max_length=15)
    shoe_size: int = Field(gt=1, lt=56)

@app.post('/greet_person')
async def greet_person(person:Person):
    return {'message': f'Hello, {person.first_name} {person.last_name}',
            'shoe_size': person.shoe_size,
            'url_origin': '/greet_person'}


class MathProblem(BaseModel):
    operator:str
    x:int = Field(ge=0, lt=100000)
    y:int = Field(ge=0, lt=100000)


@app.post('/newcalc')
async def calc(math_problem:MathProblem):
    if math_problem.operator == '+':
        result = math_problem.x + math_problem.y
    elif math_problem.operator == '*':
        result = math_problem.x * math_problem.y
    else:
        result = 'Unknown'

    return {'operator':math_problem.operator,
            'x':math_problem.x,
            'y':math_problem.y,
            'result':result}
