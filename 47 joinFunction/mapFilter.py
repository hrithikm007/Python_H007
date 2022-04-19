import re


lis = ['23','45','77','65']
print(type(lis[1]))

# say we want to dp , lis[1] = lis[1]+ 2 but cant do because its string

#  we can use for loop & then iterate through each item & typecast them but costly

numbers = list(map(int,lis))
#  its list(map())
# list_name = list(map(function, list_on_which_operation must be performed))
print(numbers[1]+2)

#  Map returns an OBJECT so we must TYPECAST it to list

# Other Functions can also be passed as paraeter to the map 

def sqre(a):
    return a*a

square = list(map(sqre,numbers))
print(square)

# lambda functions can also be passed to maps

cube = list(map(lambda x: x*x*x , numbers))
print(cube)

# list can have name of functions in them as well

def cube(a):
    return a*a*a

func = [sqre,cube]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)
# map will apply our lambda function to entire list func
#  so iteration 1 will have val = sqre(0),cube(0)
