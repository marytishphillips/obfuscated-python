from smtplib import SMTP as smtp #line:1
import json #line:2
def sendmail (OO0OO0OO00000O000 ,OO0O00OO0OOO00OO0 ,O000000OOOOO00000 ,OOO000O0000000O0O ):#line:4
    OO0000O0O00O0OO0O =smtp ('smtp.gmail.com:587')#line:5
    OO0000O0O00O0OO0O .starttls ()#line:6
    OO0000O0O00O0OO0O .login (OO0OO0OO00000O000 ,OOO000O0000000O0O )#line:7
    OO0000O0O00O0OO0O .sendmail (OO0OO0OO00000O000 ,OO0O00OO0OOO00OO0 ,O000000OOOOO00000 )#line:8
    print ("Mail sent succesfully....!")#line:9
group ={}#line:12
print ('\t\t ......LOGIN.....')#line:13
your_add =input ('Enter your email address :')#line:14
password =input ('Enter your email password for login:')#line:15
print ('\n\n\n\n')#line:16
choice ='y'#line:17
while (choice !='3'or choice !='no'):#line:18
    print ("\n 1.Create a group\n2.Message a group\n3.Exit")#line:19
    choice =input ()#line:20
    if choice =='1':#line:21
        ch ='y'#line:22
        while (ch !='n'):#line:23
            gname =input ('Enter name of group :')#line:24
            group [gname ]=input ('Enter contact emails separated by a single space :').rstrip ()#line:25
            ch =input ('Add another....y/n? :').rstrip ()#line:26
        with open ('groups.json','a')as f :#line:27
            json .dump (group ,f )#line:28
    elif choice =='2':#line:29
        gname =input ('Enter name of group :')#line:30
        try :#line:31
            f =open ('groups.json','r')#line:32
            members =json .load (f )#line:33
            f .close ()#line:34
        except :#line:35
            print ('Invalid group name. Please Create group first')#line:36
            exit #line:37
        members =members [gname ].split ()#line:38
        msg =input ('Enter message :')#line:39
        for i in members :#line:40
            try :#line:41
                sendmail (your_add ,i ,msg ,password )#line:42
            except :#line:43
                print ("An unexpected error occured. Please try again later...")#line:44
                continue #line:45
    else :#line:46
        break 