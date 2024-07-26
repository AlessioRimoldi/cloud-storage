import time
from io import StringIO
import functools 
from contextlib import redirect_stdout

def return_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f= StringIO()
        with redirect_stdout(f):
            func(*args, **kwargs)
        return f.getvalue()
    return wrapper

def timeit(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        start = time.time()
        out = fun(*args, **kwargs)
        return {'duration':time.time() - start, 'output': out}
    return wrapper

@timeit
@return_execution
def execute(code): 
    exec(code)

