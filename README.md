# PRODIGY_CS_04

Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

Before running this program, make sure you have pynput installed:

pip install pynput

Explanation:

Key Logging: The on_press function captures each key press. It writes printable characters directly to the file, while special keys (like Enter or Space) are enclosed in brackets ([Key.space] for readability).

Stopping Condition: The on_release function includes a condition to stop the keylogger, which is useful during testing. Replace 'exit' with an actual exit condition based on a specific keystroke or manual intervention.

Listener Setup: The Listener class from pynput.keyboard listens for key events and calls on_press for each keypress. It will continue to log until the on_release condition stops it.

Important Note:
Keylogging code should never be distributed without proper authorization. This example is for educational purposes within a controlled, consented environment.
