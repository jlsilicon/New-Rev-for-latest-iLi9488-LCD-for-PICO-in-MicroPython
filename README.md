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

    # fill_vrect_rgb( X,Y, W,H, [R,G,B] )
    display.fill_vrect_rgb(0,0, 50,50, [127,127,127] )

    # draw_line_rgb(self, x1, y1, x2, y2, rgb_list )
    display.draw_line_rgb( 111, 111, 122, 233, [255,127,0] )

    # def fill_ellipse_rgb(self, x0, y0, a, b, rgb_list )
    display.fill_ellipse_rgb( 80, 90, 70, 60, [255,127,0] )
