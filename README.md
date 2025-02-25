<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>RGB LED Color Modes on Raspberry Pi Pico</h1>
    <p>This project allows you to toggle between different <strong>RGB LED color modes</strong> using a button. It utilizes <strong>PWM control</strong> with a Raspberry Pi Pico and supports multiple lighting effects, including a <strong>rainbow effect</strong>.</p>
    <h2>🛠 Hardware Requirements</h2>
    <ul>
        <li>Raspberry Pi Pico</li>
        <li>12V 5050 RGB LED strip</li>
        <li>IRLZ34N MOSFETs (x3, one per color channel)</li>
        <li>12V power supply</li>
        <li>Tactile Button (for switching modes)</li>
        <li>Jumper wires</li>
    </ul>  
    <h2>🔌 Wiring Diagram</h2>
    <table>
        <tr><th>Component</th><th>Pi Pico (GPIO)</th><th>Connection</th></tr>
        <tr><td>Red LED</td><td>GP17</td><td>MOSFET Gate 1</td></tr>
        <tr><td>Green LED</td><td>GP19</td><td>MOSFET Gate 2</td></tr>
        <tr><td>Blue LED</td><td>GP16</td><td>MOSFET Gate 3</td></tr>
        <tr><td>Button</td><td>GP14</td><td>One side to GP14, other to 3.3V</td></tr>
    </table>
    <p><strong>Note:</strong> The <strong>MOSFET drain</strong> connects to the LED strip, and the <strong>source</strong> goes to ground.</p> 
    <h2>💾 Software Setup</h2>
    <ol>
        <li>Install <strong>CircuitPython</strong> on your Raspberry Pi Pico.</li>
        <li>Use <strong>Thonny IDE</strong> or another CircuitPython-compatible editor.</li>
        <li>Copy the provided <code>main.py</code> script to your Pico.</li>
    </ol>
    <h2>📝 Code Overview</h2>
    <ul>
        <li>Uses <strong>PWM (Pulse Width Modulation)</strong> to control LED brightness.</li>
        <li>Converts <strong>HSV (Hue, Saturation, Value) to RGB</strong>.</li>
        <li>Cycles through different color modes based on button presses.</li>
    </ul>
    <h2>🎨 Available Color Modes</h2>
    <ul>
        <li><strong>Rainbow</strong> - Smoothly cycles through all colors.</li>
        <li><strong>Orange</strong> - Displays a solid orange color.</li>
        <li><strong>Fade Red to Blue</strong> - Gradually transitions between red and blue.</li>
        <li><strong>Solid Red</strong> - Displays a static red color.</li>
        <li><strong>Solid Blue</strong> - Displays a static blue color.</li>
    </ul>
    <h2>🚀 Running the Code</h2>
    <ol>
        <li>Save the script as <code>main.py</code> on the Pico.</li>
        <li>Restart the board, and use the button to switch between modes.</li>
    </ol>
    <h2>✨ Adjusting Brightness</h2>
    <p>Modify the <strong>brightness factor</strong> in the script:</p>
    <pre><code>BRIGHTNESS = 0.5  # Set between 0.0 (off) and 1.0 (full brightness)</code></pre>
    <h2>🧙🏼‍♂️ Troubleshooting</h2>
    <ul>
        <li><strong>One color not working?</strong> Check wiring & GPIO assignments.</li>
        <li><strong>Dim output?</strong> Verify MOSFETs and 12V power supply.</li>
        <li><strong>No mode changes?</strong> Ensure the button is wired correctly and script is running.</li>
    </ul>
    <h2>📝 Purchase Links</h2>
    <ul>
        <li><a href="https://amzn.to/3IMwLLY" target="_blank">IRLZ34N MOSFETs</a></li>
        <li><a href="https://www.amazon.com/Daybetter-Lights-Control-Bedroom-Changing/dp/B08JSFH1G6/ref=sr_1_4" target="_blank">Daybetter 5050 RGB LED Strip</a></li>
        <li><a href="https://www.amazon.com/Aceirmc-Current-Converter-Adjustable-Regulator/dp/B082XQC2DS/ref=sr_1_3" target="_blank">5V to 12V Converter XL6019</a></li>
        <li><a href="https://www.digikey.com/short/qvv443bd" target="_blank">Tactile Button</a></li>
    </ul>
    <p>Enjoy your <strong>RGB LED color modes</strong>! </p>
</body>
</html>
