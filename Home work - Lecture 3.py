# ამოცანა 1

var_fullname=input('გთხოვტ მიუთითოთ სახელი და გვარი:')
var_name,var_surname=var_fullname.split()
print(f'თქვენი ინიციალებია: {var_name[0].upper()}.{var_surname[0].upper()}')

var_initials='.'.join([var_name[0].upper(),var_surname[0].upper()])
print(f'თქვენი ინიციალებია: {var_initials}')


#ამოცანა 2

var_string=input('გთხოვთ დაწეროთ რამე სიტყვა:')
print(f'{var_string[::-1]}')

#ამონაცა 3

var_sentence=input('დაწერეთ წინადადება:')
print(var_sentence)
var_words=input('ჯერ დაწერეთ რომელი სიტყვა უნდა შეიცვალო და შემდეგ რითი უნდა შეიცვალოს:')
var_replaceable,var_substitute=var_words.split()
var_newsentence=var_sentence.replace(var_replaceable,var_substitute)
print(var_newsentence)

