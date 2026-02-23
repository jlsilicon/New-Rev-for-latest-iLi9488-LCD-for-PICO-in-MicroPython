# New-Rev-for-latest-iLi9488-LCD-for-PICO-in-MicroPython
This is a new Tested Working Code Rev for the latest iLi9488 LCD in MicroPython 

-

Schematic :
https://content.instructables.com/FSZ/UTYB/KSONJ988/FSZUTYBKSONJ988.jpg?frame=true&width=1024&height=1024&fit=bounds

I tried it with no luck.
I commented out the images Loop.
Additionally , I added drawing different Colors and Sizes of Rectangles every 3 seconds on the Screen.
But, all I can get is a Blank White screen.

-

Code in Progress :

So far :

Fixed Color codes to 3-bytes RGB , not 2-bytes code, also Color Codes Inverted (255 - Byt).
Code draws colored rectangles on screen.

https://github.com/jlsilicon/New-Rev-for-latest-iLi9488-LCD-for-PICO-in-MicroPython/tree/main

-

Busy working on Fixing it.

Original code only gives you a White screen.

2nd modified version only draws in Gray (with Black and White) shades.

-

Bad / wrong color coding format being sent to the LCD.

-

Working Functions : 

    ## clear_rgb(rgb_list) ##
    display.clear_rgb([127,127,255])
    
    # draw_rgb_pixel(x, y, [R,G,B])
    display.draw_rgb_pixel(5, 5, [255,127,0])

    # draw_line_rgb(self, x1, y1, x2, y2, rgb_list )
    display.draw_line_rgb( 111, 111, 122, 233, [255,127,0] )

    # draw_rectangle_rgb( x, y, w, h, rgb_list):
    display.draw_rectangle_rgb( 10, 10, 400, 300, [0,255,255])

    # draw_ellipse_rgb(self, x0, y0, a, b, color) 
    display.draw_ellipse_rgb( 120, 120, 122, 133, [127,255,0])

    # fill_ellipse_rgb(self, x0, y0, a, b, rgb_list )
    display.fill_ellipse_rgb( 80, 90, 70, 60, [255,127,0] )

    # fill_vrect_rgb( X,Y, W,H, [R,G,B] )
    display.fill_vrect_rgb(0,0, 50,50, [127,127,127] )

