### iLi9488_b_test.py.py
# from https://github.com/QiaoTuCodes/MicroPython-_ILI9488/issues/4
# - WORKS - needs FIXES ...


#main.py
#for pi pico

from    time          import sleep
# from    ili9488       import Display
from    ili9488_ch_2  import Display , color666 
from    machine       import Pin, SPI
import  random


def test():
    """Test code."""
    
    # Baud rate of 60000000 seems about the max
    ## SCK=14 , MOSI=13 , DC=21 , CS=15 , RST=33 
#    spi = SPI(1, baudrate=60000000, sck=Pin(14), mosi=Pin(13))
#    display = Display(spi, dc=Pin(21), cs=Pin(15), rst=Pin(33))
    
    # Baud rate of 60000000 seems about the max
    ## SCK=2 , MOSI=3 , DC=23 , CS=5 , RST=13 
#    spi = SPI( 0, baudrate=60000000, sck=Pin(2), mosi=Pin(3) )
#    display = Display( spi, dc=Pin(12), cs=Pin(5), rst=Pin(13), width=480, height=320, rotation=0)
    
    ## SCK=6 , MOSI=7 , DC=2 , CS=0 , RST=1 
    spi = SPI( 0, baudrate=60000000, sck=Pin(6), mosi=Pin(7) )
#    spi = SPI( 0, baudrate=1000000, sck=Pin(6), mosi=Pin(7) )
    display = Display( spi, dc=Pin(2), cs=Pin(0), rst=Pin(1))

    #

    def  Fill_Rect_RGB( X , Y , W , H  ,  R,G,B ) :
        
        for yy in range( Y , (Y + H - 1) ) :
            for xx in range( X , (X + W - 1) ) :
#                display.draw_rgb_pixel( xx , yy , [R,G,B] )
                display.draw_rgb_pixel( xx , yy , [255-R,255-G,255-B] )


    '''
    for y in range(0xf8):
        for x in range(0xfc):
#            display.draw_pixel(160, i, color565(255, 0, 0))
#            display.draw_rgb_pixel(x, y, [y,x,0])
            display.draw_rgb_pixel(x, y, [0xF7-y,0xFB-x,0xF7-0] )
#            display.draw_rgb_pixel(x, y, 0xFFFF-display.color565(y, x, 0))
#            display.draw_rgb_pixel( x , y , (((y) & 0xf8) << 8) | (((x) & 0xfc) << 3) | ((0) >> 3) )
    sleep(1)
    '''

    print("\n> ... Fill Rect GRAY ... ")
#    display.fill_vrect(0,0, 320,480,0xFFFF)
#    display.fill_vrect(0,0, 480,320, display.color565(255, 255, 0))
#    display.fill_vrect(0,0, 480,320, [0xFF-0x40,0xFF-0x40,0xFF-0x40])
#    display.fill_vrect(0,0, 50,50, ((0x3800)+(0x01E0)+(0x0007)) )
    display.fill_vrect_rgb(0,0, 50,50, [127,127,127] )
#    display.fill_vrect(0,0, 50,50, ((0xF800-0x3800)+(0x07E0-0x01E0)+(0x002F-0x0007)) )
#    sleep(1)

    print("\n> ... Fill Rect BLACK ... ")
#    display.fill_vrect(20,20, 60,60, (0xFFFF-0x0000) )
#    display.fill_vrect_rgb(20,20, 60,60, [255,255,255] )  ## - Neg BLACK 
    display.fill_vrect_rgb(20,20, 50,50, [0,0,0] )  ## - BLACK 
#    sleep(1)

    print("\n> ... Fill Rect RED ... ")
#    display.fill_vrect(60,60, 70,70, (0xF800) )
#    display.fill_vrect_rgb(60,60, 70,70, display.color666(255, 255, 255) )
#    display.fill_vrect_rgb(40,40, 70,70, [0xF7-0xF7,0xFB-0x00,0xF7-0x00] )
#    print("\n> ... Fill Rect RED ... 0 ")
#    display.fill_vrect(30,30, 40,40, (0xF800) )  ## - 2byte RED => GRAY 
#    sleep(1)
    print("\n> ... Fill Rect RED ... 1 ")
#    display.fill_vrect_rgb(35,35, 50,50, [0,255,255] )  ## - Neg RED 
    display.fill_vrect_rgb(35,35, 50,50, [255,0,0] )  ## - Neg RED 
#    sleep(1)
    print("\n> ... Fill Rect BLUE ... 1 ")
#    display.fill_vrect_rgb(40,40, 50,50, [255,255,0] )  ## - Swapped Neg RED => RED 
#    display.fill_vrect_rgb(40,40, 50,50, [255,255,0] )  ## - Neg BLUE 
    display.fill_vrect_rgb(40,40, 50,50, [0,0,255] )  ## - BLUE 
#    sleep(1)
    print("\n> ... Fill Rect CYAN ... 2 ")
