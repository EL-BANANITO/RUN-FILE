import socket as soc
import gspread as gs
import os

json = gs.service_account(filename='json file name')#connect to google sheet account
opensheet = json.open("google sheet file name").sheet1#open  google sheet file
hostname = soc.gethostname()#your pc hostname name

#lists
row = opensheet.row_values("1")
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = list[row.index(hostname)]
row2 = opensheet.row_values(x + "3")

#Check if the host is in the list
if (hostname in row) :
    opensheet.update(str(list[len(row)]) + '3', 'no')
elif len(row) == 0:
    opensheet.update("A1", hostname)
else:
    opensheet.update(str(list[len(row)]) + '1', hostname)
    opensheet.update(str(list[len(row)]) + '3', 'no')

#Check start or no
while True:
    if 'yes' in row2:
        os.startfile("file name")#run file
    else:
        print('stop!')