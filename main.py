# This is a sample Python script.
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

delay = 0.01
button = Button.left
start_stop_key = KeyCode(char='s')
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

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

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
    listener.join()
