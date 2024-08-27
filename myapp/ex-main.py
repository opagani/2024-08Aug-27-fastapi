# Exercise: First API

# Install fastapi if you haven't done so already
# Create a directory in which we'll have a FastAPI application.
# Create a file (maybe main.py) in which you import FastAPI, create the app, and create a single function with a single endpoint. (You can choose.)
# Run the application with fastapi dev main.py
# Go to that URL with your browser, and see what you get!

# Exercise: Add a path parameter

# Modify your existing FastAPI application (or copy mine from GitHub, if you didn't get it already),
# such that it takes an argument, and includes it in the returned value.


# import the FastAPI class, to create a FastAPI app
from fastapi import FastAPI

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