#    display.fill_vrect_rgb(45,45, 50,50, [255,0,0] )  ## - RED 
#    display.fill_vrect_rgb(45,45, 50,50, [255,0,0] )  ## - Neg CYAN 
    display.fill_vrect_rgb(45,45, 50,50, [0,255,255] )  ## - CYAN 
#    sleep(1)
    print("\n> ... Fill Rect GREEN ... 2 ")
#    display.fill_vrect_rgb(50,50, 50,50, [255,0,255] )  ## - Neg GREEN 
    display.fill_vrect_rgb(50,50, 50,50, [0,255,0] )  ## - GREEN 
#    sleep(1)
    print("\n> ... Fill Rect YELLOW ... 2 ")
#    display.fill_vrect_rgb(50,50, 50,50, [0,0,255] )  ## - Swapped RED => WHITE
#    display.fill_vrect_rgb(50,50, 50,50, [0,0,255] )  ## - Neg YELLOW 
    display.fill_vrect_rgb(50,50, 50,50, [255,255,0] )  ## - YELLOW 
#    sleep(1)
#    display.fill_vrect(70,70, 80,80, (0x07FF) )
#    display.fill_vrect(70,70, 80,80, (0x7FFF) )
#    display.fill_vrect(80,80, 90,90, ((0xF800)|(0x07E0)|(0x002F)) )
#    display.fill_vrect(90,90, 100,100, ((0xF800-0x0000)+(0x07E0-0x07E0)+(0x002F-0x002F)) )
    # Fill_Rect_RGB( X , Y , W , H  ,  R,G,B ) : #
    print("\n> ... Fill Rect ORANGE ... 3 ")
#    Fill_Rect_RGB( 60 , 60 , 60 , 60  ,  255,0,0 )
#    display.fill_vrect_rgb(60,60, 60,60, [0,127,255] )  ## - Neg ORANGE 
    display.fill_vrect_rgb(60,60, 50,50, [255,127,0] )  ## - ORANGE 
#    sleep(1)

    print("\n> ... Fill Rect GREEN ... ")
#    Fill_Rect_RGB( 100 , 100 , 60 , 60  ,  0,255,0 )
#    display.fill_vrect_rgb(100,100, 50,50, [255,0,255] )  ## - Neg GREEN 
    display.fill_vrect_rgb(100,100, 50,50, [0,255,0] )  ## - GREEN 
#    sleep(1)

    print("\n> ... Fill Rect BLUE ... ")
#    Fill_Rect_RGB( 130 , 130 , 60 , 60  ,  0,0,255 )
#    display.fill_vrect_rgb(130 , 130 , 60 , 60, [255,255,0] )  ## - Neg BLUE 
    display.fill_vrect_rgb(130 , 130 , 50 , 50, [0,0,255] )  ## - BLUE 
#    sleep(1)

    print("\n> ... Fill Rect RED ... ")
    display.fill_vrect_rgb(150,150, 50,50, [255,0,0] )  ## - RED 
#    sleep(1)

    print("\n> ... Fill Rect ORANGE ... ")
#    Fill_Rect_RGB( 160 , 160 , 60 , 60  ,  255,127,0 )
#    display.fill_vrect_rgb(160,160, 60,60, [0,127,255] )  ## - Neg ORANGE 
    display.fill_vrect_rgb(160,160, 50,50, [255,127,0] )  ## - ORANGE 
#    sleep(1)

    print("\n> ... Fill Rect YELLOW ... ")
#    Fill_Rect_RGB( 180 , 180 , 60 , 60  ,  255,255,0 )
#    display.fill_vrect_rgb(180 , 180, 50,50, [0,0,255] )  ## - Neg YELLOW 
    display.fill_vrect_rgb(170 , 170, 50,50, [255,255,0] )  ## - YELLOW 
#    sleep(1)

    print("\n> ... Fill Rect GREEN ... ")
    display.fill_vrect_rgb(180 , 180, 50,50, [0,255,0] )  ## - GREEN 
#    sleep(1)

    print("\n> ... Fill Rect CYANA ... ")
#    Fill_Rect_RGB( 190 , 190 , 60 , 60  ,  0,255,255 )
#    display.fill_vrect_rgb(190 , 190, 50,50, [255,0,0] )  ## - Neg CYAN 
    display.fill_vrect_rgb(190 , 190, 50,50, [0,255,255] )  ## - CYAN 
#    sleep(1)

    print("\n> ... Fill Rect BLUE ... ")
    display.fill_vrect_rgb(200 , 200, 50,50, [0,0,255] )  ## - BLUE 
#    sleep(1)

    print("\n> ... Fill Rect PURPLE ... ")
#    Fill_Rect_RGB( 200 , 200 , 60 , 60  ,  255,0,255 )
#    display.fill_vrect_rgb(200 , 200, 50,50, [0,255,0] )  ## - Neg PURPLE 
    display.fill_vrect_rgb(210 , 210, 50,50, [255,0,255] )  ## - Neg PURPLE 
    sleep(1)


print("> Start > :")

test()

print("< Done . <")

###


