
lis = [23,45,77,65]

def is_great(a):
    return a>45

lis2 = list(filter(is_great,lis))
print(lis2)