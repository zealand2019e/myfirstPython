from sense_hat import SenseHat
import time

sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

sense.clear()
sense.set_pixel(1,1,yellow)

print type(sense)
   
sense.set_pixel(1,1,blue)
x = 1
y = 0

while(y < 8):
   sense.set_pixel(x,y,green)
   time.sleep(0.3)
   sense.set_pixel(x,y,yellow)
   time.sleep(0.3)
   sense.set_pixel(x,y,red)
   
   if y >= 3:
      sense.set_pixel(x,y-3,nothing)
   
   y = y+1
   

