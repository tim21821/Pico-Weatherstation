def rgb_to_hex565(rgb):
    blue, red, green = rgb[0], rgb[1], rgb[2]
    return ("%0.4X" % ((int(blue / 255 * 31) << 11) | (int(red / 255 * 63) << 5) | (int(green / 255 * 31))))

if __name__ == "__main__":
    print(rgb_to_hex565([238,243,247]))