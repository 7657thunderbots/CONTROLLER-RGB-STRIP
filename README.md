RGB LED Rainbow Effect on Raspberry Pi Pico

This project creates a rainbow effect on an RGB LED strip using PWM control with a Raspberry Pi Pico. It cycles through colors smoothly using HSV to RGB conversion.

🛠 Hardware Requirements

Raspberry Pi Pico

12V 5050 RGB LED strip

IRLZ34N MOSFETs (x3, one per color channel)

12V power supply

Jumper wires

📌 Wiring Diagram

LED Strip

Pi Pico (GPIO)

MOSFET Gate

Red

GP17

Gate 1

Green

GP19

Gate 2

Blue

GP16

Gate 3

Note: The MOSFET drain connects to the LED strip, and the source goes to ground.

💾 Software Setup

Install MicroPython on your Raspberry Pi Pico.

Use Thonny IDE or another MicroPython-compatible editor.

Copy the provided main.py script to your Pico.

📜 Code Overview

Uses PWM (Pulse Width Modulation) to control LED brightness.

Converts HSV (Hue, Saturation, Value) to RGB.

Cycles through colors smoothly for a rainbow effect.

🚀 Running the Code

Save the script as main.py on the Pico.

Restart the board, and the rainbow effect should begin.

🎨 Adjusting Brightness

Modify the brightness factor in the script:

BRIGHTNESS = 0.5  # Set between 0.0 (off) and 1.0 (full brightness)

🛠 Troubleshooting

One color not working? Check wiring & GPIO assignments.

Dim output? Verify MOSFETs and 12V power supply.

No color change? Ensure the script is running without errors.

Enjoy your rainbow LED effect! 🌈✨
