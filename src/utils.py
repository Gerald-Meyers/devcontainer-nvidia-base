from common import *

def function_timer(func):
    """
    A decorator that prints the execution time of the 
    function it wraps.
    """
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Record the start time
        start_time = time.perf_counter()
        
        # Call the original function with its arguments
        result = func(*args, **kwargs)
        
        # Record the end time
        end_time = time.perf_counter()
        
        # Calculate and print the duration
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration:.6f} seconds")
        
        # Return the original function's result
        return result
    return wrapper_timer