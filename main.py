from machine import PWM, Pin
import time
from display import LCD_2inch, BL
import draw
import temperature


def main():
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)  # max 65535

    LCD = LCD_2inch()
    key0 = Pin(15, Pin.IN, Pin.PULL_UP)
    key1 = Pin(17, Pin.IN, Pin.PULL_UP)
    key2 = Pin(2, Pin.IN, Pin.PULL_UP)
    key3 = Pin(3, Pin.IN, Pin.PULL_UP)
    # color BRG

    cloud_positions = [[130, 100], [50, 30], [20, 80], [200, 50], [250, 90]]
    lcd_power = True

    while True:
        # keyboard interrupt
        if key0.value() == 0:
            break
        if key1.value() == 0:
            lcd_power = not lcd_power

        if lcd_power:
            # drawing
            LCD.fill(LCD.SKY_BLUE)
            for x, y in cloud_positions:
                draw.draw_cloud(LCD, x, y)

            LCD.text("Temperatur: {:0.1f} °C".format(temperature.get_cpu_temp()), 20, 150)

            LCD.show()

            # update positions
            for position in cloud_positions:
                position[0] += 1
                position[0] %= LCD.width
        else:
            LCD.fill(LCD.BLACK)
            LCD.show()

        time.sleep(0.1)


if __name__ == "__main__":
    main()
