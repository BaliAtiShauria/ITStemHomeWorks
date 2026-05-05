# ამოცანა 1

var_numbers=[1,2,9,4,5]
total=0
for i in var_numbers:
    total = total + (i)
print(total)

# ამოცანა 2

var_numbers=[1,3,4,8343,45,56,546,676,7,567,578]
var_numbers.sort()
print(
     f'მინიმალური მნიშვნელობა არის: {var_numbers[0]}\n'
     f'მაქსიმალური მნიშვნელობა არის: {var_numbers[len(var_numbers)-1]}'
)
# ამოვცანა 3

var_numbers=[1,54,6,5,0]
var_luwi=[]
var_kenti=[]

for i in var_numbers:
    if i%2==0:
        var_luwi.append(i)
    else:
        var_kenti.append(i)
print(
    f'ლუწი რიცხვები {var_luwi} \n'
    f'კენტი რიცხვები {var_kenti} '
)

# ამოცანა 4

var_num=[23,345,6,7,78,969]
var_numtuple= (*var_num,)
print(var_num)
print(var_numtuple)

###############################################################
var_num=[1,2,3,4,5,6,7]
var_numtuple=tuple(var_num)
print(var_num)
print(var_numtuple)

#################################################################

var_num=[1,2,3,4,5,6]
print(var_num)
print(tuple(var_num))

# ამოცანა 5

var_num=[2,4,5,45,546,6,6,6]
var_numunic=[]
for i in var_num:
    if i not in var_numunic:
        var_numunic.append(i)
print(var_numunic)
print(type(var_numunic))

#######################################################################

var_num=[56,2,1,4,2,3,3,45,3,4,4,55,666,7,7,7,7,]
var_numunic=list(set(var_num))
print(var_numunic)
print(type(var_numunic))






