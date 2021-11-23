def draw_cloud(screen, x, y, block_size=5):
    OFFSETS = [(5,0, screen.WHITE), (6,0, screen.WHITE), (7,0, screen.WHITE),
               (1,1, screen.WHITE), (2,1, screen.WHITE), (4,1, screen.WHITE), (5,1, screen.WHITE), (6,1, screen.WHITE), (7,1, screen.WHITE), (8,1, screen.WHITE),
               (0,2, screen.WHITE), (1,2, screen.LIGHTER_GREY), (2,2, screen.WHITE), (3,2, screen.WHITE), (4,2, screen.WHITE), (5,2, screen.LIGHT_GREY), (6,2, screen.LIGHT_GREY), (7,2, screen.LIGHTER_GREY), (8,2, screen.LIGHTER_GREY), (9,2, screen.WHITE),
               (0,3, screen.LIGHT_GREY), (1,3, screen.LIGHTER_GREY), (2,3, screen.LIGHTER_GREY), (3,3, screen.WHITE), (4,3, screen.LIGHT_GREY), (5,3, screen.WHITE), (6,3, screen.WHITE), (7,3, screen.WHITE), (8,3, screen.LIGHT_GREY), (9,3, screen.LIGHT_GREY),
               (1,4, screen.LIGHT_GREY), (2,4, screen.LIGHT_GREY), (3,4, screen.LIGHT_GREY), (4,4, screen.LIGHT_GREY), (5,4, screen.LIGHT_GREY), (6,4, screen.LIGHT_GREY), (7,4, screen.LIGHT_GREY), (8,4, screen.LIGHT_GREY)]
    for x_off, y_off, color in OFFSETS:
        screen.fill_rect(x + x_off*block_size, y + y_off*block_size, block_size, block_size, color)