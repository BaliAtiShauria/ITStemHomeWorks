# ამოცანა 1

def find_min_max (*args):
    return max(args),min(args)

print(find_min_max(1,3,5,6,744,676,86,9,1234))

#ამოცანა 2
import math

def calculate(opration,*args):
    if opration == 'sum':
        return (sum(args))
    if opration == 'max':
        return (max(args))
    if opration == 'min':
        return (min(args))
    if opration == 'mult':
        return (math.prod(args))

print(calculate('mult',3,4))

# ამოცანა 3

def format_user(first_name,last_name,**kwargs):
    other=', '.join(f'{k}={v}' for k,v in kwargs.items())
    return f'{first_name} {last_name}| {other}'

print(format_user('ნიკა','ფიცხევაური',age=38,job='დეველოპერი'))

# ამოცანა 4

def safe_divide(a, b):
    if b==0:
        return "Cannot divide by zero"
    else:
        return (a//b,a%b)

print(safe_divide(59,7))
