
import reflex as rx
from app.components.button import blue_button
from app.components.red_button import red_button

def index() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            blue_button(),
            red_button(),
            class_name="flex flex-col gap-4 items-center"
        )
    )

app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index)