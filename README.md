<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RGB LED Rainbow Effect on Raspberry Pi Pico</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1, h2 { color: #333; }
        code { background: #f4f4f4; padding: 2px 5px; border-radius: 4px; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        table, th, td { border: 1px solid #ddd; padding: 8px; }
        th { background: #f4f4f4; }
    </style>
</head>
<body>
    <h1>RGB LED Rainbow Effect on Raspberry Pi Pico</h1>
    <p>This project creates a <strong>rainbow effect</strong> on an RGB LED strip using <strong>PWM control</strong> with a Raspberry Pi Pico. It cycles through colors smoothly using <strong>HSV to RGB conversion</strong>.</p>
    
    <h2>🛠 Hardware Requirements</h2>
    <ul>
        <li>Raspberry Pi Pico</li>
        <li>12V 5050 RGB LED strip</li>
        <li>IRLZ34N MOSFETs (x3, one per color channel)</li>
        <li>12V power supply</li>
        <li>Jumper wires</li>
    </ul>
    
    <h2>📌 Wiring Diagram</h2>
    <table>
        <tr><th>LED Strip</th><th>Pi Pico (GPIO)</th><th>MOSFET Gate</th></tr>
        <tr><td>Red</td><td>GP17</td><td>Gate 1</td></tr>
        <tr><td>Green</td><td>GP19</td><td>Gate 2</td></tr>
        <tr><td>Blue</td><td>GP16</td><td>Gate 3</td></tr>
    </table>
    <p><strong>Note:</strong> The <strong>MOSFET drain</strong> connects to the LED strip, and the <strong>source</strong> goes to ground.</p>
    
    <h2>💾 Software Setup</h2>
    <ol>
        <li>Install <strong>MicroPython</strong> on your Raspberry Pi Pico.</li>
        <li>Use <strong>Thonny IDE</strong> or another MicroPython-compatible editor.</li>
        <li>Copy the provided <code>main.py</code> script to your Pico.</li>
    </ol>
    
    <h2>📜 Code Overview</h2>
    <ul>
        <li>Uses <strong>PWM (Pulse Width Modulation)</strong> to control LED brightness.</li>
        <li>Converts <strong>HSV (Hue, Saturation, Value) to RGB</strong>.</li>
        <li>Cycles through colors smoothly for a rainbow effect.</li>
    </ul>
    
    <h2>🚀 Running the Code</h2>
    <ol>
        <li>Save the script as <code>main.py</code> on the Pico.</li>
        <li>Restart the board, and the rainbow effect should begin.</li>
    </ol>
    
    <h2>🎨 Adjusting Brightness</h2>
    <p>Modify the <strong>brightness factor</strong> in the script:</p>
    <pre><code>BRIGHTNESS = 0.5  # Set between 0.0 (off) and 1.0 (full brightness)</code></pre>
    
    <h2>🛠 Troubleshooting</h2>
    <ul>
        <li><strong>One color not working?</strong> Check wiring & GPIO assignments.</li>
        <li><strong>Dim output?</strong> Verify MOSFETs and 12V power supply.</li>
        <li><strong>No color change?</strong> Ensure the script is running without errors.</li>
    </ul>
    
    <p>Enjoy your <strong>rainbow LED effect</strong>! 🌈✨</p>
</body>
</html>

