import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius, colors, TextField


class GreetingsApp(UserControl):
    def build(self):
        first_name = TextField(label="First name", autofocus=True)
        last_name = TextField(label="Last name")
        greetings = Column()

        def btn_click(e):
            greetings.controls.append(Text(f"Hello, {first_name.value} {last_name.value}!"))
            first_name.value = ""
            last_name.value = ""
            self.update()
            first_name.focus()

        return Container(
            content=Column(
                controls=[
                    first_name,
                    last_name,
                    ElevatedButton(text="Say hello!", on_click=btn_click),
                    greetings,
                ],
            )
        )
