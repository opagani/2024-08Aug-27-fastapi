# import the FastAPI class, to create a FastAPI app
from fastapi import FastAPI
from pydantic import BaseModel, Field

# create a new application instance
app = FastAPI()

# let's define a new API "endpoint"
# we do that in two parts:
# (1) we use a decorator, @app.get('/the_url') to associate the function with a URL
# (2) we use a function to indicate what functionality we want


@app.get(
    "/hello/{name}"
)  # curly braces mean: capture this part of the URL, and turn into a function parameter
async def hello(name):
    return {"message": f"Hello {name}!"}


@app.get("/greeting/{name}")  # we'll have one path parameter, name
async def hello(name, x=3, y=4):  # we have two query parameters, x and y
    return {"message": f"Hello out there, {name}!", "x": x, "y": y, "x+y": x + y}


# Exercise: Calculator

# Define an API endpoint, calc
# It should take a path parameter indicating what kind of calculation to perform (+ and *)
# It should take two query parameters, x and y, which should (we hope!) contain only digits.
# Turn x and y into integers, and then perform the appropriate calculation. Return a dict containing all of the parameters


# @app.get("/calc/{operator}")  # we'll have one path parameter, name
# async def calc(operator, x, y):  # we have two query parameters, x and y
#     print(operator, x, y)
#     return {
#         "x": x,
#         "y": y,
#         "x[+*]y": int(x) + int(y) if operator == "+" else int(x) * int(y),
#     }


# Exercise: More robust calculator

# Modify the calculator API endpoint we defined earlier, such that you can get integers via FastAPI, and not check/cast them yourself.
# What if you want to use floats instead of integers?
# What if you want to allow floats or integers?


# @app.get("/calc/{operator}")  # we'll have one path parameter, name
# async def calc(operator, x: int, y: int):  # we have two query parameters, x and y
#     print(operator, x, y)
#     return {
#         "x": x,
#         "y": y,
#         "x[+*]y": x + y if operator == "+" else x * y,
#     }


class MathProblem(BaseModel):
    operator: str = Field(pattern="^[+*]$")
    x: float = Field(gt=0, lt=100_000)
    y: float = Field(gt=0, lt=100_000)


# Exercise: POST

# Let's rewrite our calculator to handle inputs via POST.
# Use the app.post decorator.
# Create a new URL (post_calc)
# Create a class for submitting MathProblem instances, with one string (operator) and two integers.
# It should return the input arguments and the result, if there is one. Only implement 2-3 operators.
# Try it out in curl, with something like this:
# ❯ curl -X POST -H 'Content-Type: application/json' -d '{"first_name":"Reuven", "last_name":"Lerner", "shoe_size":"hello"}' http://localhost:8000/greet_person


# @app.post("/newcalc")
# async def post_calc(calc: MathProblem):
#     return {
#         "operator": calc.operator,
#         "x": calc.x,
#         "y": calc.y,
#         "x[+*]y": calc.x + calc.y if calc.operator == "+" else calc.x * calc.y,
#     }


#   Exercise: Tightening up newcalc

# Modify the MathProblem class, such that x and y have to be greater than 0 and less than 100,000.
# You can use the gt, ge, lt, le keyword arguments to Field to get this to work.


@app.post("/newcalc")
async def post_calc(calc: MathProblem):
    return {
        "operator": calc.operator,
        "x": calc.x,
        "y": calc.y,
        "x[+*]y": calc.x + calc.y if calc.operator == "+" else calc.x * calc.y,
    }
