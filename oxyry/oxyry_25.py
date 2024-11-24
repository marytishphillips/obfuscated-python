from tkinter import *#line:1
import random #line:2
import os #line:3
from tkinter import messagebox #line:4
class Bill_App :#line:7
    def __init__ (OOO0O0O0O0OOO0O00 ,O0O00O000O000O0OO ):#line:8
        OOO0O0O0O0OOO0O00 .root =O0O00O000O000O0OO #line:9
        OOO0O0O0O0OOO0O00 .root .geometry ("1350x700+0+0")#line:10
        OOO0O0O0O0OOO0O00 .root .title ("Billing Software")#line:11
        O0O0000000O0OO000 ="#badc57"#line:12
        OO0O00O0OOO0O000O =Label (OOO0O0O0O0OOO0O00 .root ,text ="Billing Software",font =('times new roman',30 ,'bold'),pady =2 ,bd =12 ,bg ="#badc57",fg ="Black",relief =GROOVE )#line:13
        OO0O00O0OOO0O000O .pack (fill =X )#line:14
        OOO0O0O0O0OOO0O00 .sanitizer =IntVar ()#line:16
        OOO0O0O0O0OOO0O00 .mask =IntVar ()#line:17
        OOO0O0O0O0OOO0O00 .hand_gloves =IntVar ()#line:18
        OOO0O0O0O0OOO0O00 .dettol =IntVar ()#line:19
        OOO0O0O0O0OOO0O00 .newsprin =IntVar ()#line:20
        OOO0O0O0O0OOO0O00 .thermal_gun =IntVar ()#line:21
        OOO0O0O0O0OOO0O00 .rice =IntVar ()#line:23
        OOO0O0O0O0OOO0O00 .food_oil =IntVar ()#line:24
        OOO0O0O0O0OOO0O00 .wheat =IntVar ()#line:25
        OOO0O0O0O0OOO0O00 .daal =IntVar ()#line:26
        OOO0O0O0O0OOO0O00 .flour =IntVar ()#line:27
        OOO0O0O0O0OOO0O00 .maggi =IntVar ()#line:28
        OOO0O0O0O0OOO0O00 .sprite =IntVar ()#line:30
        OOO0O0O0O0OOO0O00 .limka =IntVar ()#line:31
        OOO0O0O0O0OOO0O00 .mazza =IntVar ()#line:32
        OOO0O0O0O0OOO0O00 .coke =IntVar ()#line:33
        OOO0O0O0O0OOO0O00 .fanta =IntVar ()#line:34
        OOO0O0O0O0OOO0O00 .mountain_duo =IntVar ()#line:35
        OOO0O0O0O0OOO0O00 .medical_price =StringVar ()#line:37
        OOO0O0O0O0OOO0O00 .grocery_price =StringVar ()#line:38
        OOO0O0O0O0OOO0O00 .cold_drinks_price =StringVar ()#line:39
        OOO0O0O0O0OOO0O00 .c_name =StringVar ()#line:41
        OOO0O0O0O0OOO0O00 .c_phone =StringVar ()#line:42
        OOO0O0O0O0OOO0O00 .bill_no =StringVar ()#line:43
        O0O0OOOO000O0OO0O =random .randint (1000 ,9999 )#line:44
        OOO0O0O0O0OOO0O00 .bill_no .set (str (O0O0OOOO000O0OO0O ))#line:45
        OOO0O0O0O0OOO0O00 .search_bill =StringVar ()#line:46
        OOO0O0O0O0OOO0O00 .medical_tax =StringVar ()#line:48
        OOO0O0O0O0OOO0O00 .grocery_tax =StringVar ()#line:49
        OOO0O0O0O0OOO0O00 .cold_drinks_tax =StringVar ()#line:50
        OOO00OOO0OO00O00O =LabelFrame (OOO0O0O0O0OOO0O00 .root ,text ="Customer Details",font =('times new roman',15 ,'bold'),bd =10 ,fg ="Black",bg ="#badc57")#line:52
        OOO00OOO0OO00O00O .place (x =0 ,y =80 ,relwidth =1 )#line:53
        OO0000O0O00O000O0 =Label (OOO00OOO0OO00O00O ,text ="Customer Name:",bg =O0O0000000O0OO000 ,font =('times new roman',15 ,'bold'))#line:54
        OO0000O0O00O000O0 .grid (row =0 ,column =0 ,padx =20 ,pady =5 )#line:55
        O00OO0O0000OOO000 =Entry (OOO00OOO0OO00O00O ,width =15 ,textvariable =OOO0O0O0O0OOO0O00 .c_name ,font ='arial 15',bd =7 ,relief =GROOVE )#line:56
        O00OO0O0000OOO000 .grid (row =0 ,column =1 ,pady =5 ,padx =10 )#line:57
        OO0000O000000O0OO =Label (OOO00OOO0OO00O00O ,text ="Customer Phone:",bg ="#badc57",font =('times new roman',15 ,'bold'))#line:59
        OO0000O000000O0OO .grid (row =0 ,column =2 ,padx =20 ,pady =5 )#line:60
        OO0O0OO00O0O0OOOO =Entry (OOO00OOO0OO00O00O ,width =15 ,textvariable =OOO0O0O0O0OOO0O00 .c_phone ,font ='arial 15',bd =7 ,relief =GROOVE )#line:61
        OO0O0OO00O0O0OOOO .grid (row =0 ,column =3 ,pady =5 ,padx =10 )#line:62
        OOO00O0O0O00OO0O0 =Label (OOO00OOO0OO00O00O ,text ="Bill Number:",bg ="#badc57",font =('times new roman',15 ,'bold'))#line:64
        OOO00O0O0O00OO0O0 .grid (row =0 ,column =4 ,padx =20 ,pady =5 )#line:65
        OO0OO0OO0O00000O0 =Entry (OOO00OOO0OO00O00O ,width =15 ,textvariable =OOO0O0O0O0OOO0O00 .search_bill ,font ='arial 15',bd =7 ,relief =GROOVE )#line:66
        OO0OO0OO0O00000O0 .grid (row =0 ,column =5 ,pady =5 ,padx =10 )#line:67
        O0O0O0OO00OOOOOOO =Button (OOO00OOO0OO00O00O ,text ="Search",command =OOO0O0O0O0OOO0O00 .find_bill ,width =10 ,bd =7 ,font =('arial',12 ,'bold'),relief =GROOVE )#line:69
        O0O0O0OO00OOOOOOO .grid (row =0 ,column =6 ,pady =5 ,padx =10 )#line:70
        O0OOO00OO0000O00O =LabelFrame (OOO0O0O0O0OOO0O00 .root ,text ="Medical Purpose",font =('times new roman',15 ,'bold'),bd =10 ,fg ="Black",bg ="#badc57")#line:73
        O0OOO00OO0000O00O .place (x =5 ,y =180 ,width =325 ,height =380 )#line:74
        O0O0O0O0OO0O0O00O =Label (O0OOO00OO0000O00O ,text ="Sanitizer",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:76
        O0O0O0O0OO0O0O00O .grid (row =0 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:77
        O0O000000O000O0OO =Entry (O0OOO00OO0000O00O ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .sanitizer ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:78
        O0O000000O000O0OO .grid (row =0 ,column =1 ,padx =10 ,pady =10 )#line:79
        O000000OOOO0000O0 =Label (O0OOO00OO0000O00O ,text ="Mask",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:81
        O000000OOOO0000O0 .grid (row =1 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:82
        OO00OO0O00O0000OO =Entry (O0OOO00OO0000O00O ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .mask ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:83
        OO00OO0O00O0000OO .grid (row =1 ,column =1 ,padx =10 ,pady =10 )#line:84
        O0O0000OOOO0O0O0O =Label (O0OOO00OO0000O00O ,text ="Hand Gloves",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:86
        O0O0000OOOO0O0O0O .grid (row =2 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:87
        OOOO0O0O00O00O00O =Entry (O0OOO00OO0000O00O ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .hand_gloves ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:88
        OOOO0O0O00O00O00O .grid (row =2 ,column =1 ,padx =10 ,pady =10 )#line:89
        O00OOO00OOO0000O0 =Label (O0OOO00OO0000O00O ,text ="Dettol",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:91
        O00OOO00OOO0000O0 .grid (row =3 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:92
        O00O0OOOO000OO000 =Entry (O0OOO00OO0000O00O ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .dettol ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:93
        O00O0OOOO000OO000 .grid (row =3 ,column =1 ,padx =10 ,pady =10 )#line:94
        O00000O0O000000O0 =Label (O0OOO00OO0000O00O ,text ="Newsprin",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:96
        O00000O0O000000O0 .grid (row =4 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:97
        O00OO0O0O0OO0O0O0 =Entry (O0OOO00OO0000O00O ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .newsprin ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:98
        O00OO0O0O0OO0O0O0 .grid (row =4 ,column =1 ,padx =10 ,pady =10 )#line:99
        O0OO00O00OO00000O =Label (O0OOO00OO0000O00O ,text ="Thermal Gun",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:101
        O0OO00O00OO00000O .grid (row =5 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:102
        OOO0O0OO0000O0OOO =Entry (O0OOO00OO0000O00O ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .thermal_gun ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:103
        OOO0O0OO0000O0OOO .grid (row =5 ,column =1 ,padx =10 ,pady =10 )#line:104
        OOO000O00O00000O0 =LabelFrame (OOO0O0O0O0OOO0O00 .root ,text ="Grocery Items",font =('times new roman',15 ,'bold'),bd =10 ,fg ="Black",bg ="#badc57")#line:107
        OOO000O00O00000O0 .place (x =340 ,y =180 ,width =325 ,height =380 )#line:108
        OO000O00000O0000O =Label (OOO000O00O00000O0 ,text ="Rice",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:110
        OO000O00000O0000O .grid (row =0 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:111
        OOO000OOOOO00OOOO =Entry (OOO000O00O00000O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .rice ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:112
        OOO000OOOOO00OOOO .grid (row =0 ,column =1 ,padx =10 ,pady =10 )#line:113
        OOOOO00O0O0OO0000 =Label (OOO000O00O00000O0 ,text ="Food Oil",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:115
        OOOOO00O0O0OO0000 .grid (row =1 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:116
        O0O00000O0OO00OOO =Entry (OOO000O00O00000O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .food_oil ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:117
        O0O00000O0OO00OOO .grid (row =1 ,column =1 ,padx =10 ,pady =10 )#line:118
        OO0O0O0OO0O0000OO =Label (OOO000O00O00000O0 ,text ="Wheat",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:120
        OO0O0O0OO0O0000OO .grid (row =2 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:121
        OO0000000OOOOOOOO =Entry (OOO000O00O00000O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .wheat ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:122
        OO0000000OOOOOOOO .grid (row =2 ,column =1 ,padx =10 ,pady =10 )#line:123
        O0OO0OO0OOO0OOOOO =Label (OOO000O00O00000O0 ,text ="Daal",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:125
        O0OO0OO0OOO0OOOOO .grid (row =3 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:126
        OOOO0000OO00O0O0O =Entry (OOO000O00O00000O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .daal ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:127
        OOOO0000OO00O0O0O .grid (row =3 ,column =1 ,padx =10 ,pady =10 )#line:128
        OOO000OOO0O0O0O00 =Label (OOO000O00O00000O0 ,text ="Flour",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:130
        OOO000OOO0O0O0O00 .grid (row =4 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:131
        O0O0000000OOO0O0O =Entry (OOO000O00O00000O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .flour ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:132
        O0O0000000OOO0O0O .grid (row =4 ,column =1 ,padx =10 ,pady =10 )#line:133
        OO00O000OOO000000 =Label (OOO000O00O00000O0 ,text ="Maggi",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:135
        OO00O000OOO000000 .grid (row =5 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:136
        OO0O00OOOO0OO0OOO =Entry (OOO000O00O00000O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .maggi ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:137
        OO0O00OOOO0OO0OOO .grid (row =5 ,column =1 ,padx =10 ,pady =10 )#line:138
        OO0000O0O000OO0O0 =LabelFrame (OOO0O0O0O0OOO0O00 .root ,text ="Cold Drinks",font =('times new roman',15 ,'bold'),bd =10 ,fg ="Black",bg ="#badc57")#line:141
        OO0000O0O000OO0O0 .place (x =670 ,y =180 ,width =325 ,height =380 )#line:142
        OO000OOOOO00OOO0O =Label (OO0000O0O000OO0O0 ,text ="Sprite",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:144
        OO000OOOOO00OOO0O .grid (row =0 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:145
        O0O000O0O00OO00O0 =Entry (OO0000O0O000OO0O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .sprite ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:146
        O0O000O0O00OO00O0 .grid (row =0 ,column =1 ,padx =10 ,pady =10 )#line:147
        O0OO0OO00O0OO0OO0 =Label (OO0000O0O000OO0O0 ,text ="Limka",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:149
        O0OO0OO00O0OO0OO0 .grid (row =1 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:150
        O0OOOO000O00OO0O0 =Entry (OO0000O0O000OO0O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .limka ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:151
        O0OOOO000O00OO0O0 .grid (row =1 ,column =1 ,padx =10 ,pady =10 )#line:152
        OO00O00O000O0OOO0 =Label (OO0000O0O000OO0O0 ,text ="Mazza",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:154
        OO00O00O000O0OOO0 .grid (row =2 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:155
        OO0000000OOOOOOOO =Entry (OO0000O0O000OO0O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .mazza ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:156
        OO0000000OOOOOOOO .grid (row =2 ,column =1 ,padx =10 ,pady =10 )#line:157
        OOO00000OO000000O =Label (OO0000O0O000OO0O0 ,text ="Coke",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:159
        OOO00000OO000000O .grid (row =3 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:160
        OOO0000OOOO0O0000 =Entry (OO0000O0O000OO0O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .coke ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:161
        OOO0000OOOO0O0000 .grid (row =3 ,column =1 ,padx =10 ,pady =10 )#line:162
        O00000OO000OOOOOO =Label (OO0000O0O000OO0O0 ,text ="Fanta",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:164
        O00000OO000OOOOOO .grid (row =4 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:165
        OO00O000OOO0OOO0O =Entry (OO0000O0O000OO0O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .fanta ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:166
        OO00O000OOO0OOO0O .grid (row =4 ,column =1 ,padx =10 ,pady =10 )#line:167
        O00OO0O0O0OO00000 =Label (OO0000O0O000OO0O0 ,text ="Mountain Duo",font =('times new roman',16 ,'bold'),bg ="#badc57",fg ="black")#line:169
        O00OO0O0O0OO00000 .grid (row =5 ,column =0 ,padx =10 ,pady =10 ,sticky ='W')#line:170
        OOOOO0OOO000OO0O0 =Entry (OO0000O0O000OO0O0 ,width =10 ,textvariable =OOO0O0O0O0OOO0O00 .mountain_duo ,font =('times new roman',16 ,'bold'),bd =5 ,relief =GROOVE )#line:171
        OOOOO0OOO000OO0O0 .grid (row =5 ,column =1 ,padx =10 ,pady =10 )#line:172
        OOO0OO000OO0O0O00 =Frame (OOO0O0O0O0OOO0O00 .root ,bd =10 ,relief =GROOVE )#line:175
        OOO0OO000OO0O0O00 .place (x =1010 ,y =180 ,width =350 ,height =380 )#line:176
        O0000000O0O0O0OOO =Label (OOO0OO000OO0O0O00 ,text ="Bill Area",font ='arial 15 bold',bd =7 ,relief =GROOVE )#line:178
        O0000000O0O0O0OOO .pack (fill =X )#line:179
        O0OO000O0O0000O00 =Scrollbar (OOO0OO000OO0O0O00 ,orient =VERTICAL )#line:180
        OOO0O0O0O0OOO0O00 .txtarea =Text (OOO0OO000OO0O0O00 ,yscrollcommand =O0OO000O0O0000O00 .set )#line:181
        O0OO000O0O0000O00 .pack (side =RIGHT ,fill =Y )#line:182
        O0OO000O0O0000O00 .config (command =OOO0O0O0O0OOO0O00 .txtarea .yview )#line:183
        OOO0O0O0O0OOO0O00 .txtarea .pack (fill =BOTH ,expand =1 )#line:184
        O0OOO0O00O0O0OO00 =LabelFrame (OOO0O0O0O0OOO0O00 .root ,text ="Bill Area",font =('times new roman',14 ,'bold'),bd =10 ,fg ="Black",bg ="#badc57")#line:187
        O0OOO0O00O0O0OO00 .place (x =0 ,y =560 ,relwidth =1 ,height =140 )#line:188
        OOO00000O0O0O0000 =Label (O0OOO0O00O0O0OO00 ,text ="Total Medical Price",font =('times new roman',14 ,'bold'),bg ="#badc57",fg ="black")#line:190
        OOO00000O0O0O0000 .grid (row =0 ,column =0 ,padx =20 ,pady =1 ,sticky ='W')#line:191
        OOOOO0O00O0O0OOO0 =Entry (O0OOO0O00O0O0OO00 ,width =18 ,textvariable =OOO0O0O0O0OOO0O00 .medical_price ,font ='arial 10 bold',bd =7 ,relief =GROOVE )#line:192
        OOOOO0O00O0O0OOO0 .grid (row =0 ,column =1 ,padx =18 ,pady =1 )#line:193
        O00OOO0O000O000OO =Label (O0OOO0O00O0O0OO00 ,text ="Total Grocery Price",font =('times new roman',14 ,'bold'),bg ="#badc57",fg ="black")#line:195
        O00OOO0O000O000OO .grid (row =1 ,column =0 ,padx =20 ,pady =1 ,sticky ='W')#line:196
        OO0000O0O0OOOOOO0 =Entry (O0OOO0O00O0O0OO00 ,width =18 ,textvariable =OOO0O0O0O0OOO0O00 .grocery_price ,font ='arial 10 bold',bd =7 ,relief =GROOVE )#line:197
        OO0000O0O0OOOOOO0 .grid (row =1 ,column =1 ,padx =18 ,pady =1 )#line:198
        O00O0OOOOOO000O0O =Label (O0OOO0O00O0O0OO00 ,text ="Total Cold Drinks Price",font =('times new roman',14 ,'bold'),bg ="#badc57",fg ="black")#line:200
        O00O0OOOOOO000O0O .grid (row =2 ,column =0 ,padx =20 ,pady =1 ,sticky ='W')#line:201
        OO0O0OO00000OOO0O =Entry (O0OOO0O00O0O0OO00 ,width =18 ,textvariable =OOO0O0O0O0OOO0O00 .cold_drinks_price ,font ='arial 10 bold',bd =7 ,relief =GROOVE )#line:202
        OO0O0OO00000OOO0O .grid (row =2 ,column =1 ,padx =18 ,pady =1 )#line:203
        OO00O0O0000000O00 =Label (O0OOO0O00O0O0OO00 ,text ="Medical Tax",font =('times new roman',14 ,'bold'),bg ="#badc57",fg ="black")#line:205
        OO00O0O0000000O00 .grid (row =0 ,column =2 ,padx =20 ,pady =1 ,sticky ='W')#line:206
        OOO0O0OOO0O0OO0O0 =Entry (O0OOO0O00O0O0OO00 ,width =18 ,textvariable =OOO0O0O0O0OOO0O00 .medical_tax ,font ='arial 10 bold',bd =7 ,relief =GROOVE )#line:207
        OOO0O0OOO0O0OO0O0 .grid (row =0 ,column =3 ,padx =18 ,pady =1 )#line:208
        OO00OO00OOOOOOO0O =Label (O0OOO0O00O0O0OO00 ,text ="Grocery Tax",font =('times new roman',14 ,'bold'),bg ="#badc57",fg ="black")#line:210
        OO00OO00OOOOOOO0O .grid (row =1 ,column =2 ,padx =20 ,pady =1 ,sticky ='W')#line:211
        O0OO0OO00O00OO000 =Entry (O0OOO0O00O0O0OO00 ,width =18 ,textvariable =OOO0O0O0O0OOO0O00 .grocery_tax ,font ='arial 10 bold',bd =7 ,relief =GROOVE )#line:212
        O0OO0OO00O00OO000 .grid (row =1 ,column =3 ,padx =18 ,pady =1 )#line:213
        OO0OOO0OO0OOOOOOO =Label (O0OOO0O00O0O0OO00 ,text ="Cold Drinks Tax",font =('times new roman',14 ,'bold'),bg ="#badc57",fg ="black")#line:215
        OO0OOO0OO0OOOOOOO .grid (row =2 ,column =2 ,padx =20 ,pady =1 ,sticky ='W')#line:216
        OO000OOOOO0OO0OOO =Entry (O0OOO0O00O0O0OO00 ,width =18 ,textvariable =OOO0O0O0O0OOO0O00 .cold_drinks_tax ,font ='arial 10 bold',bd =7 ,relief =GROOVE )#line:217
        OO000OOOOO0OO0OOO .grid (row =2 ,column =3 ,padx =18 ,pady =1 )#line:218
        OO000O000000O0OO0 =Frame (O0OOO0O00O0O0OO00 ,bd =7 ,relief =GROOVE )#line:221
        OO000O000000O0OO0 .place (x =760 ,width =580 ,height =105 )#line:222
        O0O0O000OOOO0000O =Button (OO000O000000O0OO0 ,command =OOO0O0O0O0OOO0O00 .total ,text ="Total",bg ="#535C68",bd =2 ,fg ="white",pady =15 ,width =12 ,font ='arial 13 bold')#line:224
        O0O0O000OOOO0000O .grid (row =0 ,column =0 ,padx =5 ,pady =5 )#line:225
        O00O0O000OOO0O00O =Button (OO000O000000O0OO0 ,command =OOO0O0O0O0OOO0O00 .bill_area ,text ="Generate Bill",bd =2 ,bg ="#535C68",fg ="white",pady =12 ,width =12 ,font ='arial 13 bold')#line:227
        O00O0O000OOO0O00O .grid (row =0 ,column =1 ,padx =5 ,pady =5 )#line:228
        O0000O000000OO0OO =Button (OO000O000000O0OO0 ,command =OOO0O0O0O0OOO0O00 .clear_data ,text ="Clear",bg ="#535C68",bd =2 ,fg ="white",pady =15 ,width =12 ,font ='arial 13 bold')#line:230
        O0000O000000OO0OO .grid (row =0 ,column =2 ,padx =5 ,pady =5 )#line:231
        OOOO00OOO00OO0O0O =Button (OO000O000000O0OO0 ,command =OOO0O0O0O0OOO0O00 .exit_app ,text ="Exit",bd =2 ,bg ="#535C68",fg ="white",pady =15 ,width =12 ,font ='arial 13 bold')#line:233
        OOOO00OOO00OO0O0O .grid (row =0 ,column =3 ,padx =5 ,pady =5 )#line:234
        OOO0O0O0O0OOO0O00 .welcome_bill ()#line:235
    def total (O0OOO00000O000O00 ):#line:238
        O0OOO00000O000O00 .m_h_g_p =O0OOO00000O000O00 .hand_gloves .get ()*12 #line:239
        O0OOO00000O000O00 .m_s_p =O0OOO00000O000O00 .sanitizer .get ()*2 #line:240
        O0OOO00000O000O00 .m_m_p =O0OOO00000O000O00 .mask .get ()*5 #line:241
        O0OOO00000O000O00 .m_d_p =O0OOO00000O000O00 .dettol .get ()*30 #line:242
        O0OOO00000O000O00 .m_n_p =O0OOO00000O000O00 .newsprin .get ()*5 #line:243
        O0OOO00000O000O00 .m_t_g_p =O0OOO00000O000O00 .thermal_gun .get ()*15 #line:244
        O0OOO00000O000O00 .total_medical_price =float (O0OOO00000O000O00 .m_m_p +O0OOO00000O000O00 .m_h_g_p +O0OOO00000O000O00 .m_d_p +O0OOO00000O000O00 .m_n_p +O0OOO00000O000O00 .m_t_g_p +O0OOO00000O000O00 .m_s_p )#line:245
        O0OOO00000O000O00 .medical_price .set ("Rs. "+str (O0OOO00000O000O00 .total_medical_price ))#line:247
        O0OOO00000O000O00 .c_tax =round ((O0OOO00000O000O00 .total_medical_price *0.05 ),2 )#line:248
        O0OOO00000O000O00 .medical_tax .set ("Rs. "+str (O0OOO00000O000O00 .c_tax ))#line:249
        O0OOO00000O000O00 .g_r_p =O0OOO00000O000O00 .rice .get ()*10 #line:251
        O0OOO00000O000O00 .g_f_o_p =O0OOO00000O000O00 .food_oil .get ()*10 #line:252
        O0OOO00000O000O00 .g_w_p =O0OOO00000O000O00 .wheat .get ()*10 #line:253
        O0OOO00000O000O00 .g_d_p =O0OOO00000O000O00 .daal .get ()*6 #line:254
        O0OOO00000O000O00 .g_f_p =O0OOO00000O000O00 .flour .get ()*8 #line:255
        O0OOO00000O000O00 .g_m_p =O0OOO00000O000O00 .maggi .get ()*5 #line:256
        O0OOO00000O000O00 .total_grocery_price =float (O0OOO00000O000O00 .g_r_p +O0OOO00000O000O00 .g_f_o_p +O0OOO00000O000O00 .g_w_p +O0OOO00000O000O00 .g_d_p +O0OOO00000O000O00 .g_f_p +O0OOO00000O000O00 .g_m_p )#line:257
        O0OOO00000O000O00 .grocery_price .set ("Rs. "+str (O0OOO00000O000O00 .total_grocery_price ))#line:259
        O0OOO00000O000O00 .g_tax =round ((O0OOO00000O000O00 .total_grocery_price *5 ),2 )#line:260
        O0OOO00000O000O00 .grocery_tax .set ("Rs. "+str (O0OOO00000O000O00 .g_tax ))#line:261
        O0OOO00000O000O00 .c_d_s_p =O0OOO00000O000O00 .sprite .get ()*10 #line:263
        O0OOO00000O000O00 .c_d_l_p =O0OOO00000O000O00 .limka .get ()*10 #line:264
        O0OOO00000O000O00 .c_d_m_p =O0OOO00000O000O00 .mazza .get ()*10 #line:265
        O0OOO00000O000O00 .c_d_c_p =O0OOO00000O000O00 .coke .get ()*10 #line:266
        O0OOO00000O000O00 .c_d_f_p =O0OOO00000O000O00 .fanta .get ()*10 #line:267
        O0OOO00000O000O00 .c_m_d =O0OOO00000O000O00 .mountain_duo .get ()*10 #line:268
        O0OOO00000O000O00 .total_cold_drinks_price =float (O0OOO00000O000O00 .c_d_s_p +O0OOO00000O000O00 .c_d_l_p +O0OOO00000O000O00 .c_d_m_p +O0OOO00000O000O00 .c_d_c_p +O0OOO00000O000O00 .c_d_f_p +O0OOO00000O000O00 .c_m_d )#line:269
        O0OOO00000O000O00 .cold_drinks_price .set ("Rs. "+str (O0OOO00000O000O00 .total_cold_drinks_price ))#line:271
        O0OOO00000O000O00 .c_d_tax =round ((O0OOO00000O000O00 .total_cold_drinks_price *0.1 ),2 )#line:272
        O0OOO00000O000O00 .cold_drinks_tax .set ("Rs. "+str (O0OOO00000O000O00 .c_d_tax ))#line:273
        O0OOO00000O000O00 .total_bill =float (O0OOO00000O000O00 .total_medical_price +O0OOO00000O000O00 .total_grocery_price +O0OOO00000O000O00 .total_cold_drinks_price +O0OOO00000O000O00 .c_tax +O0OOO00000O000O00 .g_tax +O0OOO00000O000O00 .c_d_tax )#line:275
    def welcome_bill (O00O0O00OO000O000 ):#line:278
        O00O0O00OO000O000 .txtarea .delete ('1.0',END )#line:279
        O00O0O00OO000O000 .txtarea .insert (END ,"\tWelcome Webcode Retail")#line:280
        O00O0O00OO000O000 .txtarea .insert (END ,f"\n Bill Number:{O00O0O00OO000O000.bill_no.get()}")#line:281
        O00O0O00OO000O000 .txtarea .insert (END ,f"\nCustomer Name:{O00O0O00OO000O000.c_name.get()}")#line:282
        O00O0O00OO000O000 .txtarea .insert (END ,f"\nPhone Number{O00O0O00OO000O000.c_phone.get()}")#line:283
        O00O0O00OO000O000 .txtarea .insert (END ,f"\n================================")#line:284
        O00O0O00OO000O000 .txtarea .insert (END ,f"\nProducts\t\tQTY\t\tPrice")#line:285
    def bill_area (O0OOO00000O00O0OO ):#line:288
        if O0OOO00000O00O0OO .c_name .get ()==" "or O0OOO00000O00O0OO .c_phone .get ()==" ":#line:289
            messagebox .showerror ("Error","Customer Details Are Must")#line:290
        elif O0OOO00000O00O0OO .medical_price .get ()=="Rs. 0.0"and O0OOO00000O00O0OO .grocery_price .get ()=="Rs. 0.0"and O0OOO00000O00O0OO .cold_drinks_price .get ()=="Rs. 0.0":#line:291
            messagebox .showerror ("Error","No Product Purchased")#line:292
        else :#line:293
            O0OOO00000O00O0OO .welcome_bill ()#line:294
        if O0OOO00000O00O0OO .sanitizer .get ()!=0 :#line:296
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Sanitizer\t\t{O0OOO00000O00O0OO.sanitizer.get()}\t\t{O0OOO00000O00O0OO.m_s_p}")#line:297
        if O0OOO00000O00O0OO .mask .get ()!=0 :#line:298
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Sanitizer\t\t{O0OOO00000O00O0OO.mask.get()}\t\t{O0OOO00000O00O0OO.m_m_p}")#line:299
        if O0OOO00000O00O0OO .hand_gloves .get ()!=0 :#line:300
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Hand Gloves\t\t{O0OOO00000O00O0OO.hand_gloves.get()}\t\t{O0OOO00000O00O0OO.m_h_g_p}")#line:301
        if O0OOO00000O00O0OO .dettol .get ()!=0 :#line:302
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Dettol\t\t{O0OOO00000O00O0OO.dettol.get()}\t\t{O0OOO00000O00O0OO.m_d_p}")#line:303
        if O0OOO00000O00O0OO .newsprin .get ()!=0 :#line:304
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Newsprin\t\t{O0OOO00000O00O0OO.newsprin.get()}\t\t{O0OOO00000O00O0OO.m_n_p}")#line:305
        if O0OOO00000O00O0OO .thermal_gun .get ()!=0 :#line:306
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Thermal Gun\t\t{O0OOO00000O00O0OO.sanitizer.get()}\t\t{O0OOO00000O00O0OO.m_t_g_p}")#line:307
        if O0OOO00000O00O0OO .rice .get ()!=0 :#line:309
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Rice\t\t{O0OOO00000O00O0OO.rice.get()}\t\t{O0OOO00000O00O0OO.g_r_p}")#line:310
        if O0OOO00000O00O0OO .food_oil .get ()!=0 :#line:311
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Food Oil\t\t{O0OOO00000O00O0OO.food_oil.get()}\t\t{O0OOO00000O00O0OO.g_f_o_p}")#line:312
        if O0OOO00000O00O0OO .wheat .get ()!=0 :#line:313
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Wheat\t\t{O0OOO00000O00O0OO.wheat.get()}\t\t{O0OOO00000O00O0OO.g_w_p}")#line:314
        if O0OOO00000O00O0OO .daal .get ()!=0 :#line:315
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Daal\t\t{O0OOO00000O00O0OO.daal.get()}\t\t{O0OOO00000O00O0OO.g_d_p}")#line:316
        if O0OOO00000O00O0OO .flour .get ()!=0 :#line:317
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Flour\t\t{O0OOO00000O00O0OO.flour.get()}\t\t{O0OOO00000O00O0OO.g_f_p}")#line:318
        if O0OOO00000O00O0OO .maggi .get ()!=0 :#line:319
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Maggi\t\t{O0OOO00000O00O0OO.maggi.get()}\t\t{O0OOO00000O00O0OO.g_m_p}")#line:320
        if O0OOO00000O00O0OO .sprite .get ()!=0 :#line:322
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Sprite\t\t{O0OOO00000O00O0OO.sprite.get()}\t\t{O0OOO00000O00O0OO.c_d_s_p}")#line:323
        if O0OOO00000O00O0OO .limka .get ()!=0 :#line:324
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Sanitizer\t\t{O0OOO00000O00O0OO.limka.get()}\t\t{O0OOO00000O00O0OO.c_d_l_p}")#line:325
        if O0OOO00000O00O0OO .mazza .get ()!=0 :#line:326
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Mazza\t\t{O0OOO00000O00O0OO.mazza.get()}\t\t{O0OOO00000O00O0OO.c_d_m_p}")#line:327
        if O0OOO00000O00O0OO .coke .get ()!=0 :#line:328
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Dettol\t\t{O0OOO00000O00O0OO.coke.get()}\t\t{O0OOO00000O00O0OO.c_d_c_p}")#line:329
        if O0OOO00000O00O0OO .fanta .get ()!=0 :#line:330
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Fanta\t\t{O0OOO00000O00O0OO.newsprin.get()}\t\t{O0OOO00000O00O0OO.c_d_f_p}")#line:331
        if O0OOO00000O00O0OO .mountain_duo .get ()!=0 :#line:332
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Mountain Duo\t\t{O0OOO00000O00O0OO.sanitizer.get()}\t\t{O0OOO00000O00O0OO.c_m_d}")#line:333
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n--------------------------------")#line:334
        if O0OOO00000O00O0OO .medical_tax .get ()!='0.0':#line:336
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Medical Tax\t\t\t{O0OOO00000O00O0OO.medical_tax.get()}")#line:337
        if O0OOO00000O00O0OO .grocery_tax .get ()!='0.0':#line:338
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Grocery Tax\t\t\t{O0OOO00000O00O0OO.grocery_tax.get()}")#line:339
        if O0OOO00000O00O0OO .cold_drinks_tax .get ()!='0.0':#line:340
            O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Cold Drinks Tax\t\t\t{O0OOO00000O00O0OO.cold_drinks_tax.get()}")#line:341
        O0OOO00000O00O0OO .txtarea .insert (END ,f"\n Total Bil:\t\t\t Rs.{O0OOO00000O00O0OO.total_bill}")#line:343
        O0OOO00000O00O0OO .txtarea .insert (END ,f"\n--------------------------------")#line:344
        O0OOO00000O00O0OO .save_bill ()#line:345
    def save_bill (O0O000O00OO00OO00 ):#line:348
        OOO000OOO0OO00O0O =messagebox .askyesno ("Save Bill","Do you want to save the bill?")#line:349
        if OOO000OOO0OO00O0O >0 :#line:350
            O0O000O00OO00OO00 .bill_data =O0O000O00OO00OO00 .txtarea .get ('1.0',END )#line:351
            O00OOO00O0000000O =open ("bills/"+str (O0O000O00OO00OO00 .bill_no .get ())+".txt","w")#line:352
            O00OOO00O0000000O .write (O0O000O00OO00OO00 .bill_data )#line:353
            O00OOO00O0000000O .close ()#line:354
            messagebox .showinfo ("Saved",f"Bill no:{O0O000O00OO00OO00.bill_no.get()} Saved Successfully")#line:355
        else :#line:356
           return #line:357
    def find_bill (OO000O0OOOO000OOO ):#line:360
        O00OOO0O0000O0O0O ="no"#line:361
        for OOO0O000O00O00O0O in os .listdir ("bills/"):#line:362
            if OOO0O000O00O00O0O .split ('.')[0 ]==OO000O0OOOO000OOO .search_bill .get ():#line:363
                O0000OOO0OOOO000O =open (f"bills/{OOO0O000O00O00O0O}","r")#line:364
                OO000O0OOOO000OOO .txtarea .delete ("1.0",END )#line:365
                for O00O0O00OO0OO0O00 in O0000OOO0OOOO000O :#line:366
                    OO000O0OOOO000OOO .txtarea .insert (END ,O00O0O00OO0OO0O00 )#line:367
                    O0000OOO0OOOO000O .close ()#line:368
                O00OOO0O0000O0O0O ="yes"#line:369
        if O00OOO0O0000O0O0O =="no":#line:370
            messagebox .showerror ("Error","Invalid Bill No")#line:371
    def clear_data (OOOOO0O00O0000O00 ):#line:374
        O00OO00OOO0O00OO0 =messagebox .askyesno ("Clear","Do you really want to Clear?")#line:375
        if O00OO00OOO0O00OO0 >0 :#line:376
            OOOOO0O00O0000O00 .sanitizer .set (0 )#line:377
            OOOOO0O00O0000O00 .mask .set (0 )#line:378
            OOOOO0O00O0000O00 .hand_gloves .set (0 )#line:379
            OOOOO0O00O0000O00 .dettol .set (0 )#line:380
            OOOOO0O00O0000O00 .newsprin .set (0 )#line:381
            OOOOO0O00O0000O00 .thermal_gun .set (0 )#line:382
            OOOOO0O00O0000O00 .rice .set (0 )#line:384
            OOOOO0O00O0000O00 .food_oil .set (0 )#line:385
            OOOOO0O00O0000O00 .wheat .set (0 )#line:386
            OOOOO0O00O0000O00 .daal .set (0 )#line:387
            OOOOO0O00O0000O00 .flour .set (0 )#line:388
            OOOOO0O00O0000O00 .maggi .set (0 )#line:389
            OOOOO0O00O0000O00 .sprite .set (0 )#line:391
            OOOOO0O00O0000O00 .limka .set (0 )#line:392
            OOOOO0O00O0000O00 .mazza .set (0 )#line:393
            OOOOO0O00O0000O00 .coke .set (0 )#line:394
            OOOOO0O00O0000O00 .fanta .set (0 )#line:395
            OOOOO0O00O0000O00 .mountain_duo .set (0 )#line:396
            OOOOO0O00O0000O00 .medical_price .set ("")#line:398
            OOOOO0O00O0000O00 .grocery_price .set ("")#line:399
            OOOOO0O00O0000O00 .cold_drinks_price .set ("")#line:400
            OOOOO0O00O0000O00 .medical_tax .set ("")#line:402
            OOOOO0O00O0000O00 .grocery_tax .set ("")#line:403
            OOOOO0O00O0000O00 .cold_drinks_tax .set ("")#line:404
            OOOOO0O00O0000O00 .c_name .set ("")#line:406
            OOOOO0O00O0000O00 .c_phone .set ("")#line:407
            OOOOO0O00O0000O00 .bill_no .set ("")#line:409
            OOOOOOOO0OO0OOOO0 =random .randint (1000 ,9999 )#line:410
            OOOOO0O00O0000O00 .bill_no .set (str (OOOOOOOO0OO0OOOO0 ))#line:411
            OOOOO0O00O0000O00 .search_bill .set ("")#line:413
            OOOOO0O00O0000O00 .welcome_bill ()#line:414
    def exit_app (OO00OOO0O0OOOO000 ):#line:417
        OOOOOOOO00OOO0O00 =messagebox .askyesno ("Exit","Do you really want to exit?")#line:418
        if OOOOOOOO00OOO0O00 >0 :#line:419
            OO00OOO0O0OOOO000 .root .destroy ()#line:420
root =Tk ()#line:423
obj =Bill_App (root )#line:424
root .mainloop ()#line:425
