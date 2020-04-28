
from netmiko import ConnectHandler
from os import path, mkdir
from csv import DictReader
from datetime import datetime

CFG_FILE = "devices.csv"                                            # Define variables
WORK_DIR = path.dirname(path.realpath(__file__))
OUT_FILE = path.join(WORK_DIR,"output.txt")                         # output file (for console report copy)
BCKP_DIR = path.join(WORK_DIR,"config_backups\\")                   # backup directory fullpath
NTP_SRV = "88.147.254.230"                                          # NTP server address

def main():

    if not path.exists(BCKP_DIR): mkdir(BCKP_DIR)                   # Creating a backup directory (if not exist)

    device_list = list()  
    with open(CFG_FILE, 'r') as f:                                  # Reading device list from CSV-file
        reader = DictReader(f, delimiter=',')
        for row in reader: device_list.append(row)
    file = open(OUT_FILE, 'w')

    for dev_data in device_list:                                    # For each device in device list
        try:                                                        # Trying connect to device
            crt = ConnectHandler(**dict(dev_data))
            crt.enable()
        except:
            print("Connection failuire to {}".format(dev_data["host"]))
            continue
                                                                    # Executing homework tasks
        strCDP = Task2_CheckCDP(crt)
        SW_Info = Task3_GetSWInfo(crt)
        strSync = Task4_SetNTPTime(crt)
        strName = Task1_GetCfg(crt)

        strRes = "{} | {} | {} | {} | {} | {}".format(strName,      # task 5 - print device report string
            SW_Info[2], SW_Info[0], SW_Info[1], strCDP, strSync)
        print(strRes)                                               #   print to console
        file.write(strRes + '\n')                                   #   print to file

    file.close()
 
def Task1_GetCfg(c):                                                # task 1 - save device configuration on disk
    strConfig = c.send_command("show running-config")
    strFileName = "{}_{}.cfg".format(
        datetime.now().strftime("%Y-%m-%d"), c.base_prompt)
    with open(BCKP_DIR + strFileName, 'w') as file:
        file.write(strConfig)
    return c.base_prompt
    
def Task2_CheckCDP(c):                                              # task 2 - check CDP and neighbors count
    str1 = c.send_command("show cdp neighbors")
    isRun = "OFF"; iPeersCnt = 0
    if not ("CDP is not" in str1):
        isRun = "ON" 
        iPeersCnt = int(str1.partition("entries displayed : ")[2])
    return "CDP is {}, {} peers".format(isRun, iPeersCnt)

def Task3_GetSWInfo(c):                                             # task 3 - check software type and get device info
    str1 = c.send_command("show version")
    strSW = str1.partition(" Software (")[2].partition("), ")[0]    #   get SW version info
    strNPE = "NPE" if ("NPE" in strSW) else "PE "                   #   check software type (NPE or PE)
    str1 = c.send_command("show inventory")
    strMOD = str1.partition("PID: ")[2].partition(" , VID:")[0]     #   get HW model info
    return [strSW, strNPE, strMOD]

def Task4_SetNTPTime(c):                                            # task 4 - set timezone and correct NTP config
    str1 = c.send_command("ping {}".format(NTP_SRV))                #   check ntp-server availability
    if "100 percent" in str1:                                          
        c.send_config_set("ntp server {}".format(NTP_SRV))          #   add ntp server reference
    c.send_config_set("clock timezone GMT 0")                       #   set GMT timezone
    strSync = "Clock is not Sync"                                          
    if ("is sync" in c.send_command("show ntp status")):            #   check ntp sync status
        strSync = "Clock is Sync"
    return strSync
    
if __name__ == "__main__": main()
