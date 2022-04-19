list_clients = ["Harry","Hamed","ROhan"];
for x in list_clients:
    print("The Clients are " , x);

print("\nWant to Read or Write??");
print("Press 1: Write \n Press Any key to read");
n = int(input("Enter Choice\n"));


def getDate():
    import datetime;
    return datetime.datetime.now();

if (n==1):
    print("1 harry 2 hamed 3 rohan");
    no = int(input());
    if no==1:
        print("1 for food 2 for Exercise");
        ch = int(input());
        if ch==1:
            while(1):
                f = open("harryfood.txt","a");
                # t = input("What have u ate\n");
                f.write(input("What You ate\n"));
                f.write("\n")
                print("press c for exit else any key to continue");
                if (input()=='c'):
                    f.write(str(getDate()));
                    break;
        if ch==2:
            while(1):
                f = open("harryexerc.txt","at");
                f.write(input("What Exercise You Did\n"));
                f.write("\n");
                print("press c for exit else any key to continue");
                if (input() == 'c'):
                    f.write(str(getDate()));
                    break;
    if no == 2:
        print("1 for food 2 for Exercise");
        ch = int(input());
        if ch == 1:
            while (1):
                f = open("hamedfood.txt", "a");
                # t = input("What have u ate\n");
                f.write(input("What You ate\n"));
                f.write("\n")
                print("press c for exit else any key to continue");
                if (input() == 'c'):
                    f.write(str(getDate()));
                    break;
        if ch == 2:
            while (1):
                f = open("hamedexerc.txt", "at");
                f.write(input("What Exercise You Did\n"));
                f.write("\n");
                print("press c for exit else any key to continue");
                if (input() == 'c'):
                    f.write(str(getDate()));
                    break;
    if no == 3:
        print("1 for food 2 for Exercise");
        ch = int(input());
        if ch == 1:
            while (1):
                f = open("rohanfood.txt", "a");
                # t = input("What have u ate\n");
                f.write(input("What You ate\n"));
                f.write("\n")
                print("press c for exit else any key to continue");
                if (input() == 'c'):
                    f.write(str(getDate()));
                    break;
        if ch == 2:
            while (1):
                f = open("rohanexerc.txt", "at");
                f.write(input("What Exercise You Did\n"));
                f.write("\n");
                print("press c for exit else any key to continue");
                if (input() == 'c'):
                    f.write(str(getDate()));
                    break;
else:
    print("1 harry 2 hamed 3 rohan");
    no = int(input());
    if no == 1:
        print("1 for Fetching Food \n 2 for Fetching Exercises ");
        ch = int(input(""));
        if ch==1:
            f = open("harryfood.txt","rt");
            txt = f.read();
            print(txt);
            f.close();
        else:
            f = open("hamedexerc.txt","rt");
            txt = f.read();
            print(txt);
            f.close();



