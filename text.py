import json,asyncio,datetime

with open("setting.json",'r',encoding='utf-8') as jfile:
    jdata=json.load(jfile)

now = datetime.datetime.now()
print(now)
datetime_str = jdata['Time']
print(datetime_str)
dt = datetime.datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')

print((dt - now).total_seconds())