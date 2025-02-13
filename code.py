import board
import pwmio
import time

# Define RGB LED pins
red = pwmio.PWMOut(board.GP17, frequency=5000, duty_cycle=0)
green = pwmio.PWMOut(board.GP19, frequency=5000, duty_cycle=0)
blue = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)

SLEEP = .005  # Speed of transition

def duty_cycle(percent):
    """Converts a percentage (0-100) to a 16-bit PWM duty cycle (0-65535)."""
    return int(percent / 100.0 * 65535.0)

def hsv_to_rgb(h, s, v):
    """Manually converts HSV to RGB (0-255 range)."""
    h = h % 360  # Ensure h is within 0-360
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    return (int((r + m) * 100), int((g + m) * 100), int((b + m) * 100))

while True:
    for hue in range(360):  # Cycle through full rainbow
        r, g, b = hsv_to_rgb(hue, 1, .75)  # Full saturation and brightness
        red.duty_cycle = duty_cycle(r)
        green.duty_cycle = duty_cycle(g)
        blue.duty_cycle = duty_cycle(b)
        time.sleep(SLEEP)

