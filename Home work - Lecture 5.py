#ამოცანა 1

n=int(input("შეიყვანე მთელი რიცხვი: "))
while n>1:
    print(n)
    n=n-1

print('მადლობა ყურადღებისთვის')

#ამოცანა 2

total=0
while True:
    var_int=int(input('შეიყვანე მთელი რიცხვი: '))
    if var_int==0:
        break
    total = total + var_int
print(total)

######################################################################################

var_int=int(input('შეიყვანე მთელი რიცხვი:')) # ეს სტრიქონი უზრუნველოყოფს რომ არანულოვანი რიცხვის დამატება არ მოხდეს, როგორც ეწერეა დავალებაში
total=0
while var_int != 0:
    total = total + var_int #
    var_int=int(input('შეიყვანე მთელი რიცხვი: '))
print(total)

#ამოცანა 4

var_str = input("შეიყვანე ტექსტი: ")
for i in var_str:
    if i in "aeiouაეიოუ":
        continue
    print(i)

#ამოცანა 5

for i in range(9):
    print(i)
for i in range(5,15):
    print(i)
for i in range(0,20,2):
    print(i)
for i in range(10,1,-1):
    print(i)





