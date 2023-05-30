import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
website = input ('enter the website to scan:')
startport = int (input('enter ythe starting port number to scan : '))
endport =int(input('enter the ending port number to scan: '))
def portscan(startport):
    try:
        s.connect((website,startport))
        return True
    except:
        return False
for x in range(startport,endport):
    if portscan(x):
        print('the port ',x,'is open','for' , website)
    else:
        print('the port ',x,'is closed','for',website)