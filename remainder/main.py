import pandas as pd
from plyer import notification
import time

#remainder is a File name
#Enter Your remainder.xlsx file location 
#Don't Forget to put the .xlsx in the end of the file name in your path
data = pd.read_excel (r'remainder.xlsx')



df = pd.DataFrame(data,columns=['Time','Task'])    
istime = False
while True:
    #This is For The time
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S %p", t).lstrip('0')

    if  current_time in df.values and istime:
                index = df.index
                condition = df["Time"] == current_time
                li = index[condition]
                lst = li.tolist()
                #This is For the Notification
                notification.notify(title = str(df.values[lst,1]).replace("['", "").replace("']", "").capitalize()+" Time",message = 'Your Task',timeout = 15)
                istime = False
                time.sleep(15)
    else:
        istime = True
        time.sleep(1)
        
