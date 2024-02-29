import dht
from machine import Timer, Pin

d = dht.DHT11(Pin(25))

def read_dht11(*args):
    d.measure()
    print(d.temperature())
    print(d.humidity())


tim1 = Timer(0)
tim1.init(period=2000, mode=Timer.PERIODIC, callback=read_dht11)



