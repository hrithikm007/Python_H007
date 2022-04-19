#string slicing in Python
var2 = "hrithik is a Genius ";
print(len(var2));
print(var2[0:7]);
print(var2[0:6]);
print(var2[0:8:2]);
print(var2[0:len(var2):3]);
print(var2[0:len(var2):4]);
#string indexing starts from 0
#var[a:b]; a included b excluded
print(var2[::2]);
print(var2.endswith("Genius "));
print(var2.capitalize());
print(var2.upper());
str = var2.replace("Genius ","Legend ")
print(str.upper());

