

def type_logger(func):
    
    def func_arg(*args, **kwargs):
        for arg in args:
            print(f'{func.__name__} ({arg}: {type(arg)})')             
        return 

    return func_arg


@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5, 2, 4.5, 'test', -5)

print(a)

