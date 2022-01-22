

def val_checker(x):
    def func_val(func):
        def func_num(b):
            msg = f'wrong val {b}'
            if b >= 0:
                print(b ** 3)
            else:
                raise ValueError(msg)
            return 
        return func_num
    return func_val

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(-5)

print(a)
