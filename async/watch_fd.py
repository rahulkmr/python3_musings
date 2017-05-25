import asyncio
from socket import socketpair

rsock, wsock = socketpair()
loop = asyncio.get_event_loop()

def reader():
    data = rsock.recv(100)
    print(('Received:', data.decode()))
    loop.remove_reader(rsock)
    loop.stop()

loop.add_reader(rsock, reader)
loop.call_soon(wsock.send, 'abc'.encode())
loop.run_forever()

rsock.close()
wsock.close()
loop.stop()
