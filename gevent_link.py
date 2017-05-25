import gevent

def tasklet():
    print("Running tasklet")
    return 4

def receiver(g):
    print(g.get())

g = gevent.spawn(tasklet)
g.link(receiver)
g.join()

g = gevent.spawn(tasklet)
try:
    g.link()
    g.join()
except gevent.greenlet.LinkedCompleted as ex:
    print(g.get())
