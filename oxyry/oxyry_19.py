import random #line:1
brain_teasers =[("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?","an echo"),("What comes once in a minute, twice in a moment, but never in a thousand years?","the letter 'm'"),("The more you take, the more you leave behind. What am I?","footsteps"),("What has keys but can't open locks?","a piano"),("You see a boat filled with people. It has not sunk, but when you look again you don’t see a single person on the boat. Why?","all the people were married"),]#line:11
def play_game ():#line:14
    O0OOOO0000OOO0O00 =0 #line:15
    random .shuffle (brain_teasers )#line:17
    print ("Welcome to the Brain Teaser Game!")#line:19
    print ("Try to answer the following brain teasers:\n")#line:20
    for OOO0OO000OOOO00OO ,O0O0O000000000O0O in brain_teasers :#line:22
        print ("Question:",OOO0OO000OOOO00OO )#line:23
        OO0000OOOO000OOO0 =input ("Your Answer: ").lower ()#line:24
        if OO0000OOOO000OOO0 ==O0O0O000000000O0O :#line:26
            print ("Correct!\n")#line:27
            O0OOOO0000OOO0O00 +=1 #line:28
        else :#line:29
            print (f"Sorry, the correct answer is '{O0O0O000000000O0O}'.\n")#line:30
    print ("Game Over! Your final score:",O0OOOO0000OOO0O00 )#line:32
if __name__ =="__main__":#line:35
    play_game ()