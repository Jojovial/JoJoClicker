import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')

class AutoClicker:
    def __init__(self, toggle_key=TOGGLE_KEY, click_interval=0.0001):
        self.clicking = False
        self.mouse = Controller()
        self.click_interval = click_interval
        self.toggle_key = toggle_key
        self.click_thread = threading.Thread(target=self.clicker)
        self.listener = Listener(on_press=self.toggle_event)

    def clicker(self):
        """Continuously click the mouse if clicking is enabled."""
        while True:
            if self.clicking:
                self.mouse.click(Button.left, 1)
                time.sleep(self.click_interval)

    def toggle_event(self, key):
        """Toggle the clicking state when the toggle key is pressed."""
        if key == self.toggle_key:
            self.clicking = not self.clicking
            print(f"{'Started' if self.clicking else 'Stopped'} clicking.")

    def start_clicking(self):
        """Start the click thread and listen for the toggle key press."""
        self.click_thread.start()
        with self.listener as listener:
            listener.join()

if __name__ == "__main__":
    auto_clicker = AutoClicker()
    auto_clicker.start_clicking()
