from Email import SendMail
from Request import Fetch
import pytz
from datetime import *

def cvtTime(n):
    n+=(60*60*5)+30*60
    ret = str(timedelta(seconds = n))
    return ret.split()[2]

def Read(data):
    ret = []
    ret.append(data['name'])
    ret.append("0"+cvtTime(data['sys']['sunrise']))
    ret.append(cvtTime(data['sys']['sunset']))
    ret.append(str(round(data['main']['temp']-273.15,2)))
    ret.append(str(data['main']['humidity'])+"%")
    ret.append(data['weather'][0]['description'])
    return ret

def Work():
    IST = pytz.timezone('Asia/Kolkata')
    curr = datetime.now(IST).strftime("%H:%M:%S")
    if (curr[:2]=="08" or curr[:2]=="12" or curr[:2]=="16") and curr[3:5]=="00" and curr[6:8]=="00" :
        data = Fetch()
        final = ["Hi Mandeep, Here's What Current Weather looks like"]
        for dat in data :
            ret = Read(dat)
            final.append("Station Name : "+ret[0])
            final.append("Sunrise : "+ret[1])
            final.append("Sunset : "+ret[2])
            final.append("Temperature : "+ret[3])
            final.append("Humidity : "+ret[4])
            final.append("Summary : "+ret[5])
            final.append('\n')
        final.pop()
        final_msg = '\n'.join(final)
        SendMail(final_msg)
while True :
    Work()
