#__init__.py
#Using __all__ for Controlled Imports

from .module1 import greet
from .module2 import farewell

__all__ = ["greet"]  # Only `greet` will be imported with `from my_package import *`
