import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius, colors

from Apps.Calc.Calclator_final import CalculatorApp
from Apps.Greetings.Greetings import GreetingsApp


def main(page: Page):
    page.title = "Calc App"

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)

    greetings = GreetingsApp()
    page.add(greetings)

    text = Text(value="Hello World!")
    page.add(text)


flet.app(target=main)
