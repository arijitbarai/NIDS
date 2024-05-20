import os
import datetime
import csv

myPath = os.getcwd()
files = os.listdir(myPath)

for f in files:
    if f.endswith("xyz"):
        print(f)
        with open(f, 'r') as fx:
            lines = fx.readlines()

        data = lines[0].split(',')
        print(data)
        mytype = data[0]
        myname = data[1]

        print(mytype+" -- "+myname)
        mynewfilename = (mytype +"-"+str(datetime.date.today())+"-"+myname +"-"+(f.replace(".","-")).replace('xyz','.csv'))

        with open(mynewfilename, 'w', newline='') as new_file:
            writer = csv.writer(new_file)
            for i, line in enumerate(lines):
                if i == 0:
                    print(line)
                else:
                    writer.writerow(line.split(','))
                    print(i, line)

        os.remove(f)

print(" ")