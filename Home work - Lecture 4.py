#ამოცანა 1
from enum import IntFlag
from selectors import SelectSelector

var_age=input('შეიყვანეთ ასაკი:')

if int(var_age)>=0:
    if int(var_age)<=12:
        print('თქვენ ხართ ბავშვი')
    elif int(var_age)<=19:
        print('თქვენ ხართ თინეიჯერი')
    elif int(var_age)<=64:
        print('თქვენ ხართ ზრდასრული')
    else:
        print('თქვენ ხართ უფროსი')


#ამოცანა 2

var_score=input('შეიყვანეთ ქულა:')
var_attendance=input('შეიყვანეთ დასწრების პროცენტული მაჩვენებელი:')
if int(var_score)>60 and int(var_attendance)>75:
    print('ჩააბარა')
else:
    print('ვერჩააბარა')

#ამოცანა 3

var_student=input('ხართ თუ არა სტუდენტი (yes/no):')
var_member=input('ხართ თუ არა წევრი (yes/no):')

if var_student=='yes' and var_member=='yes':
    print('თქვენ გაქვთ დამატებითი ფასდაკლება')
elif var_student=='yes' or var_member=='yes':
    print('თქვენ გაქვტ ფასდაკლება')
else:
    print('თქვენ არ გაქვთ ფასდაკლება')

#ამოცანა 4

var_username=input('მომხმარებლი:')

if 3<=len(var_username)<=20 and var_username.isalnum()==True:
    print('მომხმარებელის სახელი სწორია')
else:
    print('მომხმარებელის სახელი არასწორია')

