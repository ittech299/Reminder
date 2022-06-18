import pandas as pd
from plyer import notification
import time


data = pd.read_excel (r'remainder.xlsx')



df = pd.DataFrame(data,columns=['Time','Task'])    
istime = False
while True:
    t = time.localtime()
    current_time = time.strftime("%I:%M:%S %p", t).lstrip('0')

    if  current_time in df.values and istime:
                index = df.index
                condition = df["Time"] == current_time
                li = index[condition]
                lst = li.tolist()
                notification.notify(title = str(df.values[lst,1]).replace("['", "").replace("']", "").capitalize()+" Time",message = 'Your Task',timeout = 15)
                istime = False
                time.sleep(15)
    else:
        istime = True
        time.sleep(1)
        

    
                
            
    
        


  

  # index = df.index
  # condition = df["Time"] == current_time
  # li = index[condition]
  # lst = li.tolist()
  # print(df.values[lst,1], current_time)
    
        





#First  Method
#*******
#if "12:39:40" in df.values:
#        
#        #break
#else:
#        print(current_time)
#

#print(df.values[0,1])