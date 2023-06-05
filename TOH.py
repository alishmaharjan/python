'''
a=[3,2,1]
b=[]
c=[]

def display():      

    print("%10s %10s %10s"%(a,b,c))

def solveHanoi(n, src, dst, aux):

    """Move n discs from src to dst, using the spare peg aux"""

    if n==1:

        dst.append(src[-1])

        del src[-1]

        display()

    else:

        solveHanoi(n-1,src,aux,dst)

        dst.append(src[-1])

        del src[-1]

        display()

        solveHanoi(n-1,aux,dst,src)

display()

solveHanoi(3,a,c,b)


#
import socket
ip = socket.gethostbyname('www.google.com')
print(ip)
'''
'''
#
import socket
import sys
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("socket sucessfully created ")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
    port = 80
    try:
        host = socket.gethostbyname("www.google.com")
    except socket.gaierror:
        print ("there was error resolving the host")
        sys.exit()
    s.connect((host,host))
    print ("the socket has successfully connected to google")
'''
'''
#connecting domain name using socket
import socket
import sys
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print ("Socket successfully created with Address Family IPV4")

#ip = socket.gethostbyname ('www.google.com')
# port=80
except socket.error as err:
    print ("socket creation failed with error message: %s" %(err))
port = 80

try:
    host = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print ("Error resolving the host")
    sys.exit()
s.connect((host, port))
print ("Socket successfully connected to Website")
'''

import socket 
# socket.socket(ipv4,tcp)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Address family IPV4 connected with TCP connection")
ip="34.149.120.3"
#IP=socket.gethostbyname('www.softwarica.edu.np)
port=80
# s.connect(ip,port)
s.connect((ip,port))
print("connection established")