from adafruit_circuitplayground.express import cpx

while True:
    
    #changes all lights to rgb tuple
    cpx.pixels.fill((25,98,69))

    
    #to control each light reference index
    cpx.pixels[1] = (255, 0, 0)
    cpx.pixels[2] = (255, 85, 0)
    cpx.pixels[3] = ( 255, 255, 0)
    cpx.pixels[4] = (0,255,0)
    cpx.pixels[5] = (34,139,34)
    cpx.pixels[6] = (0, 255, 255)
    cpx.pixels[7] = (0, 0 , 139)
    cpx.pixels[8] = (255, 0, 255)
    cpx.pixels[9] = (75, 0, 130)

