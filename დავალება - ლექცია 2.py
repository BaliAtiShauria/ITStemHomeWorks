from operator import truediv
# ამოცანა 1
var_int= 5
var_float= 5.5
var_string= 'სტრინგი'
var_boolean= 5<=3

print(type(var_int))
print(type(var_float))
print(type(var_string))
print(type(var_boolean))

print(var_int)
print(var_float)
print(var_string)
print(var_boolean)

# ამოცანა 2

var_birthY=input('გთხოვთ მიუთითოთ დაბადების წელი: ')
var_birthY=int(var_birthY)
var_birthY=2025-var_birthY
print('მომხმარებლის ასაკი:',var_birthY)

# ამოცანა 3

var_number=input('შეიყვანე რიცხვი: ')
var_number=int(var_number)
print('დადებითი:',var_number>0)
print('უარყოფითი:',var_number<0)
print('ნული:',var_number==0)





