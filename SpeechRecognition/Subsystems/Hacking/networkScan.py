#Scan for all smart appliances on the current LAN
from socket import *
import time

#Function for scanning for ports on supplied addresses

def portScan(ipAddress):

    portList = []
    target = gethostbyname(ipAddress)
    print ('Starting scan on host: ', target)

    startTime = time.time()
    for i in range(1, 100):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((target, i))
        if(conn == 0) :
            portList.append('Port %d: OPEN' % (i,))
        s.close()
    return portList
    print('Time taken:', time.time() - startTime)

#Works!
#portScan("192.168.0.1")
