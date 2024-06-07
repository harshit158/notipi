import os
import asyncio
from functools import wraps

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
                print(f'Please set these env variables: {unset_vars}')
                return
            func(*args, **kwargs)
        return wrapper
    return outer_wrapper

def async_decorator(f):
    """Decorator to allow calling an async function like a sync function"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        ret = asyncio.run(f(*args, **kwargs))
        return ret
    return wrapper