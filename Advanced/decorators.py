import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} took {str((end-start)*1000)}mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    return [number*number for number in numbers]

@time_it
def calc_cube(numbers):
    return [number*number*number for number in numbers]

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
