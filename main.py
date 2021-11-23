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
    LCD.fill(LCD.SKY_BLUE)
    LCD.show()
    
    draw.draw_cloud(LCD, 130, 100)
    draw.draw_cloud(LCD, 50, 30)
    draw.draw_cloud(LCD, 20, 80)
    draw.draw_cloud(LCD, 200, 50)
    draw.draw_cloud(LCD, 250, 90)
    LCD.show()