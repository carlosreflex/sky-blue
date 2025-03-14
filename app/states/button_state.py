
import reflex as rx

class ButtonState(rx.State):
    count: int = 0

    @rx.event
    def increment(self):
        self.count += 1

