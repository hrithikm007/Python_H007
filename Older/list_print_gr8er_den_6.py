#prepare a list of any items in it, print only numbers gr8er than 6
list = [];
while(1):
    print("Enter value into list n press c to stop adding");
    try:
        x = input();
        list.append(int(x));
    except:
        if (x=='c'):
            break;
print("The items in List are",list);
print("The Items gr8er than 6 are");
for y in list:
    if(y > 6):
        print(y);
    else:
        continue;

