import time
from datetime import datetime as dt # now we dont have to do datetime.datetime
#if we only did import datetime as dt, then it would be dt.datetime
# so dt.now() is the same as dt.datetime now ()

host_temp = 'hosts'
#using the r allows us to escape escape characters

hosts_path = r'C:\Windows\system32\drivers\etc\hosts'
redirect = '127.0.0.1'
sites_that_kills_me = ['www.facebook.com', 'facebook.com','manganelo.com']

# these elements need their own respective lines on the host file and redirect IP
print(dt.now())

while True:
    # if you look at output of dt.now() you will see the output format
    # we are creating 3 datetime objects and comparing them
    if dt(dt.now().year, dt.now().month, dt.now().day, 10)  < dt.now()  <  dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print('Working Hours: ')
# now we can load, read and write to the hosts file, using the r+ allows reading and writing to the file

        with open(hosts_path,'r+') as file:
            content = file.read() #this will load the entire file
            for site in sites_that_kills_me:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    else:
        with open(hosts_path,'r+') as file:
# the read lines method will produce a list with each str item
# then check the read lines list against our istes that kill me list, and if items them I want them out
            content = file.readlines()
# once readline is complete the pointer will be sitting at the very end of the file
# so any append method will add from the point of the pointer
# the seek method will place pointer where we want
            file.seek(0)
            for line in content:
# if item not there, append a new file hosts via writing a new file
                if not any(site in line for site in sites_that_kills_me):
                    file.write(line)
# truncate method will delete all things UNDER the specified section
            file.truncate()
        print('time to play!!!')
    time.sleep(10)