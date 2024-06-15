import os
import asyncio
from functools import wraps
from IPython import get_ipython

def require_envs(*envs):
    """Decorator to check for required environment variables
    """
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            unset_vars = []
            for env in envs:
                if os.environ.get(env) == None:
                    unset_vars.append(env)
            if unset_vars:
                os.environ["SEND_TO_TELEGRAM"]='False'
            else:
                os.environ["SEND_TO_TELEGRAM"]='True'
            return func(*args, **kwargs)
        return wrapper
    return outer_wrapper

def async_decorator(f):
    """Decorator to allow calling an async function like a sync function"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        ret = asyncio.run(f(*args, **kwargs))
        return ret
    return wrapper

def is_notebook():
    try:
        if 'IPKernelApp' in get_ipython().config:  # pragma: no cover
            return True
        else:
            return False
    except AttributeError:
        return False