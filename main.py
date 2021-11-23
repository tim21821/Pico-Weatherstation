from machine import PWM, Pin
import time
from display import LCD_2inch, BL
import draw


if __name__== '__main__':
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)#max 65535

    LCD = LCD_2inch()
    #color BRG
        
    cloud_positions = [[130, 100], [50, 30], [20, 80], [200, 50], [250, 90]]
    
    key0 = Pin(15,Pin.IN,Pin.PULL_UP) 
    
    while True:
        LCD.fill(LCD.SKY_BLUE)
        for x, y in cloud_positions:
            draw.draw_cloud(LCD, x, y)
        LCD.show()
        for position in cloud_positions:
            position[0] += 1
            position[0] %= LCD.width
        
        time.sleep(0.5)
    
    