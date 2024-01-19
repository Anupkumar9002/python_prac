import time
timeStamp = time.strftime('%H:%M:%S')
print(timeStamp)
hour = int(time.strftime('%H'))
print(hour)
name="anup"
if(hour<12 and hour>0):
    print(f"good morning {name}")
elif(hour>=12 and hour<=20):
    print(f"good afternoon {name}")   
else:
    print(f"good night{name}")  



