import sys
import os 
import serial
from datetime import datetime
from datetime import date

port = serial.Serial("/dev/ttyACM0", "57600")

now = datetime.now()
start = date.today()
start_mth = start.month
start_day = start.day
file_title = now.strftime('%Y-%m-%d')

while True:
    if ((start_day == date.today().day) and (start_mth == date.today().month)):
        file = open('/home/pi/{0}'.format(file_title), 'a')
    else:
        now = datetime.now()
        start = date.today()
        start_day = start.day
        start_mth = start.month
        file_title = now.strftime('%Y-%m-%d')
        file = open('/home/pi/{0}'.format(file_title), 'a')
    while True:
        file1 = open('/home/pi/{0}'.format(file_title), 'a')
        format_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = port.readline().strip()
        file1.write(format_date)
        file1.write(" ")
        file1.write(data)
        file1.write("\n")
        if (start_day != date.today().day or start_mth != date.today().month):
            break
