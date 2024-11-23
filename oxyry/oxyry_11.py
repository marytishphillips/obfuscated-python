import time #line:2
import os #line:3
def pomodoro_timer_unix (work_duration =25 ,break_duration =5 ,cycles =4 ):#line:5
    for O0000OO0OOOO0OOO0 in range (cycles ):#line:6
        print (f"Cycle {O0000OO0OOOO0OOO0 + 1}/{cycles}: Start working for {work_duration} minutes.")#line:7
        time .sleep (work_duration *60 )#line:8
        os .system ('echo -e "\a"')#line:9
        print ("Time's up! Take a break.")#line:10
        print (f"Break time! Relax for {break_duration} minutes.")#line:12
        time .sleep (break_duration *60 )#line:13
        os .system ('echo -e "\a"')#line:14
        print ("Break is over! Back to work.")#line:15
    print ("All cycles completed! Great job!")#line:17
if __name__ =="__main__":#line:19
    work_duration =int (input ("Enter work duration in minutes (default is 25): ")or 25 )#line:20
    break_duration =int (input ("Enter break duration in minutes (default is 5): ")or 5 )#line:21
    cycles =int (input ("Enter number of cycles (default is 4): ")or 4 )#line:22
    pomodoro_timer_unix (work_duration ,break_duration ,cycles )