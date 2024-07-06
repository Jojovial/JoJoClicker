import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char='t')

class AutoClicker:
    def __init__(self):
        self.clicking = False
        self.mouse = Controller()
        self.click_thread = threading.Thread(target=self.clicker)
        self.listener = Listener(on_press=self.toggle_event)

    def clicker(self):
        while True:
            if self.clicking:
                self.mouse.click(Button.left, 1)
                time.sleep(0.0001)

    def toggle_event(self, key):
        if key == TOGGLE_KEY:
            self.clicking = not self.clicking

    def start(self):
        self.click_thread.start()
        with self.listener as listener:
            listener.join()

if __name__ == "__main__":
    auto_clicker = AutoClicker()
    auto_clicker.start()
