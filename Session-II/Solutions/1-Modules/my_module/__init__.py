__all__ = ["first", "second"]

## standard practice - if you are publishing your module
from .first import my_func1
from .second import my_func2

# Below can be written here or inside 'submodule' folder's __init__.py file as well. 
# We have written it there hence commenting below line.
# from .submodule.third import my_func3  