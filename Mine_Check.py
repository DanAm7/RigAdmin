import subprocess
import time
import os
from datetime import datetime, date

today = date.today()
phoenix_path = r'C:\Users\M-PC\Desktop\1\PhoenixMiner.exe'
phoenix_2_path = r"C:\Users\M-PC\Desktop\1\PhoenixMiner_2.exe"
Trex_path = r"C:\Users\M-PC\Desktop\Luncher_AS_Admin.bat"
i = 0
try:
    while True:
        time.sleep(120)
        s = subprocess.check_output('tasklist', shell=True)
        s = s.decode()
        if "PhoenixMiner.exe" in s:
            print(datetime.now().strftime("%H:%M:%S"), '  Phoenix check pass!')
        else:   
            i += 1
            if i >= 5:
                print(datetime.now().strftime("%H:%M:%S"), '  Phoenix Fail Restarting!')
                time.sleep(10)
                subprocess.call(["shutdown", "/r"])
            else:
                os.startfile(phoenix_path)
                

        if "PhoenixMiner_2.exe" in s:
            print(datetime.now().strftime("%H:%M:%S"), '  Phoenix_2 check pass!')
        else:   
            i += 1
            if i >= 5:
                print(datetime.now().strftime("%H:%M:%S"), '  Phoenix_2 Fail Restarting!')
                time.sleep(10)
                subprocess.call(["shutdown", "/r"])
            else:
                os.startfile(phoenix_2_path)

        # if "t-rex.exe" in s:
        #     print(datetime.now().strftime("%H:%M:%S"), '  Trex check pass!')
        # else:   
        #     print(datetime.now().strftime("%H:%M:%S"), '  Trex Fail restarting!')
        #     f = open('Crush Report' + ' ' + datetime.now().strftime("%H_%M_%S") + '.txt', 'w')
        #     f.write('T-rex Crush!')
        #     f.close()
        #     time.sleep(10)
        #     subprocess.call(["shutdown", "/r"])
        if "t-rex.exe" in s:
                print(datetime.now().strftime("%H:%M:%S"), '  Trex check pass!')
        else:   
            i += 1
            if i >= 5:
                print(datetime.now().strftime("%H:%M:%S"), '  Trex Fail restarting!')
                time.sleep(10)
                subprocess.call(["shutdown", "/r"])
            else:
                os.startfile(Trex_path)

except:
    print("Exception!!!!!")
    time.sleep(10)
    subprocess.call(["shutdown", "/r"]) 