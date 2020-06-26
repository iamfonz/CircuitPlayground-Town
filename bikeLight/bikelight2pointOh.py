from adafruit_circuitplayground.express  import cpx
import time

#define animation function to call later in code
def fonz_light_animations():

    for x in range(10):
        cpx.pixels[x] = (20, 20, 20)
        time.sleep(0.1)

    #counter clockwise turn OFF one at a time
    for x in range(10):
        cpx.pixels[x] = (0, 0, 0)
        time.sleep(0.1)
    
    for x in reversed(range(10)):
        cpx.pixels[x] = (20, 20, 20)
        time.sleep(0.1)

    #counter clockwise turn OFF one at a time
    for x in reversed(range(10)):
        cpx.pixels[x] = (0, 0, 0)
        time.sleep(0.1)


#end def fonz_light_animations

while True:
    if cpx.switch: #turn on only when switch is on
        fonz_light_animations()
    else:
        cpx.pixels.fill((0, 0, 0))
