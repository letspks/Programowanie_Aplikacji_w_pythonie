import time

def measure_execution_time(unit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time() if unit == 'seconds' else time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.time() if unit == 'seconds' else time.perf_counter()
            execution_time = end_time - start_time -1
            if unit == 'seconds':
                print(f"Czas wykonania funkcji: {execution_time} sekund")
            elif unit == 'microseconds':
                print(f"Czas wykonania funkcji: {execution_time * 1000000} mikrosekund")
            return result
        return wrapper
    return decorator

@measure_execution_time(unit='microseconds')
def example_function():
    time.sleep(1) 
#TAM W LINIJCE 9 wiadomo ze trzeba odjac czas ten ktory dajemy w time.sleep
    
example_function()
