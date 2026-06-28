# ამოცანა 1

lst=[1,2,3,4,5]

def safe_get(lst, index):
    return lst[index]

try:
    print(safe_get(lst,int(input('index:'))))
except IndexError:
    print("Error: There is no item with this index")
except TypeError: # დავალებაში რადგან ეწერე ჩავწერე, რეალურად ValueError იჭერს
    print('it is not a number')
except ValueError: # ეს იჭერს რიცხვისგან განსხვავებულ სიმბოლოლს შეცდომას
    print('it is not a number')

# ამოცანა 2

dictionary={'name':'Nika','age':29,'sex':'male'}

def safe_get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        print(f"Error: Key {key} doesn't exist")

print(safe_get_value(dictionary,input('key:')))

# ამოცანა 3

def square (num):
    return num**2
try:
    x=square(float(input('დაწერე რიცხვი:')))
except ValueError:
    print('თექვეა არ შეიყვანეტ რიცხვი')
else:
    print(x)
finally:
    print('ოპერაცია დასრულებული!')
