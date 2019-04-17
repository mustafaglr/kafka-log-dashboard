import os
import glob

filenames = []
oldfilepathnum = 0
os.chdir("./log")

while True:
    for file in glob.glob("*.log"):
        filenames.append([os.path.getctime(file), file])
    getmax = max(filenames)
    filepathnum = getmax[1].split(".")[0][7:]
    if int(oldfilepathnum) < int(filepathnum):
        oldfilepathnum = filepathnum
        os.system("tail -F logfile"+filepathnum+".log -n 0 | ../kafka_2.12-2.2.0/bin/kafka-console-producer.sh --broker-list=localhost:9092 --topic my-topic &")
