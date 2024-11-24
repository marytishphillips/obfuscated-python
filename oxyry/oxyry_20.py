import psutil #line:1
def get_cpu_temperature ()->float |str :#line:6
    ""#line:11
    try :#line:12
        OO00OOO0OOOO0OO0O =psutil .sensors_temperatures ()['coretemp'][0 ].current #line:15
        return OO00OOO0OOOO0OO0O #line:16
    except (KeyError ,IndexError ):#line:17
        return "NA"#line:19
def get_ram_and_cpu_util ()->list :#line:22
    ""#line:27
    O00OO000OOO0O0OOO =psutil .virtual_memory ()#line:28
    return [O00OO000OOO0O0OOO [0 ]//(1024 *1024 ),O00OO000OOO0O0OOO [2 ],psutil .cpu_percent (interval =4 ,percpu =True )]#line:35
cpu_temperature =get_cpu_temperature ()#line:39
system_utils =get_ram_and_cpu_util ()#line:42
if (type (system_utils [2 ])==list ):#line:45
    cpu_percentage =""#line:46
    for i in system_utils [2 ]:#line:47
        cpu_percentage +="{}%, ".format (i )#line:48
else :#line:49
    cpu_percentage ='{}%'.format (system_utils [2 ])#line:50
print (f"Current CPU Temperature in Celsius is {cpu_temperature}°C, with percentage utilized being at {cpu_percentage}")#line:53
print (f"Current RAM utilization is {system_utils[1]}% of {system_utils[0]} MB")