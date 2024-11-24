import ipaddress #line:1
def calculate_network_info (OOOOO0O00OO0OO00O ,OO00O0000OO0O0OOO ):#line:4
    O00OO00O0OO0OO0OO =ipaddress .IPv4Network (f"{OOOOO0O00OO0OO00O}/{OO00O0000OO0O0OOO}",strict =False )#line:5
    OOO0OO0O0OOO0OOO0 =O00OO00O0OO0OO0OO .network_address #line:7
    O00000O0O0O0OO0OO =O00OO00O0OO0OO0OO .broadcast_address #line:8
    OOO00O00OO0OOO0O0 =O00OO00O0OO0OO0OO .num_addresses #line:9
    OOOO0OO00OO0O00OO =max (OOO00O00OO0OOO0O0 -2 ,0 )#line:10
    O0O0OOO0O0OO00O00 =OOO0OO0O0OOO0OOO0 +1 if OOOO0OO00OO0O00OO >0 else None #line:11
    OOO00OO0OO0OO0O00 =O00000O0O0O0OO0OO -1 if OOOO0OO00OO0O00OO >0 else None #line:12
    O00OO0O00OO00O0OO ={"IP Address":OOOOO0O00OO0OO00O ,"Subnet Mask":OO00O0000OO0O0OOO ,"Network Address":str (OOO0OO0O0OOO0OOO0 ),"Broadcast Address":str (O00000O0O0O0OO0OO ),"Range of IP addresses":f"{OOO0OO0O0OOO0OOO0} - {O00000O0O0O0OO0OO}","Usable Host IP Range":(f"{O0O0OOO0O0OO00O00} - {OOO00OO0OO0OO0O00}"if OOOO0OO00OO0O00OO >0 else "N/A"),"Total Hosts":OOO00O00OO0OOO0O0 ,"Usable Hosts":OOOO0OO00OO0O00OO ,}#line:25
    return O00OO0O00OO00O0OO #line:27
def main ():#line:30
    try :#line:31
        O0O00000OOOO000OO =input ("Enter IP address: ")#line:32
        OO000OOOOOO0O000O =input ("Enter subnet mask: ")#line:33
        OO00OO00OO0O00O0O =calculate_network_info (O0O00000OOOO000OO ,OO000OOOOOO0O000O )#line:35
        print ("\nNetwork Information:")#line:37
        for OO0O0000000OO0OOO ,O0000OOOO000OO0OO in OO00OO00OO0O00O0O .items ():#line:38
            print (f"{OO0O0000000OO0OOO}: {O0000OOOO000OO0OO}")#line:39
    except ValueError as OOOOOO00O00OO0O0O :#line:41
        print (f"Error: {OOOOOO00O00OO0O0O}")#line:42
if __name__ =="__main__":#line:45
    main ()