#SNAKE WATER GUN GAME
import random

hrithik = 0;
computer = 0;
score = 0;
# choice;
turns = 0;
mygamelist = ["s","w","g"];
gamerules = {"sg":0 , "sw":1 , "gs":1,"gw":0,"wg":1,"ws":0};
print(gamerules);
# y = "sg";
# print(gamerules[y]);
while(turns<10):
    turns += 1 ;
    while(1):
        print("Enter Your Choice");
        choice = input("Small case s or g or w\n");
        if(choice=='s' or choice=='g' or choice=='w'):
            print("Your Choice ", choice);
            break;
        else:
            print("invalid choice ");
            continue;

    cpu = random.choice(mygamelist);
    print("CPU Chose", cpu);
    y = choice+cpu;
    if(choice==cpu):
        print("Its A Draw ")
        continue;
    # x = gamerules[choicecpu]
    elif(gamerules[y]==1):
        print("You Won round",turns);
        hrithik +=1;
    else:
        print("CPU won round",turns);
        computer +=1;
print("Your Score",hrithik,"CPU SCORE",computer);
if (hrithik>computer):
    print("Hrithik Won");
else:
    print("Cpu won");
