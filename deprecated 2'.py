from functools import wraps
from warnings import warn

def deprecated()
    def decorator(f):
       @wraps(f)
       def wrapper(*args, **kwargs):
          warn("я за себя не отвечаю")
          return   f(*args, **kwargs)
       return wrapper
@deprecated
def f(x):
    return x