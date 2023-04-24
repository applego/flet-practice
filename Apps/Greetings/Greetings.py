import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius, colors, TextField, Ref


class GreetingsApp(UserControl):
    def build(self):
        first_name = Ref[TextField]()
        last_name = Ref[TextField]()
        greetings = Ref[Column]()

        def btn_click(e):
            greetings.current.controls.append(Text(f"Hello, {first_name.current.value} {last_name.current.value}!"))
            first_name.current.value = ""
            last_name.current.value = ""
            self.update()
            first_name.current.focus()

        return Container(
            content=Column(
                controls=[
                    # first_name,
                    # last_name,
                    # この書き方だとfirst_nameやlast_nameが何なのかわからない→Ref（reactを参考）
                    TextField(ref=first_name, label="First name", autofocus=True),
                    TextField(ref=last_name, label="Last name"),
                    ElevatedButton(text="Say hello!", on_click=btn_click),
                    # この書き方だとfirst_nameやlast_nameが何なのかわからない→Ref（reactを参考）
                    # greetings,
                    Column(ref=greetings),
                ],
            )
        )
