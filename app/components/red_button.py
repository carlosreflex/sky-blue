
import reflex as rx
from app.states.button_state import ButtonState

def red_button() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.el.div(
                "Clicks: ",
                ButtonState.count,
                class_name="flex items-center gap-2"
            ),
            on_click=ButtonState.decrement,
            class_name="bg-red-500 hover:bg-red-600 text-white px-6 py-3 rounded-lg transition-colors duration-200"
        ),
        class_name="flex justify-center items-center"
    )

