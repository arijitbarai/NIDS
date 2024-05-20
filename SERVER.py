import sys
import selectors
import socket
import types

import datetime

mySelector = selectors.DefaultSelector()

def filechecker(myfilename):
    fin = open(myfilename, "rt")
    data = fin.read()
    data = data.replace('\n\n', '\n')
    fin.close()
    fin = open(myfilename, "wt")
    fin.write(data)

def accept_waepper(sock):
    conn,addr = sock.accept()
    print("================\At",datetime.datetime.now(),"\nAccepted connection from",addr,"\n--------------")
    print("\U0001f600"*5)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr,inb=b"",outb=b"")
    events = selectors.EVENT_READ|selectors.EVENT_WRITE
    mySelector.register(conn,events,data=data)

def service_connection(key,mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(20480)
        if recv_data:
            data.outb += recv_data
        else:
            print("------------\nAt",datetime.datetime.now(),"\nClosing connection to",data.addr,"\n------------")
            mySelector.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            mySize = sys.getsizeof(repr(data.outb))
            print(mySize,"bytes recived from",data.addr[0]," on port",data.addr[1])
            myfname = ''.join(data.addr[0]).encode()
            myfname = str(myfname)
            myfname += str(data.addr[1])
            myfname += '.xyz'
            f = open(myfname, "ab")
            f.write(((data.outb)))
            f.close()
            filechecker(myfname)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]

if len(sys.argv) != 3:
    print("usage:", sys.argv[0], "<host><port>")
    sys.exit(1)

host, port = sys.argv[1], int(sys.argv[2])
lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind((host,port))
lsock.listen()
print("Listening on ",(host,port))
lsock.setblocking(False)
mySelector.register(lsock,selectors.EVENT_READ, data=None)

try:
    while True:
        events = mySelector.select(timeout=None)
        for key,mask in events:
            if key.data is None:
                accept_waepper(key.fileobj)
            else:
                service_connection(key,mask)
except KeyboardInterrupt:
    print("Caught keyboard interrupt. Exiting")
finally:
    mySelector.close()