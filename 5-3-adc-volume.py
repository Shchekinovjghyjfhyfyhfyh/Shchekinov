import RPi.GPIO as gp
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

gp.setmode(gp.BCM)

gp.setup(dac, gp.OUT)
gp.output(dac, gp.LOW)

# gp.setup(troyka, gp.OUT, initial=1)
gp.setup(troyka, gp.OUT, initial = 1)
gp.output(troyka, gp.HIGH)
# gp.output(troyka, 200)

gp.setup(leds, gp.OUT)
gp.output(leds, gp.LOW)

gp.setup(comp, gp.IN)

def dectobin(a:int) -> list:
    # print(f'a: {a}')
    return [int(q) for q in bin(a)[2:].zfill(8)]

def adc():
    out = [0,0,0,0,0,0,0,0]
    for q in range(8):
        out[q] = 1
        # print(out)
        gp.output(dac, out)
        time.sleep(0.05)
        if not gp.input(comp):
            out[q] = 0
        # print(out)
        # time.sleep(0.5)

    return int(''.join([str(q) for q in out]), 2)


try:
    GLOBAL_VOLT = 3.3
    while True:
        val = adc()
        # print('---')
        # print(val)
        # continue
        # volt = val
        k = int(val/255*8)
        k = [0]*(8-k) + [1]*k
        gp.output(leds, k)
        volt= val/255*GLOBAL_VOLT
        print(f'volt: {volt:.4}')

        # gp.output(dac, [1,0,0,0,0,0,0,0])
        # time.sleep(0.1)
        # print(gp.input(comp))
finally:
    gp.output(dac, gp.LOW)
    gp.output(leds, gp.LOW)
    # gp.output(troyka, gp.LOW)
    gp.cleanup()


