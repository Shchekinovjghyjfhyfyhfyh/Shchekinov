import RPi.GPIO as gp
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)
gp.output(dac, gp.LOW)

gp.setup(troyka, gp.OUT, initial=1)
# gp.output(troyka, 200)

gp.setup(comp, gp.IN)

def dectobin(a:int) -> list:
    # print(f'a: {a}')
    return [int(q) for q in bin(a)[2:].zfill(8)]

def adc():
    h = 0
    count = 16
    for q in range(1, count+1):
        a = int(q/count*255)
        gp.output(dac, dectobin(a))
        time.sleep(0.1)
        if gp.input(comp):
            h += 1

    return h/count


try:
    while True:
        val = adc()
        volt = val
        # volt= val/8*3.3
        print(f'volt: {volt*3.3}')
finally:
    gp.output(dac, gp.LOW)
    gp.output(troyka, gp.LOW)
    gp.cleanup()


