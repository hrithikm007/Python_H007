#List datatype in Python
redeemcodes = [190,"Hariharan","190","Manoj 1",190.4,"Himanshu","160","Pramod"];
print(redeemcodes);
print(redeemcodes[1]);
#list is a mixed datatype
profit = [50,50,100,20,20,57,54,107]; #profit is  a integer list
print(profit);
print(profit[0:len(profit):3]);
print(profit[::2]);
print(profit[::-2]);
#append funtion can be used with lists
#append can insert strings also
numbers = [];
numbers.append(12);
numbers.append(7);
numbers.append(27);
print(numbers);
numbers.insert(1,69);
numbers.insert(2,7);
print(numbers);
numbers.remove(12);
numbers.remove(7);
numbers.pop();
print(numbers);
# list = [] mutable, tuple = () non mutable
tupableme = (7);
#tupableme[1] = 27 throws an error
print(tupableme);
