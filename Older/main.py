def ext(lst,ki):
    flag = 0;
    for i in lst:
        innerlength = len(i);
        flag = 0;
        for k in range(innerlength):
            if(len(str(i[k]))==ki):
                continue;
            else:
                flag = 1;
                break;
        if (flag==0):
            print(i);

ext( [(54, 2), (34, 55), (222, 23), (12, 45), (78, )], 2)
