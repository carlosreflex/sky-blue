
import reflex as rx
from app.components.button import blue_button

def index() -> rx.Component:
    return blue_button()

app = rx.App(theme=rx.theme(appearance="light"))
app.add_page(index)