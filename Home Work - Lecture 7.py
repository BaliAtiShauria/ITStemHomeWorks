# # ამოცანა 1
#
#
# var_lst=['ელენე', 'დათო', 'ნიკა', 'ოთო', 'ნიკა', 'დათო', 'ელენე', 'ნიკა', 'გიო']
#
# caunt={}
#
# for i in var_lst:
#     if i not in caunt:
#         caunt.update({i:1})
#     else:
#         caunt.update({i:caunt.get(i)+1})
#
# print(caunt)
#
# # ამოცანა 2
#
# var_dict1={'ასაკი': 23,'სქესი': 'მდედრობითი','ქვეყყანა': 'საქართველო','პროფესია': 'ჩეკისტი'}
# var_dict2={'ფეხის ზომა': 43,'ასაკი': 45,'სიმაღლე' : 1.82,'პროფესია': 'მეშახტე'}
# var_dict3={}
# for i in var_dict1:
#     if i in var_dict2:
#         var_dict3[i]=[var_dict1[i],var_dict2[i]]
#     else:
#         var_dict3[i]=var_dict1[i]
#
# print(var_dict3)
#
# # ამოცანა 3
#
# var_dict={'a':1,'b':2,'c':3}
# var_dictrev={}
# for key,value in var_dict.items():
#     var_dictrev[value]=key
#
# print(var_dictrev)
#
# ამოცანა 4
#
# films1 = {"Inception", "Interstellar", "Joker", "The Matrix", "Dune", "Oppenheimer"}
# films2 = {"Joker", "The Matrix", "Parasite", "Interstellar", "The Shawshank Redemption", "Dune"}
#
# print(f'საერთო ფილმები {films1 & films2}')
# print(f'ფილმები რომელიც უყვარს პირველ ადამიანს {films1 - films2}')
# print(f'ფილმები რომელიც უყვარს მეორე ადამიანს {films2 - films1}')
# print(f'ფილმები რომელიც ან მხოლოდ ერთს უყვარს ან მხოლოდ მეორეს {films1 ^ films2}')
# print(f'ყველა უნიკალური ფილმი {films1 | films2 }')
#
# ამოცანა 5
from itertools import count
from tkinter.font import names

data= {
    "კლასი 10A": {
        "გიორგი": {
            "ასაკი": 16,
            "საშუალო_ქულა": 8.7,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 8, "გამოცდა": False},
                "ისტორია": {"ქულა": 9, "გამოცდა": True},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 92,
            "დამატებითი": ["ფეხბურთი", "პროგრამირება"]
        },
        "ანა": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.4,
            "საგნები": {
                "მათემატიკა": {"ქულა": 10, "გამოცდა": True},
                "ფიზიკა": {"ქულა": 9, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": False},
                "ინგლისური": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 98,
            "დამატებითი": ["ცეკვა"]
        },
        "დავით": {
            "ასაკი": 16,
            "საშუალო_ქულა": 7.2,
            "საგნები": {
                "მათემატიკა": {"ქულა": 6, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": True},
                "ისტორია": {"ქულა": 8, "გამოცდა": True},
                "ინგლისური": {"ქულა": 9, "გამოცდა": False}
            },
            "დასწრება": 75,
            "დამატებითი": ["კალათბურთი", "პროგრამირება"]
        }
    },

    "კლასი 10B": {
        "მარიამ": {
            "ასაკი": 15,
            "საშუალო_ქულა": 9.1,
            "საგნები": {
                "მათემატიკა": {"ქულა": 9, "გამოცდა": True},
                "ბიოლოგია": {"ქულა": 10, "გამოცდა": True}
            },
            "დასწრება": 95,
            "დამატებითი": ["მუსიკა", "ხატვა"]
        },
        "ლევან": {
            "ასაკი": 16,
            "საშუალო_ქულა": 6.8,
            "საგნები": {
                "მათემატიკა": {"ქულა": 5, "გამოცდა": False},
                "ფიზიკა": {"ქულა": 7, "გამოცდა": False}
            },
            "დასწრება": 60,
            "დამატებითი": []
        }
    }
}

var_dict={}

for key, value in data.items():
    for k, v in value.items():
        var_dict[k]=v.get("საშუალო_ქულა")

print(f'სტუდენტების ქულები: {var_dict}')

#############################################################################

for key,value in var_dict.items():
    if value is max(var_dict.values()):
        print(f'საუკეთესო მოსწავლე ქულების მიხედვით: {key, value}')

#############################################################################

atandance ={}

for key, value in data.items():
    for k, v in value.items():
        if v.get('დასწრება') > 90:
           atandance[k]=v.get('დასწრება')

print(f'სტუდენტები 90% ზე მეტი დასწრებით: {atandance}')

#############################################################################

var_classes={}

for key, value in data.items():
    var_classes[key]=len(value)

for key,value in var_classes.items():
    if value is max(var_classes.values()):
        print(f'{key}_ში არის ყველაზე მეტი ბავშვი კონკრეტულად: {value}')

#############################################################################

var_codeing=[]

for key,value in data.items():
    for k, v in value.items():
        for i, j in v.items():
            if i=='დამატებითი' or i=='საგნები':
                if 'პროგრამირება' in j:
                    var_codeing.append(k)
print(f'პროგრამირებას სწავლობენ: {var_codeing}')

#############################################################################

var_attendance=0
var_count=0
for key,value in data.items():
    for k, v in value.items():
        var_attendance=(var_attendance+v.get('დასწრება'))
        var_count=var_count+1
print(f'სკოლაში საშუალო დასწრება არის : {var_attendance/var_count}')

#############################################################################

var_subjects={}

for key, value in data.items():
    for k, v in value.items():
        for i, j in v.items():
            if i=='საგნები':
                var_subjects[k]=len(j)
            if i=='დამატებითი':
                var_subjects[k]=var_subjects.get(k)+len(j)

print(f'სტუდენტების საგნები დამათებითი აქტივობების ჩათვლით: {var_subjects}')

#############################################################################

var_activitycount={}
var_maxactivity={}

for key, value in data.items():
    for k, v in value.items():
        for i, j in v.items():
            if i=='დამატებითი':
                var_activitycount[k]=len(j)

for key,value in var_activitycount.items():
    if value is max(var_activitycount.values()):
        var_maxactivity[key]=value

print(f'ყველაზე მეტი დამატებითი აქტივობა აქვს: {var_maxactivity}')

#############################################################################