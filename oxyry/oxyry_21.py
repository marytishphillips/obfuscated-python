class CoffeeMachine :#line:1
    def __init__ (OO000000OO00OOOO0 ):#line:2
        OO000000OO00OOOO0 .water =500 #line:4
        OO000000OO00OOOO0 .milk =500 #line:5
        OO000000OO00OOOO0 .coffee_beans =200 #line:6
        OO000000OO00OOOO0 .cups =10 #line:7
        OO000000OO00OOOO0 .money =0 #line:8
    def check_resources (O00O000OO0OOOO0O0 ,O0000O0OO0O00O00O ,O000OO0OOO0OOOOO0 ,O00O0O0OOOOOOO0O0 ,OOO00OOO00O0OO0O0 ):#line:10
        if O00O000OO0OOOO0O0 .water <O0000O0OO0O00O00O :#line:12
            return "Sorry, not enough water."#line:13
        elif O00O000OO0OOOO0O0 .milk <O000OO0OOO0OOOOO0 :#line:14
            return "Sorry, not enough milk."#line:15
        elif O00O000OO0OOOO0O0 .coffee_beans <O00O0O0OOOOOOO0O0 :#line:16
            return "Sorry, not enough coffee beans."#line:17
        elif O00O000OO0OOOO0O0 .cups <OOO00OOO00O0OO0O0 :#line:18
            return "Sorry, not enough cups."#line:19
        else :#line:20
            return "Enough resources. Enjoy your coffee!"#line:21
    def buy_coffee (OOO0OOOOO0O0OOOO0 ,OO00O0O0OO0O0O0OO ):#line:23
        if OO00O0O0OO0O0O0OO =="espresso":#line:24
            OOOO0000O0O0O0O0O =50 #line:26
            OO0OOO0O000OO0OO0 =0 #line:27
            O00O0O00OO00O00OO =18 #line:28
            OOOO00OO0000OO0O0 =1 #line:29
            O0000OO0000OOO00O =1.50 #line:30
            O0OOO00O0O0O0000O ="Espresso"#line:31
        elif OO00O0O0OO0O0O0OO =="latte":#line:32
            OOOO0000O0O0O0O0O =200 #line:34
            OO0OOO0O000OO0OO0 =150 #line:35
            O00O0O00OO00O00OO =24 #line:36
            OOOO00OO0000OO0O0 =1 #line:37
            O0000OO0000OOO00O =2.50 #line:38
            O0OOO00O0O0O0000O ="Latte"#line:39
        elif OO00O0O0OO0O0O0OO =="cappuccino":#line:40
            OOOO0000O0O0O0O0O =250 #line:42
            OO0OOO0O000OO0OO0 =100 #line:43
            O00O0O00OO00O00OO =24 #line:44
            OOOO00OO0000OO0O0 =1 #line:45
            O0000OO0000OOO00O =3.00 #line:46
            O0OOO00O0O0O0000O ="Cappuccino"#line:47
        else :#line:48
            O0OOOO0OOOO0000O0 ="Invalid choice. Please try again."#line:50
            return O0OOOO0OOOO0000O0 #line:51
        O0OOOO0OOOO0000O0 =OOO0OOOOO0O0OOOO0 .check_resources (OOOO0000O0O0O0O0O ,OO0OOO0O000OO0OO0 ,O00O0O00OO00O00OO ,OOOO00OO0000OO0O0 )#line:55
        if O0OOOO0OOOO0000O0 =="Enough resources. Enjoy your coffee!":#line:56
            print (f"Please insert coins for {O0OOO00O0O0O0000O} (${O0000OO0000OOO00O}):")#line:58
            O000O00OOO000O000 =int (input ("How many quarters?: "))#line:59
            OOO0O0O00OOOOOO0O =int (input ("How many dimes?: "))#line:60
            O00OOO0O000O0000O =int (input ("How many nickels?: "))#line:61
            OOOOOO0O00O0000O0 =int (input ("How many pennies?: "))#line:62
            O00O0OO00OOO0OO00 =0.25 *O000O00OOO000O000 +0.10 *OOO0O0O00OOOOOO0O +0.05 *O00OOO0O000O0000O +0.01 *OOOOOO0O00O0000O0 #line:64
            if O00O0OO00OOO0OO00 <O0000OO0000OOO00O :#line:65
                return "Insufficient amount. Money refunded."#line:66
            else :#line:67
                O0O0O0OO0O000OOOO =round (O00O0OO00OOO0OO00 -O0000OO0000OOO00O ,2 )#line:69
                OOO0OOOOO0O0OOOO0 .money +=O0000OO0000OOO00O #line:70
                OOO0OOOOO0O0OOOO0 .water -=OOOO0000O0O0O0O0O #line:71
                OOO0OOOOO0O0OOOO0 .milk -=OO0OOO0O000OO0OO0 #line:72
                OOO0OOOOO0O0OOOO0 .coffee_beans -=O00O0O00OO00O00OO #line:73
                OOO0OOOOO0O0OOOO0 .cups -=OOOO00OO0000OO0O0 #line:74
                return f"Here is ${O0O0O0OO0O000OOOO} in change. Here is your {O0OOO00O0O0O0000O}. Enjoy!"#line:75
        return O0OOOO0OOOO0000O0 #line:78
def main ():#line:81
    O00O00000000OO000 =CoffeeMachine ()#line:83
    while True :#line:85
        print ("============================================")#line:86
        OO0OOOO00OOOO0000 =input ("What would you like? (espresso/latte/cappuccino): ")#line:87
        if OO0OOOO00OOOO0000 in ["espresso","latte","cappuccino"]:#line:89
            print (O00O00000000OO000 .buy_coffee (OO0OOOO00OOOO0000 ))#line:90
        else :#line:91
            print ("Invalid choice. Please try again.")#line:92
if __name__ =="__main__":#line:95
    main ()