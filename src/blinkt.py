global leds 

leds = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
brightness = 0.2
toClear = True

# blinkt.clear()
def clear():
    global leds 
    leds = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# blinkt.get_pixel(x)
def get_pixel(ledNum):
    return leds[ledNum]

# blinkt.set_all(r, g, b, brightness=None)
def set_all(r,g,b,brightness=brightness):
    for i in range(8):
        leds[i] = [r,g,b,brightness]

# blinkt.set_brightness(brightness)
def set_brightness(brightness):
    brightness = brightness

# blinkt.set_clear_on_exit(value=True)
def set_clear_on_exit(value=True):
    toClear = value

# blinkt.set_pixel(x, r, g, b, brightness=None)
def set_pixel(i,r,g,b,brightness=brightness):
    leds[i] = [r,g,b,brightness]

# blinkt.show()
def show():
    for i in range(len(leds)):
        print(leds[i])