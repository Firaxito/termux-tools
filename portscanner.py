from threading import Thread
import socket


host = str(input('host > '))
from_port = int(input('start scan from port > ') or 0)
to_port = int(input('finish scan to port > ') or 65535)
counting_open = []
counting_close = []
threads = []


def scan(port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((host, port))
    if result == 0:
        counting_open.append(port)
        print((str(port))+' !!!!!!!!!  -> OPEN <-- !!!!!!!!!!')
        s.close()
    else:
        counting_close.append(port)
        print((str(port))+' -> closed ', counting_open)
        s.close()

counter = 0
for i in range(from_port, to_port):
    t = Thread(target=scan, args=(i,))
    threads.append(t)
    t.start()
    counter = counter + 1
    if counter == 10:
        counter = 0
        [x.join() for x in threads]
        threads.clear()


print(counting_open)