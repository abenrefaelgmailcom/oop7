# ✳️ תרגיל 1: סכום מספרים עם *args
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(1, 2, 3, 4))



# ✳️ תרגיל 2: הדפסת מידע על משתמשים עם **kwargs
def print_user_info(**kwargs):
    info =[]
    for key, value in kwargs.items():
        info.append(f'{key}: {value}')
    print(', '.join(info))

print_user_info(name="Dana", age=30, city="Tel Aviv")

# ✳️ תרגיל 3: חיבור ערכים עם *args ו־**kwargs יחד
def combine_values(*args, **kwargs):
    print(f'sum: {sum(args)}')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

combine_values(2, 4, 6, name="Tom", job="Dev")


# ✳️ תרגיל 4: ברירת מחדל עם **kwargs

def greet_user(**kwargs):
    name = kwargs.get('name', 'guest')
    print(f'Hellow {name}')
greet_user(name="Adam")
greet_user()