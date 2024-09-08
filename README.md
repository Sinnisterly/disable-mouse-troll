

# Console Window Mover and Click Disabler

This Python script hides a console window, moves it to random locations on the screen at random intervals, and disables left mouse clicks inside the window. The script runs continuously until the `END` key is pressed.

## Features

- Hides the console window upon starting the script.
- Moves the hidden console window to random positions on the screen every 1 to 120 seconds.
- Disables left mouse clicks if the mouse is inside the boundaries of the console window.
- Monitors for the `END` key to terminate the script.

## Requirements

The following Python packages are required for the script:

- `pyautogui` - Used to detect the mouse position, screen size, and mouse control.
- `pygetwindow` - To interact with the console window, allowing it to be moved and hidden.
- `keyboard` - To listen for key presses (`END` key) to stop the script.
- `random` - For generating random intervals and positions.
- `time` - To manage delays and intervals.

Install the required packages using pip:

```bash
pip install pyautogui pygetwindow keyboard
```

## How to Use

1. Open a console window with the title containing "Console".
2. Run the script using Python:

```bash
python script.py
```

3. The script will hide the console window and begin moving it randomly on the screen.
4. Left mouse clicks will be disabled inside the console window area.
5. To exit the script, press the `END` key on your keyboard.

## How the Script Works

1. **Console Window Handling**:  
   The script locates the first window with the title "Console" and hides it.
   
2. **Random Movement**:  
   The script moves the console window to a random position on the screen every 1 to 120 seconds. It ensures the window remains within the screen boundaries.

3. **Click Disabling**:  
   The script continuously checks the mouse position. If the mouse is inside the hidden console window, and the left mouse button is clicked, the script releases the click to prevent interaction with the console.

4. **Exit Condition**:  
   The script listens for the `END` key. Once pressed, it exits the loop and terminates.

## Example

Here's an example of running the script:

```bash
python scriptnamehere.py
```

While running, the script will:
- Hide the console window.
- Randomly move the hidden console window every 1 to 120 seconds.
- Block left-clicks when the mouse is inside the hidden console window.
- Exit when the `END` key is pressed.
