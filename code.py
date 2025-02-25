import board
import digitalio
import pwmio
import time

# Define RGB LED pins
red = pwmio.PWMOut(board.GP17, frequency=5000, duty_cycle=0)
green = pwmio.PWMOut(board.GP19, frequency=5000, duty_cycle=0)
blue = pwmio.PWMOut(board.GP16, frequency=5000, duty_cycle=0)

# Define button pin
button = digitalio.DigitalInOut(board.GP14)
button.switch_to_input(pull=digitalio.Pull.DOWN)

SLEEP = 0.005  # Speed of transition
mode = 0  # Current mode index
lastButtonState = 0  # Track previous button state

# Color modes: (Rainbow effect, Orange, Fade red to blue, Solid Red, and Solid Blue)
colorModes = ["Rainbow", "Orange", "FadeRedtoBlue", "Red", "Blue"]

def duty_cycle(percent):
    """Converts a percentage (0-100) to a 16-bit PWM duty cycle (0-65535)."""
    return int(percent / 100.0 * 65535.0)

def hsv_to_rgb(h, s, v):
    """Converts HSV to RGB (0-255 range)."""
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
    buttonState = button.value

    # Detect button press (edge detection)
    if buttonState and not lastButtonState:
        mode = (mode + 1) % len(colorModes)  # Cycle through modes
        print(f"Mode changed to: {colorModes[mode]}")
        time.sleep(0.2)  # Debounce delay

    lastButtonState = buttonState  # Update last state

    # Apply the selected mode
    if colorModes[mode] == "Rainbow":  
        hue = 0  # Start hue at 0
        while colorModes[mode] == "Rainbow":
            r, g, b = hsv_to_rgb(hue, 0.75, 0.75)  
            red.duty_cycle = duty_cycle(r)
            green.duty_cycle = duty_cycle(g)
            blue.duty_cycle = duty_cycle(b)
            time.sleep(SLEEP)

            hue = (hue + 1) % 360  # Increment hue

            # **Check for button press inside loop to exit immediately**
            if button.value:
                mode = (mode + 1) % len(colorModes)  
                print(f"Mode changed to: {colorModes[mode]}")
                time.sleep(0.2)  # Debounce delay
                break  # Exit the loop

    elif colorModes[mode] == "Orange":
        red.duty_cycle = duty_cycle(100)
        green.duty_cycle = duty_cycle(65)  # Adjust for orange
        blue.duty_cycle = 0

    elif colorModes[mode] == "FadeRedtoBlue":
        fade_amount = 1
        value = 0
        increasing = True
        while colorModes[mode] == "FadeRedtoBlue":
            red.duty_cycle = duty_cycle(100 - value)
            blue.duty_cycle = duty_cycle(value)

            if increasing:
                value += fade_amount
                if value >= 100:
                    increasing = False
            else:
                value -= fade_amount
                if value <= 0:
                    increasing = True

            time.sleep(0.02)

            # **Check for button press inside loop to exit immediately**
            if button.value:
                mode = (mode + 1) % len(colorModes)  
                print(f"Mode changed to: {colorModes[mode]}")
                time.sleep(0.2)  # Debounce delay
                break  # Exit the loop

    elif colorModes[mode] == "Red":
        red.duty_cycle = duty_cycle(100)
        green.duty_cycle = 0
        blue.duty_cycle = 0

    elif colorModes[mode] == "Blue":
        red.duty_cycle = 0
        green.duty_cycle = 0
        blue.duty_cycle = duty_cycle(100)
