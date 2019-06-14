from json import dumps
import confluent_kafka as ck

import os
import glob

filenames = []
oldfilepathnum = 0
oldlinecount=0
oldsizeoffile=0
os.chdir("./log")

p = ck.Producer({'bootstrap.servers': 'kafka:9092'})
while True:
    for file in glob.glob("*.log"):
        filenames.append([os.path.getctime(file), file])
    getmax = max(filenames)
    filepathnum = getmax[1].split(".")[0][7:]
    if int(oldfilepathnum) < int(filepathnum):
        oldfilepathnum = filepathnum
    f = open("logfile"+filepathnum+".log","rb")
    linecount = f.readlines().__len__()
    sizeoffile = os.path.getsize("logfile"+filepathnum+".log")

    if oldlinecount < linecount and oldsizeoffile < sizeoffile:
        f.seek(oldsizeoffile - sizeoffile,os.SEEK_END)
        oldsizeoffile = sizeoffile

        if oldlinecount != 0 and oldlinecount != linecount:
            for read in f.readlines():
                p.poll(0)
                p.produce('mytopic',read.decode("UTF-8").replace("\n", ""))
            p.flush()
        oldlinecount = linecount
