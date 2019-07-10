#Scan for all smart appliances on the current LAN
from socket import *
import time

#Function for scanning for ports on supplied addresses

def portScan(ipAddress):

    target = gethostbyname(ipAddress)
    print ('Starting scan on host: ', target)

    startTime = time.time()
    for i in range(1, 1024):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((target, i))
        if(conn == 0) :
            return 'Port %d: OPEN' % (i,)
        s.close()

    print('Time taken:', time.time() - startTime)

#Works!
#portScan("192.168.0.1")
