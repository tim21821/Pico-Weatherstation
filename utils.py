def rgb_to_hex565(rgb):
    """Turns a RGB triple into a hex565 BRG code

    :param rgb: Triple of RGB values (0 to 255)
    :type rgb: list
    :return: Hex565 BRG code of the RGB color
    :rtype: str
    """
    red, green, blue = rgb
    return "%0.4X" % (
        (int(blue / 255 * 31) << 11)
        | (int(red / 255 * 63) << 5)
        | (int(green / 255 * 31))
    )


if __name__ == "__main__":
    print(rgb_to_hex565([255, 255, 255]))
