# ამოცანა 1

def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(8298798))

# ამოცანა 2

is_even=lambda x:x%2==0

print(is_even(8298))

# ამოცანა 3

students = [
    ("Luka", 15, 85),
    ("Ana", 14, 92),
    ("Giorgi", 16, 78),
    ("Nino", 15, 95)
]

sorted_students = sorted(students, key=lambda x:(x[1],x[2]))

print(sorted_students)

# ამოცანა 4

words = ["banana", "apple", "kiwi", "watermelon", "cherry"]

sorted_words = sorted(words, key=lambda x:len(x), reverse=True)

print(sorted_words)

# ამოცანა 5

uppercase_letters = list(map(lambda x:x[0].upper(), words))
print(uppercase_letters)

# ამოცანა 6

numbers = [5, 12, 7, 18, 3, 24, 9]

filtered_numbers = list(filter(lambda x:(x%3==0 and x>10), numbers))

print(filtered_numbers)

# Optional Task

students_list= {'ნიკა': {'ქართული':80, 'მათემატიკა':98, 'სთიმი':97},
                'სალომე': {'ქართული':65, 'მათემატიკა':92, 'სთიმი':92},
                'ნინო': {'ქართული':89, 'მათემატიკა':78, 'სთიმი':77},
                'გიორგი': {'ქართული':76, 'მათემატიკა':83, 'სთიმი':65},
                'დათო': {'ქართული':93, 'მათემატიკა':84, 'სთიმი':88}
                }

avaradge_sroce=dict(map(lambda x:(x[0],sum(x[1].values())/len(x[1])),students_list.items()))

print(avaradge_sroce)

filter_by_score=dict(filter(lambda x:x[1]>85,avaradge_sroce.items()))

print(filter_by_score)

sorted_by_score=dict(sorted(avaradge_sroce.items(),key=lambda x:x[1],reverse=True))

print(sorted_by_score)