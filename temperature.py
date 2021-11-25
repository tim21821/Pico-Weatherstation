import machine


TEMP_SENSOR = machine.ADC(4)
CONVERSION_FACTOR = 3.3 / 65535


def get_cpu_temp():
    """Reads the CPU temperature of the Raspberry Pi Pico.

    :return: The measured temperature in °C.
    :rtype: float
    """
    
    # read voltage, that is proportional to temperature and convert it
    conv_voltage = TEMP_SENSOR.read_u16() * CONVERSION_FACTOR
    temp = 27 - (conv_voltage - 0.706) / 0.001721
    return temp
