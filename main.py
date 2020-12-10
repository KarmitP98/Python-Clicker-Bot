# This is a sample Python script.
import threading
import time

from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Frequency of Clicks per sec
delay = 0.001
# Click Button
button = Button.left
# Start Stop Key
start_stop_key = KeyCode(char='s')
# Exit Key
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):

    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.button = button
        self.delay = delay
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
        print("Start Clicking")

    def stop_clicking(self):
        self.running = False
        print("Stop Clicking")

    def exit(self):
        self.stop_clicking()
        self.program_running = False
        print("Stop Program")

    def run(self):
        # While the whole program is running
        while self.program_running:
            # While the clicker is clicking
            while self.running:
                # Perform Mouse Click [Left Button]
                mouse.click(self.button)
                # Sleep for delay time
                time.sleep(self.delay)


# Mouse is of type controller
mouse = Controller()
# Create a thread with the function of ClickMouse Class
click_thread = ClickMouse(delay, button)
# Make sure you start the thread at the end. Creates a delay for mounting the listener for some reason
# Start the thread
click_thread.start()

def on_press(key):
    # If Key == "S"
    if key == start_stop_key:
        # If Clicker is clicking
        if click_thread.running:
            # Stop Clicking
            click_thread.stop_clicking()
        else:
            # Start Clicking
            click_thread.start_clicking()
        # If Key == "e"
    elif key == exit_key:
        # Exit Application
        click_thread.exit()
        # Stop Thread
        listener.stop()


# Create Listener for "on_press" ? Not sure about this part
with Listener(on_press=on_press) as listener:
    print("Press 's' to Start Clicking...")
    print("Listener Mounted")
    listener.join()
