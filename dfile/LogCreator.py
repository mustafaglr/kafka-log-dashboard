import time
import datetime
import random
import os
import glob


logServerCityName = ["Istanbul", "Tokyo", "Moskow", "Beijing", "London"]
logLevel = ["INFO", "WARN", "FATAL", "DEBUG", "ERROR"]

filenames = []

os.chdir("./log")


def writetologfile():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
    exist = glob.glob("logfile*.log")
    if not exist:
        w = open("logfile1.log", "w+")
        w.close()

    for file in glob.glob("*.log"):
        filenames.append([os.path.getctime(file), file])
    getmax = max(filenames)
    filepathnum = getmax[1].split(".")[0][7:]
    if os.path.getsize("logfile"+filepathnum+".log") >= 2000000:
        filepathnum = int(filepathnum) + 1
        w = open("logfile"+str(filepathnum)+".log", "w+")
        w.close()

    f = open("logfile"+str(filepathnum)+".log", "a")
    rand = random.randint(0, 4)
    f.write(st + " " + logLevel[random.randint(0, 4)] + " " + logServerCityName[rand] + " Hello-From-" + logServerCityName[
            rand] + "\n")
    f.close()
    print(st + " " + logLevel[random.randint(0, 4)] + " " + logServerCityName[rand] + " Hello-From-" + logServerCityName[
            rand] + "\n")

while True:
    time.sleep(1)
    writetologfile()
