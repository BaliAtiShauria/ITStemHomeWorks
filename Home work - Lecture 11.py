# ამოცანა 1

import math
def decorator(func):
    def wrapper(*args,**kwargs):
        if args[0] != 'sum':
            if args[0] != 'max':
                if args[0] != 'min':
                    if args[0] != 'mult':
                         return 'შეიყვანე სწორი ოპერატორი'
        for i in args[1:]:
            if i<0:
                return "შეიყვანე მხოლოდ დადებითი რიცხვები"
        return func(*args,**kwargs)
    return wrapper

@decorator
def calculate(opration,*args):
    if opration == 'sum':
        return (sum(args))
    if opration == 'max':
        return (max(args))
    if opration == 'min':
        return (min(args))
    if opration == 'mult':
        return (math.prod(args))

print(calculate('min',3,-4,5,6,7,7))


# ამოცანა 2

def formated(func):
    def wrap(*args,**kwargs):
        return print(f'function called {func.__name__},with attributes: {args},{kwargs}, returned: {func(*args,**kwargs)}')
    return wrap


@formated
def add (a,b):
    return (a+b)
add(1,2)

@formated
def div (a,b):
    return (a/b)
div(1,2)

# ამოცანა 3

import time

def decor (func):
    def wrapper(*args,**kwargs):
        for i in range(0,args[0]):
            func(*args,**kwargs)
            time.sleep(args[1])
    return wrapper

@decor
def printi (times,delay):
    print ("Hallo")
printi (10,0.5)

# ამოვცანა 4

current_user = {
    "username": "irakli",
    "role": "editor"
}

def role_required(role):
    def wrapper(*args, **kwargs):
        if current_user['role'] not in args:
            print ('permission denied!')
        else:
            return role(*args,**kwargs)
    return wrapper

@role_required
def delete_user(user_id):
    print (f'User with id {user_id} has been deleted.')
delete_user('admin')
@role_required
def edit_user(user_id):
   print (f'User with id {user_id} has been updated.')
edit_user('editor')
@role_required
def create_user(first_name):
    print (f'User {first_name} has been created.')
create_user('user')